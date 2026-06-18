# Mock GCal

A high-fidelity, stateful mock of the Google Calendar REST API, built for stress-testing AI agents that interact with Google Calendar.

## What it does

- **38 Google Calendar API endpoints** — calendarList, calendars, events, ACL, colors, freeBusy, settings, and channels
- **Stateful SQLite backend** — persistent CRUD across calendars, events, and ACL rules
- **Snapshot/restore** — save and reset DB state for deterministic evaluation runs
- **4 seed scenarios** — default, launch_crunch, travel_heavy, long_context — each with a curated content library of realistic calendar events
- **Evaluation task framework** with automated verifiers using DB state diffs and action logs
- **MCP server** — expose all endpoints as MCP tools via `fastapi-mcp`
- **Gymnasium environment** — `GCalToolEnv` for RL-style agent training

## Quick start

```bash
cd packages/environments/mock-gcal

# Seed with realistic calendar data and start the server
uv run mock-gcal seed --scenario default
uv run mock-gcal serve --no-mcp
# API:      http://127.0.0.1:9002/calendar/v3/users/me/calendarList
# API Docs: http://127.0.0.1:9002/docs
```

`uv run` reads `pyproject.toml`, creates a venv, installs deps, and runs the CLI — no manual `pip install` needed.

### Alternative: pip install

```bash
pip install -e ".[all]"
mock-gcal seed
mock-gcal serve
```

## Scenarios

| Scenario | Events | Use case |
|----------|--------|----------|
| `default` | ~72 | Quick testing and development |
| `launch_crunch` | ~96 | Launch-heavy week with war rooms and leadership syncs |
| `travel_heavy` | ~88 | Conference and customer travel with dense logistics |
| `long_context` | ~1400 | Stress-testing: search, date filtering, long-horizon tasks |

The seeded user is **Alex Chen** (`alex@nexusai.com`) at a fictional AI startup, NexusAI. Calendars include primary, team, product, leadership, recruiting, travel, family, and US holidays.

## CLI

```
mock-gcal seed              # Seed DB with realistic data (options: --scenario, --seed, --users)
mock-gcal serve             # Start server (default :9002, options: --host, --port, --no-mcp)
mock-gcal reset             # Restore DB to initial seed state
mock-gcal list-tasks        # Show all registered evaluation tasks
mock-gcal run-task <name>   # Print task instructions for an agent
mock-gcal eval-task <name>  # Evaluate task completion (PASS/FAIL + reward)
```

## Verification framework

`mock-gcal` now follows the same verification pattern as `mock-gmail`:

- `tests/test_api.py` — functional and Google-style error behavior checks
- `tests/test_conformance.py` — response-shape checks against real Calendar fixtures
- `tests/test_seed.py` — seed richness and invariants
- `tests/fixtures/gcal_api_spec.json` — endpoint inventory / completeness baseline
- `tests/fixtures/mock_coverage.json` — endpoint -> fixture -> test mapping
- `tests/fixtures/real_gcal/` — golden responses from the real Calendar API
- `scripts/capture_fixtures.py` — refresh live fixtures via `gws`
- `scripts/validate_seed.py` — validate seeded data assumptions
- `API_NOTES.md` — Calendar quirks, coverage boundaries, and capture notes

Run the full validation suite:

```bash
cd packages/environments/mock-gcal
uv run --extra dev pytest tests/ -q
```

## API compatibility

The API is mounted at `/calendar/v3/` and mirrors the Google Calendar REST API:

