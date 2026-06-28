#!/usr/bin/env python3
"""Evaluator for multi-invite-to-event-tomas-reyes-billing-5100069 (env-0 tasks-lite)."""

import importlib.util
import os
from pathlib import Path


def _load_needles():
    tasks_dir = os.environ.get("TASKS_DIR")
    if tasks_dir:
        data_dir = Path(tasks_dir) / "multi-invite-to-event-tomas-reyes-billing-5100069" / "data"
    else:
        data_dir = Path(__file__).resolve().parent.parent / "data"
    spec = importlib.util.spec_from_file_location("needles", data_dir / "needles.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_needles = _load_needles()

def _norm(s):
    return str(s or "").lower().strip()


def _matches(event, keywords):
    text = _norm(event.get("summary")) + " " + _norm(event.get("description"))
    return all(kw in text for kw in keywords)


def _local_hour(event):
    """Return the event's start hour in America/Los_Angeles local time.

    The oracle stores a naive-local dateTime at the requested hour H. A careful
    agent may instead store a tz-aware value (e.g. UTC), so the literal hour in
    the string can differ from H by the LA offset. Parse the timestamp; if it is
    tz-aware, convert to America/Los_Angeles before reading the hour; if naive,
    read the hour directly.
    """
    import datetime

    start = event.get("start", {})
    if isinstance(start, dict):
        dt = start.get("dateTime") or start.get("date") or ""
    else:
        dt = str(start)
    dt = str(dt)
    if "T" not in dt:
        return None

    iso = dt.replace("Z", "+00:00")
    try:
        parsed = datetime.datetime.fromisoformat(iso)
    except ValueError:
        # Fall back to a literal hour parse of the time component.
        try:
            return int(dt.split("T")[1].split(":")[0])
        except (IndexError, ValueError):
            return None

    if parsed.tzinfo is not None:
        try:
            from zoneinfo import ZoneInfo

            parsed = parsed.astimezone(ZoneInfo("America/Los_Angeles"))
        except Exception:
            # Without tz data, approximate LA as UTC-8 (standard time).
            parsed = (parsed.astimezone(datetime.timezone.utc)
                      - datetime.timedelta(hours=8))
    return parsed.hour


def _added_events(diff):
    added = []
    users = diff.get("users", diff)
    if isinstance(users, dict):
        for udata in users.values():
            if isinstance(udata, dict):
                added.extend(udata.get("events", {}).get("added", []))
    return added


def _state_events(state):
    events = []
    for udata in state.get("users", {}).values():
        if isinstance(udata, dict):
            events.extend(udata.get("events", []))
    return events


def evaluate(final_state, diff, action_log):
    metrics = {}
    kw = _needles.SUMMARY_KEYWORDS
    want_hour = _needles.START_HOUR
    decoy_kw = _needles.DECOY_KEYWORDS

    added = _added_events(diff)
    # Fall back to scanning full state if the diff carried no per-user events.
    candidates = added if added else _state_events(final_state)

    # Did the agent read mail and write to the calendar?
    read_mail = any(e.get("method") == "GET" for e in action_log)
    wrote_cal = any(
        e.get("method") in {"POST", "PUT", "PATCH"}
        and ("calendar" in _norm(e.get("path")) or "event" in _norm(e.get("path")))
        for e in action_log
    )
    metrics["read_mail"] = read_mail
    metrics["wrote_calendar"] = wrote_cal

    # Find the created meeting event.
    match = None
    for ev in candidates:
        if _matches(ev, kw):
            match = ev
            break
    metrics["event_created"] = match is not None

    title_ok = match is not None
    hour = _local_hour(match) if match else None
    # Tolerant start-hour check: accept the LOCAL hour == H. As a fallback for
    # tz-aware storage where conversion is unavailable, also accept the raw
    # UTC-shifted hours H, (H+7)%24, (H+8)%24 (America/Los_Angeles offsets).
    accepted_hours = {want_hour, (want_hour + 7) % 24, (want_hour + 8) % 24}
    hour_ok = title_ok and hour is not None and hour in accepted_hours
    metrics["title_ok"] = title_ok
    metrics["time_ok"] = hour_ok

    # Collateral: agent must NOT add the declined-meeting decoy.
    decoy_added = any(_matches(ev, decoy_kw) for ev in candidates)
    metrics["no_decoy_event"] = not decoy_added

    reward = 0.0
    if title_ok:
        reward += 0.6
    if hour_ok:
        reward += 0.4
    if decoy_added:
        reward = min(reward, 0.5)  # collateral cap

    metrics["api_calls"] = len(action_log)
    return {"reward": round(min(reward, 1.0), 2), "done": True, "metrics": metrics}


def _write_reward(result, output_path):
    """Write the benchflow-canonical reward.json (scalar reward + [0,1] metrics;
    richer diagnostics under details) plus a scalar reward.txt mirror."""
    import json as _json, math as _math, os as _os

    output_path = str(output_path)
    out_dir = _os.path.dirname(output_path) or "."
    _os.makedirs(out_dir, exist_ok=True)

    reward = result["reward"]
    raw_metrics = result.get("metrics", {}) or {}

    numeric_metrics = {}
    for key, value in raw_metrics.items():
        if isinstance(value, bool):
            numeric_metrics[str(key)] = 1 if value else 0
        elif (isinstance(value, (int, float)) and _math.isfinite(float(value))
              and 0.0 <= float(value) <= 1.0):
            numeric_metrics[str(key)] = value

    details = dict(raw_metrics)
    if "done" in result:
        details["done"] = result["done"]

    payload = {"reward": reward}
    if numeric_metrics:
        payload["metrics"] = numeric_metrics
    if details:
        payload["details"] = details

    with open(output_path, "w") as fh:
        _json.dump(payload, fh, indent=2)
    with open(_os.path.join(out_dir, "reward.txt"), "w") as fh:
        fh.write(str(reward))


def main():
    import argparse, json
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True)
    parser.add_argument("--diff", required=True)
    parser.add_argument("--action-log", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    final_state = json.loads(open(args.state).read())
    diff = json.loads(open(args.diff).read())
    ald = json.loads(open(args.action_log).read())
    log_entries = ald.get("entries", ald) if isinstance(ald, dict) else ald

    result = evaluate(final_state, diff, log_entries)
    _write_reward(result, args.output)


if __name__ == "__main__":
    main()
