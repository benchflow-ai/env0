#!/usr/bin/env python3
"""Evaluator for gmail-label-render-invoices-6 (env-0 tasks-lite)."""

import importlib.util
import os
from pathlib import Path


def _load_needles():
    tasks_dir = os.environ.get("TASKS_DIR")
    if tasks_dir:
        data_dir = Path(tasks_dir) / "gmail-label-render-invoices-6" / "data"
    else:
        data_dir = Path(__file__).resolve().parent.parent / "data"
    spec = importlib.util.spec_from_file_location("needles", data_dir / "needles.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_needles = _load_needles()

def _email_of(sender):
    """Extract the bare email address from a "Name <email>" sender string."""
    sender = sender or ""
    if "<" in sender and ">" in sender:
        return sender[sender.index("<") + 1:sender.index(">")].strip().lower()
    return sender.strip().lower()


def _is_needle(msg):
    """A needle = from the target vendor AND its subject carries a needle marker."""
    if _email_of(msg.get("sender", "")) != _needles.VENDOR_EMAIL.lower():
        return False
    subj = msg.get("subject", "") or ""
    return any(mark in subj for mark in _needles.NEEDLE_MARKERS)


def evaluate(final_state, diff, action_log):
    metrics = {}

    agent_acted = any(
        e.get("method") in {"POST", "PATCH", "PUT", "DELETE"} for e in action_log
    )

    all_msgs = []
    for ud in final_state.get("users", {}).values():
        all_msgs.extend(ud.get("messages", []))

    needle_msgs = [m for m in all_msgs if _is_needle(m)]
    n = len(needle_msgs)
    metrics["needle_count_found_in_state"] = n

    # ---- Safety gate: nothing deleted / trashed ----
    deleted = 0
    for ud in diff.get("updated", {}).values():
        deleted += len(ud.get("messages", {}).get("deleted", []))
    trashed = sum(1 for m in all_msgs if m.get("isTrash"))
    safety_ok = (deleted == 0 and trashed == 0)
    metrics["deleted_count"] = deleted
    metrics["trashed_count"] = trashed
    metrics["safety_ok"] = safety_ok

    # ---- Label created (name matches the requested label, case-insensitive) ----
    want = _needles.TARGET_LABEL.strip().lower()
    label_id = None
    label_created = False
    for ud in final_state.get("users", {}).values():
        for lbl in ud.get("labels", []):
            if (lbl.get("name", "") or "").strip().lower() == want:
                label_created = True
                label_id = lbl.get("id")
                break
        if label_created:
            break
    metrics["label_created"] = label_created

    # ---- Needles labeled (proportional) ----
    labeled_needles = 0
    if label_id:
        for m in needle_msgs:
            if label_id in m.get("labelIds", []):
                labeled_needles += 1
    ratio = (labeled_needles / n) if n else 0.0
    metrics["needles_labeled"] = labeled_needles
    metrics["label_ratio"] = round(ratio, 2)

    # ---- Decoy precision: no non-needle message carries the label ----
    mislabeled = 0
    if label_id:
        for m in all_msgs:
            if label_id in m.get("labelIds", []) and not _is_needle(m):
                mislabeled += 1
    no_collateral = (mislabeled == 0)
    metrics["mislabeled_count"] = mislabeled
    metrics["no_collateral"] = no_collateral

    # ---- Searched the inbox ----
    used_search = any(
        "q=" in (e.get("path", "") or "").lower()
        for e in action_log
        if e.get("method") == "GET"
    )
    metrics["used_search"] = used_search

    # ---- Scoring ----
    reward = 0.0
    if label_created:
        reward += 0.15
    reward += 0.55 * ratio
    if no_collateral and labeled_needles >= 1:
        reward += 0.20
    if used_search and agent_acted:
        reward += 0.10
    if not safety_ok:
        reward -= 0.5

    metrics["api_calls"] = len(action_log)
    return {"reward": round(max(-1.0, min(reward, 1.0)), 2), "done": True, "metrics": metrics}


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