```
# Calendar List
GET    /calendar/v3/users/me/calendarList
GET    /calendar/v3/users/me/calendarList/{calendarId}
POST   /calendar/v3/users/me/calendarList
PATCH  /calendar/v3/users/me/calendarList/{calendarId}
DELETE /calendar/v3/users/me/calendarList/{calendarId}

# Calendars
GET    /calendar/v3/calendars/{calendarId}
POST   /calendar/v3/calendars
PATCH  /calendar/v3/calendars/{calendarId}
DELETE /calendar/v3/calendars/{calendarId}

# Events
GET    /calendar/v3/calendars/{calendarId}/events
GET    /calendar/v3/calendars/{calendarId}/events/{eventId}
POST   /calendar/v3/calendars/{calendarId}/events
PATCH  /calendar/v3/calendars/{calendarId}/events/{eventId}
DELETE /calendar/v3/calendars/{calendarId}/events/{eventId}
GET    /calendar/v3/calendars/{calendarId}/events/{eventId}/instances
POST   /calendar/v3/calendars/{calendarId}/events/quickAdd
POST   /calendar/v3/calendars/{calendarId}/events/{eventId}/move

# ACL
GET    /calendar/v3/calendars/{calendarId}/acl
GET    /calendar/v3/calendars/{calendarId}/acl/{ruleId}
POST   /calendar/v3/calendars/{calendarId}/acl
PATCH  /calendar/v3/calendars/{calendarId}/acl/{ruleId}
DELETE /calendar/v3/calendars/{calendarId}/acl/{ruleId}

# Colors / FreeBusy / Settings / Channels
GET    /calendar/v3/colors
POST   /calendar/v3/freeBusy
GET    /calendar/v3/users/me/settings
GET    /calendar/v3/users/me/settings/{setting}
POST   /calendar/v3/channels/stop
```

Agents using any Google Calendar client library can point at this server instead of `googleapis.com` with zero code changes — just override the base URL.

## Admin endpoints

These endpoints are used by evaluation frameworks to observe and control server state:

```
GET  /health                          # Liveness check
POST /_admin/reset                    # Restore DB to initial seed state
POST /_admin/seed?scenario=default    # Re-seed from scratch
GET  /_admin/state                    # Full DB state dump (JSON)
GET  /_admin/diff                     # Diff vs initial snapshot
GET  /_admin/action_log               # Ordered log of all API calls made
POST /_admin/snapshot/{name}          # Save current state as named snapshot
POST /_admin/restore/{name}           # Restore from named snapshot
GET  /_admin/tasks                    # List all evaluation tasks
POST /_admin/tasks/{name}/evaluate    # Run task evaluator, returns reward + done
```

Typical evaluation loop:

```python
# 1. Reset to clean state
requests.post("http://127.0.0.1:9002/_admin/reset")

# 2. Run agent against /calendar/v3/* endpoints
agent.run(task.instruction)

# 3. Evaluate
result = requests.post("http://127.0.0.1:9002/_admin/tasks/my-task/evaluate").json()
print(result["reward"], result["done"])
```

## Project structure

```
packages/environments/mock-gcal/
├── API_NOTES.md
├── mock_gcal/
│   ├── api/              # FastAPI routes (calendars, events, acl, colors, freebusy, settings, channels)
│   ├── models/           # SQLAlchemy ORM (User, Calendar, Event, AclRule)
│   ├── seed/             # Realistic calendar content + scenario generator
│   │   └── content_library/  # Event pools: work, ops, security, personal, travel
│   ├── state/            # Snapshot save/restore, action logging, channel registry
│   ├── tasks/            # Evaluation task base class + registry
│   ├── env/              # Gymnasium environment wrapper (GCalToolEnv)
│   ├── mcp/              # MCP server via fastapi-mcp
│   ├── cli.py            # CLI entry point
│   └── server.py         # Uvicorn server setup
├── scripts/
│   ├── capture_fixtures.py
│   └── validate_seed.py
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   ├── test_conformance.py
│   ├── test_seed.py
│   └── fixtures/
│       ├── gcal_api_spec.json
│       ├── mock_coverage.json
│       └── real_gcal/
└── pyproject.toml
```

## env0

This environment lives at `packages/environments/mock-gcal/` inside env0.
Use the repo root launcher for multi-service sessions and example-task seeding.
