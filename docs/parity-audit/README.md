# Parity Audit

Parity audit is the cross-env review layer for API fidelity. It summarizes how
well each mock matches real API fixtures and where conformance work remains.

Source material was ported from the initial parity-audit notebooks.
Paths/names were mechanically updated toward `packages/environments/mock-*`.

## Current Fixture Set

Current real golden fixture count in `env0`:

- Gmail: 35 fixtures
- GCal: 31 fixtures
- GDocs: 6 fixtures
- GDrive: 42 fixtures
- Slack: 57 fixtures
- Total: 171 golden fixtures

Regenerate this count with:

```bash
python3 - <<'PY'
from pathlib import Path

root = Path("packages/environments")
for env in ["mock-gmail", "mock-gcal", "mock-gdoc", "mock-gdrive", "mock-slack"]:
    real_dirs = (root / env / "tests" / "fixtures").glob("real_*")
    count = sum(
        1
        for real_dir in real_dirs
        for p in real_dir.glob("*.json")
        if p.name != "_capture_metadata.json"
    )
    print(env, count)
PY
```

See [AUDIT_RESULTS.md](AUDIT_RESULTS.md).

## What To Audit

For each env:

- every implemented endpoint has fixture coverage or documented skip reason
- every fixture is referenced by conformance tests
- success and error response shapes match real fixtures
- pagination behavior is covered where applicable
- mutation side effects are covered by functional tests
- `API_NOTES.md` documents known divergences

## Commands

Run one env conformance suite:

```bash
cd packages/environments/mock-gdrive
uv run --extra dev pytest tests/test_conformance.py -q
```

Run all tests for one env:

```bash
cd packages/environments/mock-gdrive
uv run --extra dev pytest tests -q
```

Re-capture fixtures when credentials are available:

```bash
cd packages/environments/mock-gdrive
uv run python scripts/capture_fixtures.py
```

## Notebook Status

The notebooks are included as starting points:

- `gmail-parity-audit.ipynb`
- `gcal-parity-audit.ipynb`
- `gdoc-parity-audit.ipynb`
- `gdrive-parity-audit.ipynb`
- `slack-parity-audit.ipynb`

Treat them as review artifacts until each one is rerun in the env0 repo.
Before using a notebook as a gate, verify it:

- load fixtures from `packages/environments/mock-*/tests/fixtures`
- read `mock_coverage.json`
- report fixture freshness
- report endpoint and fixture coverage
- list blocking parity gaps
