# Mock Slack

A high-fidelity, stateful mock of the Slack Web API, built for stress-testing AI agents that interact with Slack workspaces.

## What it does

- **41 Slack Web API endpoints** — conversations, chat, users, reactions, files, pins, reminders, search, team, auth
- **Stateful SQLite backend** — persistent CRUD across channels, messages, reactions, pins, files, and reminders
- **Snapshot/restore** — save and reset DB state for deterministic evaluation runs
- **57 golden fixtures** captured from a real Slack Developer Program sandbox with tests validating response shapes and behavior
- **Evaluation tasks** with automated verifiers using DB state diffs and action logs
- **MCP server** — expose all endpoints as MCP tools via `fastapi-mcp`
- **Web UI** — Slack-style channel/message view plus a standalone dev dashboard (API explorer, DB viewer)

## Quick start

```bash
cd packages/environments/mock-slack

# Seed with realistic workspace data and start the server
uv run mock-slack seed --scenario default
uv run mock-slack serve
# API:       http://127.0.0.1:9005/api/conversations.list
# Web UI:    http://127.0.0.1:9005/
# Dev tools: http://127.0.0.1:9005/dev/dashboard
# API Docs:  http://127.0.0.1:9005/docs
```

`uv run` reads `pyproject.toml`, creates a venv, installs deps, and runs the CLI — no manual `pip install` needed.

## Scenarios

| Scenario | Description | Use case |
|----------|-------------|----------|
| `default` | 10 channels, 10 users, realistic engineering startup messages | General agent testing |
| `safety_corporate` | Default + sensitive/confidential messages | Safety boundary testing |
| `long_context` | Default + 50+ extra messages per channel | Stress-testing search, pagination, long-horizon tasks |

The seeded workspace is **NexusAI**, a fictional AI startup. Users include engineers, a PM, designer, and a bot user.

## CLI

```text
mock-slack seed              # Seed DB (options: --scenario, --seed, --db)
mock-slack serve             # Start server (default :9005, options: --host, --port, --no-mcp)
mock-slack reset             # Restore DB to initial seed state
```

## API compatibility

All endpoints are mounted at `/api/` and mirror the Slack Web API method naming convention:

```text
# Conversations
GET  /api/conversations.list
GET  /api/conversations.info?channel=C123
GET  /api/conversations.history?channel=C123
GET  /api/conversations.members?channel=C123
GET  /api/conversations.replies?channel=C123&ts=1234
POST /api/conversations.create
POST /api/conversations.invite
POST /api/conversations.join
POST /api/conversations.kick
POST /api/conversations.leave
POST /api/conversations.rename
POST /api/conversations.setPurpose
POST /api/conversations.setTopic
POST /api/conversations.archive
POST /api/conversations.unarchive

# Chat
POST /api/chat.postMessage
POST /api/chat.postEphemeral
POST /api/chat.update
POST /api/chat.delete
GET  /api/chat.getPermalink

# Users
GET  /api/users.list
GET  /api/users.info
GET  /api/users.lookupByEmail
GET  /api/users.getPresence
POST /api/users.setPresence
GET  /api/users.profile.get
POST /api/users.profile.set

# Reactions / Pins / Files / Search / Team / Auth / Reminders
POST /api/reactions.add
POST /api/reactions.remove
GET  /api/reactions.get
POST /api/pins.add
POST /api/pins.remove
GET  /api/pins.list
GET  /api/files.list
GET  /api/files.info
POST /api/files.upload
POST /api/files.delete
GET  /api/search.messages
GET  /api/team.info
POST /api/auth.test
GET  /api/reminders.list
```

All responses follow the Slack API envelope: `{"ok": true, ...}` on success and `{"ok": false, "error": "..."}` on error, always HTTP 200.

Agents using any Slack SDK can point at this server with zero code changes — just set the base URL to `http://127.0.0.1:9005`.

## Admin endpoints / evaluation harness

```text
POST /_admin/reset                    # Restore DB to initial seed state
POST /_admin/seed?scenario=default    # Re-seed from scratch
GET  /_admin/state                    # Full DB state dump (JSON)
GET  /_admin/diff                     # Diff vs initial snapshot
GET  /_admin/action_log               # Ordered log of all API calls made
POST /_admin/snapshot/{name}          # Save current state as named snapshot
POST /_admin/restore/{name}           # Restore from named snapshot
```

Typical evaluation loop:

```python
# 1. Reset to clean state
requests.post("http://127.0.0.1:9005/_admin/reset")

# 2. Run agent against /api/* endpoints
agent.run(task.instruction)

# 3. Inspect state/diff/action log from the admin endpoints
state = requests.get("http://127.0.0.1:9005/_admin/state").json()
diff = requests.get("http://127.0.0.1:9005/_admin/diff").json()
```

## Testing

```bash
uv run --extra dev pytest tests -q
```

| Suite | What it covers |
|-------|----------------|
| `test_conformance.py` | Response-shape validation against real Slack API golden fixtures |
| `test_api.py` | Functional CRUD: channel lifecycle, message lifecycle, membership, files, search, error cases |
| `test_pagination.py` | Cursor pagination behavior |

### Golden fixtures

Fixtures in `tests/fixtures/real_slack/` are captured from a Slack Developer Program sandbox. Conformance tests check that the mock's response structure (keys, types, nesting) matches the real Slack fixture — not exact values, since IDs and timestamps differ.

See `tests/fixtures/mock_coverage.json` for the full mapping of spec endpoint → fixture → tests.

## Seed validation

```bash
python scripts/validate_seed.py
```

Validates that the default seed meets invariants: correct user count, all persona emails present, thread reply counts consistent, files/pins/reminders seeded.

## Project structure

```
packages/environments/mock-slack/
├── API_NOTES.md                      # Ground truth, API quirks, design decisions
├── mock_slack/
│   ├── api/              # FastAPI routes (conversations, chat, users, reactions, pins, files, search, team, auth, reminders)
│   ├── models/           # SQLAlchemy ORM (Workspace, SlackUser, Channel, Message, Reaction, SlackFile, Pin, Reminder)
│   ├── seed/             # Realistic workspace content + scenario generator
│   ├── state/            # Snapshot save/restore + action logging
│   ├── tasks/            # Evaluation task base class + registry
│   ├── web/              # Web UI (Slack view + standalone dev dashboard)
│   ├── cli.py            # CLI entry point
│   └── server.py         # Uvicorn server setup
├── scripts/
│   ├── slack_auth.py         # One-time auth for real Slack API
│   ├── capture_fixtures.py   # Captures golden fixtures from real workspace
│   └── validate_seed.py      # Validates seed data meets evaluator expectations
└── tests/
    ├── fixtures/
    │   ├── slack_api_spec.json       # All 83 real Slack API endpoints
    │   ├── mock_coverage.json        # Endpoint → fixture → test mapping
    │   └── real_slack/               # 57 golden fixtures + _capture_metadata.json
    ├── conftest.py                   # Seeded DB + TestClient fixture
    ├── test_conformance.py
    ├── test_api.py
    └── test_pagination.py
```
