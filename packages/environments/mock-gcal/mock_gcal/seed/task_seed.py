"""Per-task seed scenario for Calendar.

Task-specific seed definitions live in:
    tasks/<task-name>/data/needles.py

Supported module-level fields in needles.py:
    NEEDLE_EVENTS / NEEDLES      list[dict] or dict[str, dict]
    RECURRING_NEEDLES            list[dict] or dict[str, dict]
    GCAL_FILL_CONFIG             {
        "base_scenario": str | None,
        "seed_packs": list[str],
        "target_count": int | "fixed_only",
        "distribution": dict[str, float],
        "include_needles": bool,
    }
"""

from __future__ import annotations

import importlib.util
import os
import sys
from pathlib import Path
from typing import Mapping

from sqlalchemy.orm import Session

from mock_gcal.models import Calendar, User
from mock_gcal.seed.content import (
    DEFAULT_DISTRIBUTION,
    DEFAULT_TARGET_EVENTS,
    SCENARIO_DEFINITIONS,
)
from mock_gcal.seed.long_context import seed_distribution_scenario
from mock_gcal.seed.task_packs import clone_pack_events, get_seed_pack

def _candidate_task_roots() -> list[Path]:
    roots: list[Path] = []
    for env_name in ("TASKS_DIR", "ENV0_TASKS_DIR"):
        env_value = os.environ.get(env_name)
        if env_value:
            roots.append(Path(env_value))

    for parent in Path(__file__).resolve().parents:
        roots.append(parent / "example_tasks")
        roots.append(parent / "tasks")

    unique: list[Path] = []
    seen: set[Path] = set()
    for root in roots:
        resolved = root.expanduser()
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(resolved)
    return unique


def _task_data_dir(task_dir_name: str) -> Path:
    for root in _candidate_task_roots():
        task_data = root / task_dir_name / "data"
        if (task_data / "needles.py").exists():
            return task_data
    return _candidate_task_roots()[0] / task_dir_name / "data"


def _load_needles_module(
    task_dir_name: str | None = None,
    task_data_path: str | Path | None = None,
):
    if task_data_path:
        needles_path = Path(task_data_path) / "needles.py"
    else:
        if not task_dir_name:
            raise ValueError("task_dir_name or task_data_path required")
        needles_path = _task_data_dir(task_dir_name) / "needles.py"
    if not needles_path.exists():
        raise FileNotFoundError(f"Task needles not found: {needles_path}")

    module_suffix = (
        task_dir_name.replace("-", "_")
        if task_dir_name
        else f"path_{abs(hash(str(needles_path.resolve())))}"
    )
    module_name = f"gcal_task_needles_{module_suffix}"
    if module_name in sys.modules:
        return sys.modules[module_name]

    spec = importlib.util.spec_from_file_location(module_name, needles_path)
    if not spec or not spec.loader:
        raise RuntimeError(f"Failed to load task needles: {needles_path}")

    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


def _as_event_list(raw) -> list[dict]:
    if raw is None:
        return []
    if isinstance(raw, dict):
        ordered_keys = sorted(raw.keys(), key=lambda key: str(key))
        values = [raw[key] for key in ordered_keys]
    elif isinstance(raw, list):
        values = raw
    else:
        return []

    items: list[dict] = []
    for item in values:
        if isinstance(item, dict):
            items.append(dict(item))
    return items


def _read_task_config(
    task_dir_name: str | None = None,
    task_data_path: str | Path | None = None,
) -> tuple[list[dict], list[dict], dict]:
    module = _load_needles_module(task_dir_name=task_dir_name, task_data_path=task_data_path)
    needle_events = _as_event_list(
        getattr(module, "NEEDLE_EVENTS", getattr(module, "NEEDLES", None))
    )
    recurring_needles = _as_event_list(getattr(module, "RECURRING_NEEDLES", None))
    fill_config = getattr(module, "GCAL_FILL_CONFIG", {}) or {}

    return needle_events, recurring_needles, fill_config


def _normalize_pack_names(raw_names: object) -> list[str]:
    if raw_names is None:
        return []
    if isinstance(raw_names, str):
        values = [raw_names]
    elif isinstance(raw_names, list):
        values = raw_names
    else:
        return []

    names: list[str] = []
    seen: set[str] = set()
    for value in values:
        name = str(value).strip()
        if not name or name in seen:
            continue
        names.append(name)
        seen.add(name)
    return names


