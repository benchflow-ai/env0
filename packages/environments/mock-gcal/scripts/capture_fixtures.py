#!/usr/bin/env python3
"""Capture real Google Calendar API responses as golden fixtures.

Usage:
    python scripts/capture_fixtures.py
    python scripts/capture_fixtures.py --account fixture-user@example.com --diff

This script uses the `gws` CLI as the source of truth for live Calendar API
calls. Before running it, authenticate with Calendar scopes:

    gws auth login --account fixture-user@example.com --services calendar
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from uuid import uuid4

ROOT = Path(__file__).resolve().parent.parent
FIXTURES_DIR = ROOT / "tests" / "fixtures" / "real_gcal"
DEFAULT_ACCOUNT = os.environ.get("GOOGLE_WORKSPACE_CLI_ACCOUNT", "fixture-user@example.com")
API_BASE = "https://www.googleapis.com/calendar/v3"


def _parse_json(text: str) -> dict | list | None:
    text = text.strip()
    if not text:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        try:
            return json.loads(text[start : end + 1])
        except json.JSONDecodeError:
            return None
    return None


def _run_gws(
    *parts: str,
    account: str,
    params: dict | None = None,
    body: dict | None = None,
    allow_error: bool = False,
) -> dict | list:
    cmd = ["gws", "calendar", *parts]
    if params:
        cmd.extend(["--params", json.dumps(params, separators=(",", ":"))])
    if body is not None:
        cmd.extend(["--json", json.dumps(body, separators=(",", ":"))])

    env = os.environ.copy()
    env["GOOGLE_WORKSPACE_CLI_ACCOUNT"] = account

    result = subprocess.run(cmd, capture_output=True, text=True, env=env)
    payload = _parse_json(result.stdout) or _parse_json(result.stderr)
    if payload is None and result.returncode == 0:
        payload = {}

    if result.returncode != 0 and not allow_error:
        message = ""
        if isinstance(payload, dict):
            message = payload.get("error", {}).get("message", "")
        if not message:
            message = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(message)

    if payload is None:
        payload = {}

    return payload


class Saver:
    def __init__(self, fixtures_dir: Path, diff_mode: bool):
        self.fixtures_dir = fixtures_dir
        self.diff_mode = diff_mode
        self.changed = 0
        self.unchanged = 0
        self.created = 0

    def save(self, name: str, data: dict | list) -> None:
        self.fixtures_dir.mkdir(parents=True, exist_ok=True)
        payload = data
        if isinstance(payload, dict):
            payload = {**payload, "_captured_at": datetime.now(timezone.utc).isoformat()}
        text = json.dumps(payload, indent=2, sort_keys=False) + "\n"
        path = self.fixtures_dir / f"{name}.json"
        previous = path.read_text() if path.exists() else None
        path.write_text(text)

        if previous is None:
            self.created += 1
            status = "created"
        elif previous == text:
            self.unchanged += 1
            status = "unchanged"
        else:
            self.changed += 1
            status = "updated"

        if self.diff_mode:
            print(f"  {status:9} {path.name}")
        else:
            print(f"  saved     {path.name}")


def _error_message(exc: Exception) -> str:
    msg = str(exc).strip()
    if "insufficient authentication scopes" in msg.lower():
        return (
            f"{msg}\n\n"
            "Re-authenticate with Calendar scopes and rerun:\n"
            f"  gws auth login --account {DEFAULT_ACCOUNT} --services calendar"
        )
    return msg


def _short_reason(exc: Exception) -> str:
    msg = str(exc).strip()
    lower = msg.lower()
    if "insufficient authentication scopes" in lower:
        return "gws calendarList.list returned insufficientPermissions for this account during live capture."
    if "length required" in lower or "content-length header" in lower:
        return "gws sends quickAdd/move without Content-Length; Google responds with 411 Length Required."
    return msg


def _make_event_body(summary: str, start: datetime, end: datetime, **extra) -> dict:
    body = {
        "summary": summary,
        "start": {"dateTime": start.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"), "timeZone": "UTC"},
        "end": {"dateTime": end.astimezone(timezone.utc).isoformat().replace("+00:00", "Z"), "timeZone": "UTC"},
    }
    # Include all optional fields by default so fixtures show the full response shape.
    # Individual callers can override via **extra.
    body.setdefault("location", "Conference Room A")
    body.setdefault("description", "Fixture test event with all optional fields")
    body.setdefault("attendees", [{"email": "fixture-user@example.com"}])
    body.update(extra)
    return body


def _write_metadata(account: str, skipped: list[dict[str, str]] | None = None) -> None:
    fixture_count = len([p for p in FIXTURES_DIR.glob("*.json") if not p.name.startswith("_")])
    metadata = {
        "captured_at": datetime.now(timezone.utc).isoformat(),
        "account": account,
        "api_version": "v3",
        "api_base": API_BASE,
        "auth_method": "google-workspace-cli (gws auth login)",
        "capture_script": "scripts/capture_fixtures.py",
        "fixture_count": fixture_count,
        "note": "Capture creates and cleans up a temporary calendar, events, and ACL rule.",
    }
    if skipped:
        metadata["skipped"] = skipped
    (FIXTURES_DIR / "_capture_metadata.json").write_text(json.dumps(metadata, indent=2) + "\n")


def capture(account: str, diff_mode: bool) -> None:
    saver = Saver(FIXTURES_DIR, diff_mode=diff_mode)
    skipped: list[dict[str, str]] = []

    now = datetime.now(timezone.utc).replace(microsecond=0)
    start = now + timedelta(days=1)
    end = start + timedelta(hours=1)
    start_2 = start + timedelta(days=1)
    end_2 = start_2 + timedelta(hours=2)

    temp_calendar_id: str | None = None
    move_event_id: str | None = None
    primary_temp_event_id: str | None = None

    try:
        # Capture calendarList BEFORE any mutations for a clean baseline
        print("Capturing calendarList baseline (pre-mutation)...")
        try:
            saver.save("calendarlist_list", _run_gws("calendarList", "list", account=account, params={"userId": "me"}))
        except Exception as exc:
            skipped.append({
                "fixture": "calendarlist_list.json",
                "endpoint": "calendar.calendarList.list",
                "reason": _short_reason(exc),
            })
            print("  skipped   calendarlist_list.json (kept existing fixture)")

        print("Capturing primary and singleton resources...")
        saver.save("colors_get", _run_gws("colors", "get", account=account))
        saver.save("settings_list", _run_gws("settings", "list", account=account, params={"userId": "me"}))
        saver.save(
            "settings_get_timezone",
            _run_gws("settings", "get", account=account, params={"userId": "me", "setting": "timezone"}),
        )
        saver.save(
            "calendarlist_get_primary",
            _run_gws("calendarList", "get", account=account, params={"userId": "me", "calendarId": "primary"}),
        )
        saver.save("calendars_get_primary", _run_gws("calendars", "get", account=account, params={"calendarId": "primary"}))
        saver.save("acl_list_primary", _run_gws("acl", "list", account=account, params={"calendarId": "primary"}))
        saver.save(
            "freebusy_query_primary",
            _run_gws(
                "freebusy",
                "query",
                account=account,
                body={
                    "timeMin": (now - timedelta(days=1)).isoformat().replace("+00:00", "Z"),
                    "timeMax": (now + timedelta(days=1)).isoformat().replace("+00:00", "Z"),
                    "items": [{"id": "primary"}],
                },
            ),
        )

        primary_list_params = {
            "calendarId": "primary",
            "maxResults": 5,
            "singleEvents": True,
            "orderBy": "startTime",
            "timeMin": (now - timedelta(days=1)).isoformat().replace("+00:00", "Z"),
        }
        primary_events = _run_gws(
            "events",
            "list",
            account=account,
            params=primary_list_params,
        )
        if not primary_events.get("items"):
            primary_insert = _run_gws(
                "events",
                "insert",
                account=account,
                params={"calendarId": "primary"},
                body=_make_event_body("Fixture Primary Event", start, end),
            )
            primary_temp_event_id = primary_insert["id"]
            primary_events = _run_gws(
                "events",
                "list",
                account=account,
                params=primary_list_params,
            )
        saver.save("events_list_primary", primary_events)
        primary_event_id = primary_events["items"][0]["id"]
        saver.save(
            "events_get_primary",
            _run_gws("events", "get", account=account, params={"calendarId": "primary", "eventId": primary_event_id}),
        )

        print("Capturing temporary secondary calendar lifecycle...")
        temp_name = f"Fixture Temp {uuid4().hex[:8]}"
        created_calendar = _run_gws(
            "calendars",
            "insert",
            account=account,
            body={"summary": temp_name, "description": "Fixture baseline", "timeZone": "UTC"},
        )
        temp_calendar_id = created_calendar["id"]
        saver.save("calendars_insert_response", created_calendar)

        patched_calendar = _run_gws(
            "calendars",
            "patch",
            account=account,
            params={"calendarId": temp_calendar_id},
            body={"summary": f"{temp_name} Patched"},
        )
        saver.save("calendars_patch_response", patched_calendar)

        updated_calendar = _run_gws(
            "calendars",
            "update",
            account=account,
            params={"calendarId": temp_calendar_id},
            body={"summary": "Updated 172946", "description": "Updated desc", "timeZone": "UTC"},
        )
        saver.save("calendars_update_response", updated_calendar)

        _run_gws(
            "calendarList",
            "patch",
            account=account,
            params={"userId": "me", "calendarId": temp_calendar_id},
            body={"selected": True, "colorId": "3"},
        )
        saver.save(
            "calendarlist_get_secondary",
            _run_gws("calendarList", "get", account=account, params={"userId": "me", "calendarId": temp_calendar_id}),
        )

        print("Capturing ACL lifecycle...")
        acl_insert = _run_gws(
            "acl",
            "insert",
            account=account,
            params={"calendarId": temp_calendar_id},
            body={"role": "reader", "scope": {"type": "user", "value": "fixture-user@example.com"}},
        )
        acl_rule_id = acl_insert["id"]
        saver.save("acl_insert_response", acl_insert)
        saver.save(
            "acl_get_response",
            _run_gws("acl", "get", account=account, params={"calendarId": temp_calendar_id, "ruleId": acl_rule_id}),
        )
        saver.save(
            "acl_patch_response",
            _run_gws(
                "acl",
                "patch",
                account=account,
                params={"calendarId": temp_calendar_id, "ruleId": acl_rule_id},
                body={"role": "writer"},
            ),
        )
        saver.save(
            "acl_update_response",
            _run_gws(
                "acl",
                "update",
                account=account,
                params={"calendarId": temp_calendar_id, "ruleId": acl_rule_id},
                body={"role": "reader", "scope": {"type": "user", "value": "fixture-user@example.com"}},
            ),
        )

        print("Capturing event lifecycle and conformance fixtures...")
        inserted_event = _run_gws(
            "events",
            "insert",
            account=account,
            params={"calendarId": temp_calendar_id},
            body=_make_event_body(
                "Fixture Event 172946",
                start,
                end,
                description="Fixture body",
                location="Virtual",
            ),
        )
        event_id = inserted_event["id"]
        saver.save("events_insert_response", inserted_event)
        saver.save(
            "events_list_secondary",
            _run_gws("events", "list", account=account, params={"calendarId": temp_calendar_id}),
        )
        saver.save(
            "events_get_response",
            _run_gws("events", "get", account=account, params={"calendarId": temp_calendar_id, "eventId": event_id}),
        )
        saver.save(
            "events_patch_response",
            _run_gws(
                "events",
                "patch",
                account=account,
                params={"calendarId": temp_calendar_id, "eventId": event_id},
                body={"summary": "Patched", "description": "Fixture body", "location": "Virtual"},
            ),
        )
        saver.save(
            "events_update_response",
            _run_gws(
                "events",
                "update",
                account=account,
                params={"calendarId": temp_calendar_id, "eventId": event_id},
                body=_make_event_body(
                    "Updated",
                    start_2,
                    end_2,
                    description="updated",
                    location="Room B",
                ),
            ),
        )

        import_error = _run_gws(
            "events",
            "import",
            account=account,
            params={"calendarId": temp_calendar_id},
            body=_make_event_body("Import without UID", start, end),
            allow_error=True,
        )
        saver.save("events_import_response", import_error)

        recurring_event = _run_gws(
            "events",
            "insert",
            account=account,
            params={"calendarId": temp_calendar_id},
            body=_make_event_body(
                "Fixture Recurring Event",
                start,
                end,
                description="Fixture body",
                location="Virtual",
                recurrence=["RRULE:FREQ=DAILY;COUNT=1"],
            ),
        )
        saver.save(
            "events_instances_response",
            _run_gws(
                "events",
                "instances",
                account=account,
                params={"calendarId": temp_calendar_id, "eventId": recurring_event["id"]},
            ),
        )

        watcher_id = f"fixture-watch-{uuid4().hex[:8]}"
        watch_response = _run_gws(
            "events",
            "watch",
            account=account,
            params={"calendarId": temp_calendar_id},
            body={"id": watcher_id, "type": "web_hook", "address": "https://example.com/hook"},
        )
        saver.save("events_watch_response", watch_response)

        try:
            saver.save(
                "events_quickadd_response",
                _run_gws(
                    "events",
                    "quickAdd",
                    account=account,
                    params={"calendarId": temp_calendar_id, "text": "Lunch tomorrow noon"},
                ),
            )
        except Exception as exc:
            skipped.append({
                "fixture": "events_quickadd_response.json",
                "endpoint": "calendar.events.quickAdd",
                "reason": _short_reason(exc),
            })
            print("  skipped   events_quickadd_response.json (kept existing fixture)")

        move_event = _run_gws(
            "events",
            "insert",
            account=account,
            params={"calendarId": temp_calendar_id},
            body=_make_event_body("Move Semantics Event", start, end),
        )
        move_event_id = move_event["id"]
        try:
            move_response = _run_gws(
                "events",
                "move",
                account=account,
                params={"calendarId": temp_calendar_id, "eventId": move_event_id, "destination": "primary"},
            )
            saver.save("events_move_response", move_response)
        except Exception as exc:
            skipped.append({
                "fixture": "events_move_response.json",
                "endpoint": "calendar.events.move",
                "reason": _short_reason(exc),
            })
            print("  skipped   events_move_response.json (kept existing fixture)")

        stop_response = _run_gws(
            "channels",
            "stop",
            account=account,
            body={"id": watch_response["id"], "resourceId": watch_response["resourceId"]},
            allow_error=True,
        )
        saver.save("channels_stop_response", stop_response)

        # --- Error response captures ---
        print("Capturing error responses...")

        # 404: event not found
        saver.save(
            "error_event_not_found",
            _run_gws(
                "events",
                "get",
                account=account,
                params={"calendarId": "primary", "eventId": "nonexistent_event_id_12345"},
                allow_error=True,
            ),
        )

        # 404: calendar not found
        saver.save(
            "error_calendar_not_found",
            _run_gws(
                "calendars",
                "get",
                account=account,
                params={"calendarId": "nonexistent_calendar_id_12345"},
                allow_error=True,
            ),
        )

        # 400: invalid event body (missing required fields)
        saver.save(
            "error_invalid_event",
            _run_gws(
                "events",
                "insert",
                account=account,
                params={"calendarId": "primary"},
                body={"summary": "Missing start/end"},
                allow_error=True,
            ),
        )

        _write_metadata(account, skipped=skipped)

    except Exception as exc:  # pragma: no cover - operational failure path
        print(_error_message(exc), file=sys.stderr)
        raise
    finally:
        if primary_temp_event_id:
            try:
                _run_gws(
                    "events",
                    "delete",
                    account=account,
                    params={"calendarId": "primary", "eventId": primary_temp_event_id},
                    allow_error=True,
                )
            except Exception:
                pass
        if move_event_id:
            try:
                _run_gws(
                    "events",
                    "delete",
                    account=account,
                    params={"calendarId": "primary", "eventId": move_event_id},
                    allow_error=True,
                )
            except Exception:
                pass
        if temp_calendar_id:
            try:
                _run_gws(
                    "calendars",
                    "delete",
                    account=account,
                    params={"calendarId": temp_calendar_id},
                    allow_error=True,
                )
                # Verify cleanup
                verify = _run_gws(
                    "calendars",
                    "get",
                    account=account,
                    params={"calendarId": temp_calendar_id},
                    allow_error=True,
                )
                if "error" not in str(verify):
                    print(f"  WARNING: temp calendar {temp_calendar_id} was NOT deleted — may pollute future captures")
            except Exception:
                pass

    total = len([p for p in FIXTURES_DIR.glob("*.json") if not p.name.startswith("_")])
    print()
    print(f"Captured {total} fixture files for account {account}.")
    if diff_mode:
        print(f"Diff summary: {saver.created} created, {saver.changed} updated, {saver.unchanged} unchanged")
    if skipped:
        print("Skipped live refresh for:")
        for item in skipped:
            print(f"  - {item['fixture']}: {item['reason']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--account", default=DEFAULT_ACCOUNT, help="Google account email for gws auth")
    parser.add_argument("--diff", action="store_true", help="Print per-fixture change status")
    args = parser.parse_args()
    capture(account=args.account, diff_mode=args.diff)


if __name__ == "__main__":
    main()
