# Mock GDrive

A high-fidelity, stateful mock of the Google Drive REST API v3, built for stress-testing AI coding agents that interact with Google Drive.

## Why this exists

AI coding agents increasingly perform real-world tasks: organizing files, managing permissions, cleaning up storage, sharing documents. When these agents run against a real Google Drive account, mistakes are irreversible — a bad prompt can delete critical files, expose sensitive documents publicly, or destroy folder structures built over years.

Mock GDrive provides a safe, fully stateful Drive environment where agents can be exercised against realistic data without touching production accounts. It is part of env0's first-party mock environment suite.

## What it does

- **41 Drive API v3 endpoints** (100% of core methods, 72% of all 57 methods — 16 deprecated/niche methods intentionally skipped) — files, permissions, comments, replies, revisions, changes, shared drives, about
- **Full search query parser** — `lark`-based PEG grammar supporting `and`, `or`, `not`, `contains`, `in parents`, datetime comparisons, parenthetical grouping, `fullText contains`, and property queries
- **Stateful SQLite backend** — 8 ORM models (User, File, Permission, Comment, Reply, Revision, Change, Drive), 37 File columns, 43 file capability flags, 21 drive capability flags
- **Snapshot/restore** — save and reset DB state for deterministic evaluation runs
- **12 golden fixtures** captured from a real Google Drive account with 33 conformance tests validating response shapes match real Drive + 25 golden fixture tests
- **`fields` parameter** — matches real API default behavior: `files.list` returns only `{kind, id, name, mimeType}` without `fields`; `files.get` returns full resource
- **Web UI** — file browser with folder navigation, detail view, user switching
- **211 tests** covering all endpoints, query parser, capabilities, conformance, and golden fixtures

## Quick start

```bash
cd packages/environments/mock-gdrive

# Seed with realistic Drive data and start the server
uv run mock-gdrive seed
uv run mock-gdrive serve
# API:      http://127.0.0.1:9003/drive/v3/files
# Web UI:   http://127.0.0.1:9003/
# API Docs: http://127.0.0.1:9003/docs
```

`uv run` reads `pyproject.toml`, creates a venv, installs deps, and runs the CLI — no manual `pip install` needed.

### Alternative: pip install

If you prefer a traditional install:

```bash
pip install -e ".[all]"
mock-gdrive seed
mock-gdrive serve
```

## CLI

```
mock-gdrive seed              # Seed DB with realistic Drive data (~552 items: 7 users, 52 folders, ~500 files)
mock-gdrive serve              # Start API server (default :9003)
mock-gdrive reset              # Restore DB to initial seed state
```

## API compatibility

The API is mounted at `/drive/v3/` and mirrors Google's Drive REST API v3:

```
GET    /drive/v3/files
GET    /drive/v3/files/{fileId}
POST   /drive/v3/files
PATCH  /drive/v3/files/{fileId}
DELETE /drive/v3/files/{fileId}
POST   /drive/v3/files/{fileId}/copy
GET    /drive/v3/files/{fileId}/export
GET    /drive/v3/files/generateIds
DELETE /drive/v3/files/trash
POST   /drive/v3/files/{fileId}/watch

GET    /drive/v3/files/{fileId}/permissions
GET    /drive/v3/files/{fileId}/permissions/{permissionId}
POST   /drive/v3/files/{fileId}/permissions
PATCH  /drive/v3/files/{fileId}/permissions/{permissionId}
DELETE /drive/v3/files/{fileId}/permissions/{permissionId}

GET    /drive/v3/files/{fileId}/comments
GET    /drive/v3/files/{fileId}/comments/{commentId}
POST   /drive/v3/files/{fileId}/comments
PATCH  /drive/v3/files/{fileId}/comments/{commentId}
DELETE /drive/v3/files/{fileId}/comments/{commentId}

GET    /drive/v3/files/{fileId}/comments/{commentId}/replies
GET    /drive/v3/files/{fileId}/comments/{commentId}/replies/{replyId}
POST   /drive/v3/files/{fileId}/comments/{commentId}/replies
PATCH  /drive/v3/files/{fileId}/comments/{commentId}/replies/{replyId}
DELETE /drive/v3/files/{fileId}/comments/{commentId}/replies/{replyId}

GET    /drive/v3/files/{fileId}/revisions
GET    /drive/v3/files/{fileId}/revisions/{revisionId}
PATCH  /drive/v3/files/{fileId}/revisions/{revisionId}
DELETE /drive/v3/files/{fileId}/revisions/{revisionId}

GET    /drive/v3/changes/startPageToken
GET    /drive/v3/changes
POST   /drive/v3/changes/watch
POST   /drive/v3/channels/stop

GET    /drive/v3/drives
GET    /drive/v3/drives/{driveId}
POST   /drive/v3/drives
PATCH  /drive/v3/drives/{driveId}
DELETE /drive/v3/drives/{driveId}
POST   /drive/v3/drives/{driveId}/hide
POST   /drive/v3/drives/{driveId}/unhide

GET    /drive/v3/about
```

