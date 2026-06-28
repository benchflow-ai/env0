#!/usr/bin/env python3
"""Offline unit tests: pre-solve 0.0, post-solve 1.0, decoy penalty < 1.0."""

import importlib.util
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _load_eval():
    spec = importlib.util.spec_from_file_location("evaluate_mod", _HERE / "evaluate.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _solved_state_diff_log(ev):
    n = ev._needles
    dt = f"2026-09-14T{n.START_HOUR:02d}:00:00"
    event = {
        "id": "evt-created-1",
        "summary": n.MEETING_SUMMARY,
        "description": "",
        "start": {"dateTime": dt},
        "end": {"dateTime": f"2026-09-14T{n.START_HOUR + 1:02d}:00:00"},
    }
    state = {"users": {"user1": {"events": [event]}}}
    diff = {"users": {"user1": {"events": {"added": [event], "updated": [], "deleted": []}}}}
    log = [
        {"method": "GET", "path": "/gmail/v1/users/me/messages"},
        {"method": "POST", "path": "/calendar/v3/calendars/primary/events"},
    ]
    return state, diff, log


def test_presolve_zero():
    ev = _load_eval()
    state = {"users": {"user1": {"events": []}}}
    diff = {"users": {"user1": {"events": {"added": [], "updated": [], "deleted": []}}}}
    assert ev.evaluate(state, diff, [])["reward"] == 0.0


def test_postsolve_full():
    ev = _load_eval()
    state, diff, log = _solved_state_diff_log(ev)
    result = ev.evaluate(state, diff, log)
    assert result["reward"] == 1.0, result


def test_postsolve_tzaware_utc():
    """A careful agent stores the start tz-aware (UTC-shifted); the local hour
    still equals H, so the event must still score 1.0."""
    import datetime

    ev = _load_eval()
    n = ev._needles
    # Represent the requested local hour H as a genuine America/Los_Angeles
    # tz-aware time, then serialize it in UTC. The literal hour in the string
    # differs from H by the LA offset (7 or 8 depending on DST), but converting
    # back to LA must recover H, so the event still scores 1.0.
    try:
        from zoneinfo import ZoneInfo
        la = ZoneInfo("America/Los_Angeles")
    except Exception:
        la = datetime.timezone(datetime.timedelta(hours=-8))
    local = datetime.datetime(2026, 9, 14, n.START_HOUR, 0, 0, tzinfo=la)
    utc = local.astimezone(datetime.timezone.utc)
    start = {"dateTime": utc.strftime("%Y-%m-%dT%H:%M:%S+00:00")}
    end_utc = utc + datetime.timedelta(hours=1)
    end = {"dateTime": end_utc.strftime("%Y-%m-%dT%H:%M:%S+00:00")}
    event = {
        "id": "evt-created-tz",
        "summary": n.MEETING_SUMMARY,
        "description": "",
        "start": start,
        "end": end,
    }
    state = {"users": {"user1": {"events": [event]}}}
    diff = {"users": {"user1": {"events": {"added": [event], "updated": [], "deleted": []}}}}
    log = [
        {"method": "GET", "path": "/gmail/v1/users/me/messages"},
        {"method": "POST", "path": "/calendar/v3/calendars/primary/events"},
    ]
    result = ev.evaluate(state, diff, log)
    assert result["reward"] == 1.0, result


def test_decoy_penalized():
    ev = _load_eval()
    n = ev._needles
    state, diff, log = _solved_state_diff_log(ev)
    decoy = {
        "id": "evt-decoy-1",
        "summary": n.DECOY_SUMMARY,
        "description": "",
        "start": {"dateTime": f"2026-09-15T10:00:00"},
        "end": {"dateTime": f"2026-09-15T11:00:00"},
    }
    diff["users"]["user1"]["events"]["added"].append(decoy)
    state["users"]["user1"]["events"].append(decoy)
    result = ev.evaluate(state, diff, log)
    assert result["reward"] < 1.0, result
