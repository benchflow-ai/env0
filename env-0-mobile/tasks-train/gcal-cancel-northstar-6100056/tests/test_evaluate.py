#!/usr/bin/env python3
"""Offline unit tests: pre-solve == 0.0, post-solve == 1.0, trap penalized."""

import importlib.util
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _load_eval():
    spec = importlib.util.spec_from_file_location("evaluate_mod", _HERE / "evaluate.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _ev(summary, status="confirmed"):
    return {"id": "evt_" + summary, "summary": summary, "status": status}


def test_presolve_zero():
    ev = _load_eval()
    n = ev._needles
    events = [_ev(s) for s in n.CANCEL_SUMMARIES] + [_ev(s) for s in n.KEEP_SUMMARIES]
    state = {"users": {"user1": {"events": events}}}
    assert ev.evaluate(state, {"users": {}}, [])["reward"] == 0.0


def test_postsolve_full():
    ev = _load_eval()
    n = ev._needles
    events = [_ev(s) for s in n.KEEP_SUMMARIES]  # cancelled ones removed
    state = {"users": {"user1": {"events": events}}}
    diff = {"users": {"user1": {"events": {"added": [], "updated": [], "deleted": []}}}}
    log = [{"method": "DELETE", "path": "/calendar/v3/calendars/primary/events/x"}]
    assert ev.evaluate(state, diff, log)["reward"] == 1.0


def test_trap_penalized():
    ev = _load_eval()
    n = ev._needles
    events = [_ev(s) for s in n.KEEP_SUMMARIES[1:]]  # one keep wrongly removed
    state = {"users": {"user1": {"events": events}}}
    log = [{"method": "DELETE", "path": "/calendar/v3/calendars/primary/events/x"}]
    assert ev.evaluate(state, {"users": {}}, log)["reward"] < 1.0
