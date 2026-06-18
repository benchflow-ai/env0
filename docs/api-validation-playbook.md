# API Validation Playbook

Use this playbook to keep mock REST APIs aligned with real services. The goal
is deterministic, high-fidelity agent testing without live credentials during
normal evaluation.

Names and commands here use `mock-*` packages.

## Artifacts

Each environment should maintain:

```text
packages/environments/mock-<service>/
├── API_NOTES.md
├── scripts/
│   ├── auth.py
│   └── capture_fixtures.py
└── tests/
    ├── test_api.py
    ├── test_conformance.py
    └── fixtures/
        ├── mock_coverage.json
        ├── <service>_api_spec.json
        └── real_<service>/
            ├── _capture_metadata.json
            └── *.json
```

## Quick Commands

Run conformance for one env:

```bash
cd packages/environments/mock-gdrive
uv run --extra dev pytest tests/test_conformance.py -q
```

Run all tests for one env:

```bash
cd packages/environments/mock-gdrive
uv run --extra dev pytest tests -q
```

Re-capture fixtures only when credentials are available:

```bash
cd packages/environments/mock-gdrive
if find scripts -maxdepth 1 -name 'client_secret*.json' | grep -q .; then
  uv run python scripts/capture_fixtures.py
else
  echo "Skipping capture: add scripts/client_secret*.json first"
fi
```

Credentials and tokens must stay local and gitignored. Typical locations:

- `scripts/credentials.json`
- `scripts/token.json`
- `scripts/slack_token.json`
- repo-level `secrets/`

Do not commit live credentials or copied account data that is not already part
of deliberate golden fixtures.

## Phase 0: Inventory

For each mock API, record:

- implemented routes
- official API docs URL
- auth method for real API capture
- endpoint type: list, read, mutation, singleton
- shape-changing params: `format`, `fields`, `view`, `include`, `projection`
- required success and error fixtures

Store design decisions and known divergences in `API_NOTES.md`.

## Phase 1: Capture Golden Fixtures

Golden fixtures are real API JSON responses. Capture enough variants to define
the response contract:

- non-empty list responses
- empty list responses
- read response variants
- mutation responses
- default singleton settings
- not-found errors
- invalid request errors
- endpoint-specific errors

Capture scripts should:

- be idempotent
- clean up resources they create
- add per-fixture `_captured_at` metadata
- write `_capture_metadata.json` with run-level `captured_at`
- print missing or skipped endpoint coverage
- avoid committing credentials or tokens

Fixture metadata example:

```json
{
  "captured_at": "2026-03-27T12:00:00+00:00",
  "account": "test-account@example.com",
  "api_version": "v1",
  "auth_method": "OAuth 2.0",
  "capture_script": "scripts/capture_fixtures.py",
  "fixture_count": 41
}
```

Convention:

- individual fixture response JSONs carry `_captured_at`
- `_capture_metadata.json` carries run-level `captured_at`, `fixture_count`,
  account, API version, and notes
- tests should strip `_captured_at` before comparing API response bodies

## Phase 2: Compare Shapes

`tests/test_conformance.py` should compare mock responses against golden
fixtures.

Check:

- top-level keys
- nested object keys
- list item shape
- value types
- optional key behavior
- `null` vs absent
- empty collection shape
- error response shape

Tests should strip metadata fields such as `_captured_at` before comparison.

## Common Bug Classes

- Mutation response returns full object instead of sparse real response.
- Mock serializes `null` fields where real API omits keys.
- Format variants return same shape.
- Empty collections return `[]` where real API omits the collection key.
- Defaults are over-serialized.
- List items are too detailed compared to detail views.
- Error shape differs from real API.
- Pagination tokens or cursors are missing or malformed.
- State mutation side effects differ from real API.
- Subtype-specific fields are missing or always present.

## Coverage Rules

Every committed fixture should be referenced by at least one conformance test.
When adding fixtures, add tests in the same change.

`mock_coverage.json` should describe which mock endpoints are covered by which
fixtures/tests. Keep it in sync with route additions.

## Parity Report

For broad audits, use [parity audit](parity-audit/README.md). The audit tracks:

- fixture count and freshness
- endpoint implementation coverage
- fixture-to-test coverage
- known parity gaps

## When To Re-Capture

Re-capture when:

- implementing a new endpoint
- changing response schemas
- adding error handling
- real API docs changed
- fixtures are stale or missing metadata
- an agent failure suggests mock behavior differs from the real service

Do not guess real API shape. Capture it or document why capture is unavailable.
