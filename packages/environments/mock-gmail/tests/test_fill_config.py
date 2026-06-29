"""Tests that task_seed reads GMAIL_FILL_CONFIG from needles modules."""

from __future__ import annotations

import types

from unittest import mock

from mock_gmail.seed.task_seed import get_task_data_summary


def _make_needles_module(**attrs) -> types.ModuleType:
    mod = types.ModuleType("fake_needles")
    for k, v in attrs.items():
        setattr(mod, k, v)
    return mod


def _patch_summary(mod):
    """Patch both the module loader and the needles-path existence check."""
    return mock.patch.multiple(
        "mock_gmail.seed.task_seed",
        _load_needles_module=mock.Mock(return_value=mod),
        _TASKS_DIR=mock.MagicMock(
            __truediv__=lambda self, *a: mock.MagicMock(
                __truediv__=lambda self, *a: mock.MagicMock(exists=lambda: True)
            ),
        ),
    )


class TestGmailFillConfig:
    def test_reads_gmail_fill_config(self, tmp_path):
        mod = _make_needles_module(
            GMAIL_FILL_CONFIG={"target_count": 200},
            NEEDLES=[{"sender_name": "A", "sender_email": "a@test", "subject": "s", "labels": ["INBOX"]}],
        )
        # Create fake needles path so the existence check passes
        task_dir = tmp_path / "fake-task" / "data"
        task_dir.mkdir(parents=True)
        (task_dir / "needles.py").write_text("")
        with mock.patch("mock_gmail.seed.task_seed._TASKS_DIR", tmp_path), \
             mock.patch("mock_gmail.seed.task_seed._load_needles_module", return_value=mod):
            summary = get_task_data_summary("fake-task")
        assert summary["fill_config"] == {"target_count": 200}

    def test_empty_without_gmail_fill_config(self, tmp_path):
        mod = _make_needles_module(NEEDLES=[], NEEDLE_THREADS=[])
        task_dir = tmp_path / "fake-task" / "data"
        task_dir.mkdir(parents=True)
        (task_dir / "needles.py").write_text("")
        with mock.patch("mock_gmail.seed.task_seed._TASKS_DIR", tmp_path), \
             mock.patch("mock_gmail.seed.task_seed._load_needles_module", return_value=mod):
            summary = get_task_data_summary("fake-task")
        assert summary["fill_config"] == {}

    def test_ignores_plain_fill_config(self, tmp_path):
        mod = _make_needles_module(
            FILL_CONFIG={"target_count": 999},
            NEEDLES=[],
        )
        task_dir = tmp_path / "fake-task" / "data"
        task_dir.mkdir(parents=True)
        (task_dir / "needles.py").write_text("")
        with mock.patch("mock_gmail.seed.task_seed._TASKS_DIR", tmp_path), \
             mock.patch("mock_gmail.seed.task_seed._load_needles_module", return_value=mod):
            summary = get_task_data_summary("fake-task")
        assert summary["fill_config"] == {}