def _resolve_distribution(raw_distribution: object, *, base_config: dict | None) -> Mapping[str, float]:
    if isinstance(raw_distribution, dict):
        return raw_distribution
    if base_config is not None:
        return base_config["distribution"]
    return DEFAULT_DISTRIBUTION


def _resolve_target_count(raw_target_count: object, *, base_config: dict | None) -> int:
    if isinstance(raw_target_count, str):
        if raw_target_count.strip().lower() == "fixed_only":
            return 0
        return int(raw_target_count)
    if raw_target_count is not None:
        return int(raw_target_count)
    if base_config is not None:
        return int(base_config["target_events"])
    return DEFAULT_TARGET_EVENTS


def _resolve_base_config(fill_config: dict) -> tuple[str | None, dict | None]:
    base_scenario = str(fill_config.get("base_scenario") or "").strip()
    if not base_scenario:
        return None, None
    if base_scenario not in SCENARIO_DEFINITIONS:
        available = ", ".join(sorted(SCENARIO_DEFINITIONS))
        raise ValueError(
            f"Unknown gcal base scenario {base_scenario!r}. Available: {available}"
        )
    return base_scenario, SCENARIO_DEFINITIONS[base_scenario]


def _resolve_seed_inputs(
    task_dir_name: str | None = None,
    task_data_path: str | Path | None = None,
) -> tuple[list[dict], list[dict], dict, list[str], str | None]:
    needle_events, recurring_needles, fill_config = _read_task_config(
        task_dir_name=task_dir_name,
        task_data_path=task_data_path,
    )
    base_scenario, base_config = _resolve_base_config(fill_config)
    seed_packs = _normalize_pack_names(fill_config.get("seed_packs"))

    resolved_needle_events: list[dict] = []
    resolved_recurring_needles: list[dict] = []

    if base_config is not None:
        if fill_config.get("include_base_needles", True):
            resolved_needle_events.extend(_as_event_list(base_config["needle_events"]))
        if fill_config.get("include_base_recurring", True):
            resolved_recurring_needles.extend(_as_event_list(base_config["recurring_needles"]))

    for pack_name in seed_packs:
        pack = get_seed_pack(pack_name)
        pack_needles, pack_recurring = clone_pack_events(pack)
        resolved_needle_events.extend(pack_needles)
        resolved_recurring_needles.extend(pack_recurring)

    resolved_needle_events.extend(needle_events)
    resolved_recurring_needles.extend(recurring_needles)

    distribution = _resolve_distribution(fill_config.get("distribution"), base_config=base_config)
    target_count = _resolve_target_count(fill_config.get("target_count"), base_config=base_config)

    resolved_fill_config = dict(fill_config)
    resolved_fill_config.setdefault("seed_packs", seed_packs)
    if base_scenario is not None:
        resolved_fill_config.setdefault("base_scenario", base_scenario)
    resolved_fill_config["target_count"] = target_count
    resolved_fill_config["distribution"] = dict(distribution)

    return (
        resolved_needle_events,
        resolved_recurring_needles,
        resolved_fill_config,
        seed_packs,
        base_scenario,
    )


def get_task_data_summary(task_dir_name: str) -> dict:
    """Return a compact summary used by admin/debug tools."""
    needles_path = _task_data_dir(task_dir_name) / "needles.py"
    if not needles_path.exists():
        return {"has_per_task_data": False}

    needle_events, recurring_needles, fill_config, seed_packs, base_scenario = _resolve_seed_inputs(task_dir_name)
    return {
        "has_per_task_data": True,
        "base_scenario": base_scenario,
        "seed_packs": seed_packs,
        "needle_event_count": len(needle_events),
        "recurring_needle_count": len(recurring_needles),
        "fill_config": fill_config,
    }


def seed_task_scenario(
    db: Session,
    user: User,
    calendars_by_key: Mapping[str, Calendar],
    rng,
    task_dir_name: str | None = None,
    task_data_path: str | Path | None = None,
) -> int:
    """Seed a task-specific scenario: task needles + shared distribution fill."""
    needle_events, recurring_needles, fill_config, _seed_packs, _base_scenario = _resolve_seed_inputs(
        task_dir_name=task_dir_name,
        task_data_path=task_data_path,
    )

    target_count = int(fill_config["target_count"])
    distribution = fill_config["distribution"]
    include_needles = bool(fill_config.get("include_needles", True))

    return seed_distribution_scenario(
        db,
        user,
        calendars_by_key,
        rng,
        target_events=target_count,
        distribution=distribution,
        needle_events=needle_events,
        recurring_needles=recurring_needles,
        include_needles=include_needles,
    )
