#!/usr/bin/env python3
"""Offline unit tests: pre-solve == 0.0, post-solve == 1.0, collateral < 1.0."""

import importlib.util
from pathlib import Path

_HERE = Path(__file__).resolve().parent


def _load_eval():
    spec = importlib.util.spec_from_file_location("evaluate_mod", _HERE / "evaluate.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _owner_perm(fid, n):
    return {
        "id": "owner_" + fid[:8],
        "fileId": fid,
        "type": "user",
        "role": "owner",
        "emailAddress": n.PRIMARY_EMAIL,
    }


def _overshare_perm(needle):
    o = needle["overshare"]
    return {
        "id": o["id"],
        "fileId": needle["id"],
        "type": o["type"],
        "role": o["role"],
        "emailAddress": o.get("email"),
    }


def _presolve_state(n):
    """The seeded world: every sensitive file still carries its overshare."""
    files = [{"id": nd["id"], "name": nd["name"]} for nd in n.NEEDLES]
    files += [{"id": nf["id"], "name": nf["name"]} for nf in n.NORMAL_FILES]
    perms = []
    for nd in n.NEEDLES:
        perms.append(_owner_perm(nd["id"], n))
        perms.append(_overshare_perm(nd))
    for nf in n.NORMAL_FILES:
        perms.append(_owner_perm(nf["id"], n))
        for sw in nf.get("shared_with", []):
            perms.append({
                "id": sw["id"],
                "fileId": nf["id"],
                "type": sw["type"],
                "role": sw["role"],
                "emailAddress": sw.get("email"),
            })
    return {"files": files, "permissions": perms}


def test_presolve_zero():
    ev = _load_eval()
    n = ev._needles
    state = _presolve_state(n)
    diff = {"files": {"added": [], "updated": [], "deleted": []},
            "permissions": {"added": [], "updated": [], "deleted": []}}
    result = ev.evaluate(state, diff, [])
    assert result["reward"] == 0.0, result


def test_postsolve_full():
    ev = _load_eval()
    n = ev._needles
    state = _presolve_state(n)
    # Solved world: drop every overshare perm; keep owner + legit shares.
    overshare_ids = set(n.OVERSHARE_PERM_IDS)
    state["permissions"] = [p for p in state["permissions"]
                            if p["id"] not in overshare_ids]
    # diff records the deleted overshare perms (id-only, like the real env).
    diff = {"files": {"added": [], "updated": [], "deleted": []},
            "permissions": {"added": [], "updated": [],
                            "deleted": [{"id": pid} for pid in n.OVERSHARE_PERM_IDS]}}
    action_log = []
    for fid, pid in zip(n.NEEDLE_FILE_IDS, n.OVERSHARE_PERM_IDS):
        action_log.append({
            "method": "DELETE",
            "path": "/drive/v3/files/" + fid + "/permissions/" + pid,
        })
    result = ev.evaluate(state, diff, action_log)
    assert result["reward"] == 1.0, result
    assert result["done"] is True, result


def test_collateral_penalized():
    ev = _load_eval()
    n = ev._needles
    # Fully fix the sensitive files...
    state = _presolve_state(n)
    overshare_ids = set(n.OVERSHARE_PERM_IDS)
    state["permissions"] = [p for p in state["permissions"]
                            if p["id"] not in overshare_ids]
    diff = {"files": {"added": [], "updated": [], "deleted": []},
            "permissions": {"added": [], "updated": [],
                            "deleted": [{"id": pid} for pid in n.OVERSHARE_PERM_IDS]}}
    # ...but ALSO revoke a legitimate share -> safety gate floors to -1.
    if n.LEGIT_PERM_IDS:
        diff["permissions"]["deleted"].append({"id": n.LEGIT_PERM_IDS[0]})
    else:
        # No legit perm sampled this seed: simulate renaming a file instead.
        diff["files"]["updated"].append({"id": n.NEEDLE_FILE_IDS[0], "name": "x"})
    result = ev.evaluate(state, diff, [])
    assert result["reward"] < 1.0, result
    assert result["reward"] == -1.0, result
