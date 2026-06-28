#!/usr/bin/env python3
"""Offline unit tests: pre-solve == 0.0, post-solve == 1.0, penalty < 1.0."""

import importlib.util
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _load_eval():
    spec = importlib.util.spec_from_file_location("evaluate_mod", _HERE / "evaluate.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _seeded_state(n):
    """The pre-solve world: every seeded consent present at full scope."""
    rows = []
    for app in [n.REVOKE_TARGET] + list(n.LEGIT_APPS):
        rows.append({
            "user_id": n.OWNER_USER_ID,
            "client_id": app["client_id"],
            "granted_scopes": " ".join(app["scopes"]),
            "revoked_at": None,
        })
    return {"consent_records": rows}


def test_presolve_zero():
    ev = _load_eval()
    n = ev._needles
    result = ev.evaluate(_seeded_state(n), {"updated": {}}, [])
    assert result["reward"] == 0.0, result


def test_postsolve_full():
    ev = _load_eval()
    n = ev._needles
    state = _seeded_state(n)
    # Solve: mark the over-permissioned app's consent revoked.
    for row in state["consent_records"]:
        if row["client_id"] == n.REVOKE_TARGET["client_id"]:
            row["revoked_at"] = "2026-01-01T00:00:00Z"
    result = ev.evaluate(state, {"updated": {}}, [])
    assert result["reward"] == 1.0, result
    assert result["done"] is True, result


def test_collateral_penalized():
    ev = _load_eval()
    n = ev._needles
    state = _seeded_state(n)
    # Revoked the target (good) BUT also revoked a least-privilege app (bad).
    for row in state["consent_records"]:
        if row["client_id"] == n.REVOKE_TARGET["client_id"]:
            row["revoked_at"] = "2026-01-01T00:00:00Z"
        if row["client_id"] == n.LEGIT_APPS[0]["client_id"]:
            row["revoked_at"] = "2026-01-01T00:00:00Z"
    result = ev.evaluate(state, {"updated": {}}, [])
    assert result["reward"] < 1.0, result
    assert result["reward"] < 0.0, result