Upload paths are also registered at `/upload/drive/v3/files` and `/upload/drive/v3/files/{fileId}`.

Agents using any Drive client library can point at this server instead of `googleapis.com` with zero code changes.

Admin endpoints for evaluation harnesses:

```
POST   /_admin/reset           # Reset to seed state
POST   /_admin/seed            # Re-seed database
GET    /_admin/state            # Full DB state dump
GET    /_admin/diff             # Diff from seed snapshot
GET    /_admin/action_log       # All API actions taken
POST   /_admin/snapshot/{name}  # Save named snapshot
POST   /_admin/restore/{name}   # Restore named snapshot
```

## Authentication

The mock identifies the current user via:

1. `X-Mock-Drive-User` header — resolve by user ID or email
2. `Authorization: Bearer <user_id_or_email>` header
3. Fallback — first user in database

The current user determines file visibility, permissions, and capabilities.

## Seed data

`mock-gdrive seed` creates a realistic startup Google Drive (~552 items):

- **7 users**: Alex Chen (owner/founder), Jordan Kim, Priya Sharma, Marcus Thompson, Sarah Lin (team), David Park (investor), DataFlow Support (vendor)
- **52 folders** in a realistic hierarchy: Engineering, Product, Finance, HR, Legal, Marketing, Shared, tmp
- **35 handwritten files** with multi-paragraph content (budget documents, pitch decks, API specs, contracts, meeting notes)
- **~463 filler files** with generated names and placeholder content (45% Docs, 25% Sheets, 15% PDFs, 10% PNGs, 5% CSVs)
- **2 shortcuts** pointing across folders
- **~15%** of filler files randomly shared with other users
- `content_text` populated for all Google Docs/Sheets/CSV files (enables `fullText contains` queries)

## Testing

```bash
uv run --extra dev pytest tests -q
```

| Suite | Tests | What it covers |
|-------|-------|----------------|
| `test_files.py` | 43 | Files CRUD, search, ordering, trash, copy, export, upload |
| `test_conformance.py` | 33 | Response shape validation against Drive API Discovery Document |
| `test_golden_fixtures.py` | 25 | Mock responses vs 12 real Drive API captures |
| `test_drives.py` | 23 | Shared drives CRUD, hide/unhide, pagination, query |
| `test_query_parser.py` | 18 | All query operators: `=`, `!=`, `<`, `>`, `contains`, `in`, `and`, `or`, `not` |
| `test_permissions.py` | 15 | Permissions CRUD, transfer ownership, visibility scoping |
| `test_comments.py` | 15 | Comments + replies CRUD, resolve/reopen, deleted handling |
| `test_capabilities.py` | 12 | 43 capability flags computed from role/ownership |
| `test_fields.py` | 12 | `fields` parameter parsing, default behavior, nested selection |
| `test_revisions.py` | 7 | Revisions CRUD, publishing flags |
| `test_changes.py` | 6 | Changes feed, startPageToken, channels.stop |
| `test_about.py` | 2 | About endpoint, storage quota |

## Fidelity

See [API_NOTES.md](API_NOTES.md) §3–4 for skipped methods and known simplifications. Key points:

- 41/57 methods implemented (16 deprecated/niche skipped)
- No resumable upload protocol (simple/multipart works)
- No OAuth scope enforcement
- `files.export` returns stored text without format conversion
- `files.watch` / `changes.watch` are no-op stubs (no push notifications)
- `fullText contains` uses SQL `LIKE` (no stemming/relevance ranking)

## Project structure

```
packages/environments/mock-gdrive/
├── mock_gdrive/
│   ├── api/              # FastAPI routes (files, permissions, comments, replies, revisions, changes, drives, about)
│   ├── models/           # SQLAlchemy ORM (User, File, Permission, Comment, Reply, Revision, Change, Drive)
│   ├── seed/             # Realistic Drive content + folder hierarchy + filler generator
│   ├── state/            # Snapshot save/restore + action logging
│   ├── web/              # Web UI (file browser, detail view, user switching)
│   ├── cli.py            # CLI entry point
│   └── server.py         # Uvicorn server setup
├── tests/
│   ├── fixtures/         # Golden fixtures from real Drive + Discovery Document
│   └── test_*.py         # 211 tests
├── scripts/              # Drive auth + fixture capture from real account
├── API_NOTES.md          # Ground truth, quirks, simplifications, design choices
└── pyproject.toml
```

## env0

This environment lives at `packages/environments/mock-gdrive/` inside env0. Use the repo root launcher for multi-service sessions and example-task seeding.
