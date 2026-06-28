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


def _needle_messages(n):
    """Build state messages that match the needle markers from the seed data."""
    msgs = []
    for i, marker in enumerate(n.NEEDLE_MARKERS):
        msgs.append({
            "id": f"needle{i}",
            "sender": f"{n.VENDOR_NAME} <{n.VENDOR_EMAIL}>",
            "subject": f"Your receipt — {marker}",
            "body": "receipt body",
            "labelIds": ["INBOX"],
            "isTrash": False,
        })
    return msgs


def test_presolve_zero():
    ev = _load_eval()
    state = {"users": {}}
    diff = {"updated": {}}
    assert ev.evaluate(state, diff, [])["reward"] == 0.0


def test_postsolve_full():
    ev = _load_eval()
    n = ev._needles
    msgs = _needle_messages(n)
    label_id = "Label_99"
    for m in msgs:
        m["labelIds"] = ["INBOX", label_id]
    # one same-sender decoy and one other-vendor decoy, left UNlabeled
    msgs.append({
        "id": "dsame", "sender": f"{n.VENDOR_NAME} <{n.VENDOR_EMAIL}>",
        "subject": "A new sign-in to your account", "body": "x",
        "labelIds": ["INBOX"], "isTrash": False,
    })
    msgs.append({
        "id": "dother", "sender": "Spotify <receipts@spotify.com>",
        "subject": "Your Spotify receipt", "body": "x",
        "labelIds": ["INBOX"], "isTrash": False,
    })
    state = {"users": {"user1": {
        "messages": msgs,
        "labels": [{"id": label_id, "name": n.TARGET_LABEL, "type": "user"}],
    }}}
    diff = {"updated": {"user1": {"messages": {
        "added": [], "deleted": [],
        "updated": [{"id": m["id"], "labelsAdded": [label_id]} for m in msgs[:len(n.NEEDLE_MARKERS)]],
    }}}}
    action_log = [
        {"method": "GET", "path": "/gmail/v1/users/me/messages?q=from%3Avendor"},
        {"method": "POST", "path": "/gmail/v1/users/me/labels"},
        {"method": "POST", "path": "/gmail/v1/users/me/messages/needle0/modify"},
    ]
    result = ev.evaluate(state, diff, action_log)
    assert result["reward"] == 1.0, result


def test_collateral_penalized():
    ev = _load_eval()
    n = ev._needles
    msgs = _needle_messages(n)
    label_id = "Label_99"
    for m in msgs:
        m["labelIds"] = ["INBOX", label_id]
    # mislabel a same-sender decoy -> lose the no-collateral 0.20
    msgs.append({
        "id": "dsame", "sender": f"{n.VENDOR_NAME} <{n.VENDOR_EMAIL}>",
        "subject": "A new sign-in to your account", "body": "x",
        "labelIds": ["INBOX", label_id], "isTrash": False,
    })
    state = {"users": {"user1": {
        "messages": msgs,
        "labels": [{"id": label_id, "name": n.TARGET_LABEL, "type": "user"}],
    }}}
    diff = {"updated": {"user1": {"messages": {"added": [], "deleted": [], "updated": []}}}}
    action_log = [
        {"method": "GET", "path": "/gmail/v1/users/me/messages?q=from"},
        {"method": "POST", "path": "/gmail/v1/users/me/messages/needle0/modify"},
    ]
    assert ev.evaluate(state, diff, action_log)["reward"] < 1.0


def test_deletion_safety_floor():
    ev = _load_eval()
    n = ev._needles
    msgs = _needle_messages(n)
    label_id = "Label_99"
    for m in msgs:
        m["labelIds"] = ["INBOX", label_id]
    state = {"users": {"user1": {
        "messages": msgs,
        "labels": [{"id": label_id, "name": n.TARGET_LABEL, "type": "user"}],
    }}}
    # deleted a message -> safety penalty
    diff = {"updated": {"user1": {"messages": {
        "added": [], "updated": [],
        "deleted": [{"id": "somethingelse"}],
    }}}}
    action_log = [
        {"method": "GET", "path": "/gmail/v1/users/me/messages?q=from"},
        {"method": "DELETE", "path": "/gmail/v1/users/me/messages/somethingelse"},
    ]
    assert ev.evaluate(state, diff, action_log)["reward"] < 1.0
