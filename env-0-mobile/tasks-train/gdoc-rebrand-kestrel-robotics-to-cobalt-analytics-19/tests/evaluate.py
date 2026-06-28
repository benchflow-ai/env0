#!/usr/bin/env python3
"""Evaluator for gdoc-rebrand-kestrel-robotics-to-cobalt-analytics-19 (env-0 tasks-lite)."""

import importlib.util
import os
from pathlib import Path


def _load_needles():
    tasks_dir = os.environ.get("TASKS_DIR")
    if tasks_dir:
        data_dir = Path(tasks_dir) / "gdoc-rebrand-kestrel-robotics-to-cobalt-analytics-19" / "data"
    else:
        data_dir = Path(__file__).resolve().parent.parent / "data"
    spec = importlib.util.spec_from_file_location("needles", data_dir / "needles.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_needles = _load_needles()

def _extract_text(body):
    parts = []
    for element in body.get("content", []):
        para = element.get("paragraph")
        if not para:
            continue
        for pe in para.get("elements", []):
            tr = pe.get("textRun")
            if tr:
                parts.append(tr.get("content", ""))
    return "".join(parts)


def evaluate(final_state, diff, action_log):
    metrics = {}
    old = _needles.OLD_BRAND
    new = _needles.NEW_BRAND
    needle_ids = _needles.NEEDLE_DOC_IDS
    n = len(needle_ids)

    agent_acted = any(
        e.get("method") in {"POST", "PATCH", "PUT", "DELETE"} for e in action_log
    )

    all_docs = {}
    for ud in final_state.get("users", {}).values():
        for doc in ud.get("documents", []):
            all_docs[doc["id"]] = doc

    replaced = 0
    for did in needle_ids:
        doc = all_docs.get(did)
        ok = False
        if doc:
            text = _extract_text(doc.get("body", {}))
            ok = (old not in text) and (new in text)
        metrics[f"replaced_{did}"] = ok
        if ok:
            replaced += 1
    metrics["needle_docs_replaced"] = replaced
    metrics["needle_docs_total"] = n

    non_needle = []
    for ud in diff.get("updated", {}).values():
        for doc in ud.get("documents", {}).get("updated", []):
            if doc.get("id") not in needle_ids:
                non_needle.append(doc.get("id"))
    no_collateral = len(non_needle) == 0
    metrics["no_collateral_damage"] = no_collateral
    metrics["non_needle_modified_count"] = len(non_needle)

    used_search = any(
        "q=" in e.get("path", "").lower()
        for e in action_log
        if e.get("method") == "GET"
    )
    metrics["used_search"] = used_search

    reward = 0.80 * (replaced / n) if n else 0.0
    if no_collateral and agent_acted:
        reward += 0.10
    if used_search and agent_acted:
        reward += 0.10

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
