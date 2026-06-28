#!/usr/bin/env python3
"""Evaluator for gcal-cancel-falcon-5100128 (env-0 tasks-lite)."""

import importlib.util
import os
from pathlib import Path


def _load_needles():
    tasks_dir = os.environ.get("TASKS_DIR")
    if tasks_dir:
        data_dir = Path(tasks_dir) / "gcal-cancel-falcon-5100128" / "data"
    else:
        data_dir = Path(__file__).resolve().parent.parent / "data"
    spec = importlib.util.spec_from_file_location("needles", data_dir / "needles.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_needles = _load_needles()

def _norm(t):
    return " ".join((t or "").lower().split())


def _status(ev):
    return _norm(ev.get("status", "confirmed"))


def _all_events(state):
    out = []
    users = state.get("users", state)
    for ud in users.values():
        if isinstance(ud, dict):
            out.extend(ud.get("events", []))
    return out


def _active_summaries(events):
    return [_norm(e.get("summary", "")) for e in events if _status(e) != "cancelled"]


def evaluate(final_state, diff, action_log):
    metrics = {}
    cancel = [_norm(s) for s in _needles.CANCEL_SUMMARIES]
    keep = [_norm(s) for s in _needles.KEEP_SUMMARIES]
    n_cancel, n_keep = len(cancel), len(keep)

    active = _active_summaries(_all_events(final_state))
    agent_acted = any(
        e.get("method") in {"POST", "PATCH", "PUT", "DELETE"} for e in action_log
    )

    removed = 0
    for s in cancel:
        gone = s not in active
        metrics[f"removed::{s}"] = gone
        if gone:
            removed += 1
    metrics["cancelled_removed"] = removed
    metrics["cancelled_total"] = n_cancel

    kept = 0
    for s in keep:
        ok = active.count(s) >= 1
        metrics[f"kept::{s}"] = ok
        if ok:
            kept += 1
    trap_hit = n_keep - kept
    metrics["keep_intact"] = kept
    metrics["keep_total"] = n_keep
    metrics["traps_hit"] = trap_hit

    removed_frac = removed / n_cancel if n_cancel else 0.0
    reward = 0.80 * removed_frac
    if kept == n_keep and agent_acted:
        reward += 0.20
    reward -= 0.50 * trap_hit
    reward = max(-1.0, min(1.0, reward))

    metrics["api_calls"] = len(action_log)
    return {"reward": round(reward, 4), "done": True, "metrics": metrics}


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
