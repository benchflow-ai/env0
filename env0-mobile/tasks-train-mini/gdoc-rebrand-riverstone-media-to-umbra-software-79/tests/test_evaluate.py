#!/usr/bin/env python3
"""Offline unit tests: pre-solve reward == 0.0 and post-solve reward == 1.0."""

import importlib.util
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _load_eval():
    spec = importlib.util.spec_from_file_location("evaluate_mod", _HERE / "evaluate.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_presolve_zero():
    ev = _load_eval()
    state = {"users": {}}
    diff = {"updated": {}}
    assert ev.evaluate(state, diff, [])["reward"] == 0.0


def test_postsolve_full():
    ev = _load_eval()
    n = ev._needles
    new = n.NEW_BRAND
    docs = [
        {"id": did, "body": {"content": [
            {"paragraph": {"elements": [{"textRun": {"content": f"Now branded {new}.\n"}}]}}
        ]}}
        for did in n.NEEDLE_DOC_IDS
    ]
    state = {"users": {"user1": {"documents": docs}}}
    diff = {"updated": {"user1": {"documents": {"updated": [{"id": d} for d in n.NEEDLE_DOC_IDS]}}}}
    action_log = [
        {"method": "GET", "path": "/drive/v3/files?q=fullText%20contains"},
        {"method": "POST", "path": "/docs/v1/documents/x:batchUpdate"},
    ]
    result = ev.evaluate(state, diff, action_log)
    assert result["reward"] == 1.0, result


def test_collateral_penalized():
    ev = _load_eval()
    n = ev._needles
    new = n.NEW_BRAND
    docs = [
        {"id": did, "body": {"content": [
            {"paragraph": {"elements": [{"textRun": {"content": f"Now branded {new}.\n"}}]}}
        ]}}
        for did in n.NEEDLE_DOC_IDS
    ]
    state = {"users": {"user1": {"documents": docs}}}
    # touched an unrelated doc -> lose the no-collateral 0.10
    diff = {"updated": {"user1": {"documents": {"updated": (
        [{"id": d} for d in n.NEEDLE_DOC_IDS] + [{"id": "UNRELATED_DOC_ID"}]
    )}}}}
    action_log = [
        {"method": "GET", "path": "/drive/v3/files?q=fullText"},
        {"method": "POST", "path": "/docs/x:batchUpdate"},
    ]
    assert ev.evaluate(state, diff, action_log)["reward"] < 1.0
