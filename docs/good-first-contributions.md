# Good First Contributions

env0 gets better when its mock services behave more like the real systems they
stand in for. High-value contributions are usually small, testable improvements
to API fidelity, seed realism, dev tooling, or documentation accuracy.

## Best First Issues

1. **Add missing conformance fixtures.** Pick one endpoint in Gmail, Calendar,
   Docs, Drive, or Slack, capture or update a real fixture, and add a
   `test_conformance.py` assertion that compares the mock shape to the fixture.
2. **Improve error parity.** Real APIs often return sparse, structured errors.
   Matching status codes, error bodies, and edge cases is more valuable than
   adding happy-path methods.
3. **Strengthen action logs.** Verifiers and debugging tools depend on
   `/_admin/action_log`. Add meaningful entries for mutations, searches, and
   permission changes.
4. **Improve seed realism.** Add deterministic filler data that resembles real
   inboxes, calendars, docs, drives, or Slack workspaces without leaking
   private data or making task intent obvious.
5. **Polish dev surfaces.** `/dev/dashboard`, `/dev/api-explorer`, and
   `/dev/db-viewer` should make local debugging faster without becoming a
   benchmark dashboard.
6. **Tighten docs by running commands.** If a documented command fails in a
   clean checkout, fix the command or document its preconditions.

## What Not To Do

- Do not make env0 the source of truth for benchmark tasks or scoring policy.
- Do not add legacy service names when current `mock-*` and `MOCK_*` contracts
  already exist.
- Do not infer services from Dockerfile text. Service metadata comes from
  `config.toml`.
- Do not commit credentials, OAuth tokens, or uncensored live account exports.

## Small PR Checklist

Before opening a PR, run the narrowest checks that cover your change:

```bash
scripts/smoke_dev.sh
```

For a single environment package:

```bash
cd packages/environments/mock-gdrive
uv run --extra dev pytest tests -q
```

For a response-shape change:

```bash
cd packages/environments/mock-gdrive
uv run --extra dev pytest tests/test_conformance.py -q
```

For Docker/base-image or example task changes:

```bash
docker/build-base.sh
PULL_BASE=0 scripts/smoke_docker_examples.sh
```
