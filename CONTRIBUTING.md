# Contributing to env0

env0 is a mock-environment runtime for agent testing. It owns first-party mock
service development, local environment tooling, deterministic seeding, API
parity, devhub surfaces, and the shared Docker base image.

If you want to contribute benchmark tasks or scoring policy, use the downstream
benchmark package that owns those tasks. In this repo, `example_tasks/` are
runtime fixtures and `tasks/` contains copied BenchFlow-native task packages for
reference and downstream evaluation.

## What To Contribute

| Area | Good contribution | Start here |
|---|---|---|
| Mock API fidelity | Add or correct endpoints, response shapes, errors, pagination, side effects, or conformance fixtures. | [`docs/api-validation-playbook.md`](docs/api-validation-playbook.md) |
| Environment packages | Add a new `mock-*` service or improve an existing one. | [`docs/adding-new-environment.md`](docs/adding-new-environment.md) |
| Seed realism | Improve deterministic seed data, filler distributions, role markers, or task-aware seed paths. | Existing `packages/environments/mock-*/seed/` modules |
| Dev tooling | Improve `scripts/dev.sh`, `scripts/env0_control.py`, devhub, smoke tests, or Docker base-image generation. | [`docs/dev.md`](docs/dev.md) |
| Documentation | Fix inaccurate commands, clarify preconditions, or document real parity gaps. | This file plus [`README.md`](README.md) |

## Boundaries

- Keep service ids and CLIs on current `mock-*` names.
- Keep service URL env vars on current `MOCK_*_URL` names.
- Read service metadata from `config.toml`; do not infer services from
  Dockerfile text.
- Keep public launcher UX task-name based: `scripts/dev.sh task <name>`.
- Keep raw `--task-data` plumbing internal to env CLIs, control scripts, and
  Dockerfiles.
- Preserve `example_tasks/*/environment/Dockerfile` as minimal runtime
  templates.
- Do not copy environment source code into thin task images.
- Do not commit credentials, OAuth tokens, live account exports, or private
  customer data.

## Development Setup

Use `uv run` from the relevant package directory. Normal workflows do not need
manual virtualenv setup.

From the repo root:

```bash
scripts/smoke_dev.sh
```

Start every configured mock service plus devhub:

```bash
scripts/dev.sh
```

Start only services declared by an example task:

```bash
scripts/dev.sh task gdrive-archive-stale-drafts
```

## Validation Matrix

Pick the narrowest checks that cover your change.

Launcher, control script, devhub, or seed routing:

```bash
scripts/smoke_dev.sh
```

One environment package:

```bash
cd packages/environments/mock-gdrive
uv run --extra dev pytest tests -q
```

API response-shape or golden-fixture work:

```bash
cd packages/environments/mock-gdrive
uv run --extra dev pytest tests/test_conformance.py -q
```

Docker base image or example task image changes:

```bash
docker/build-base.sh
PULL_BASE=0 scripts/smoke_docker_examples.sh
```

Copied BenchFlow task packages under `tasks/`:

```bash
for task in tasks/*; do
  [ -d "$task" ] || continue
  [ "$(basename "$task")" = "_manifests" ] && continue
  bench tasks check "$task" --level structural
done
```

The `tasks/` check requires the BenchFlow CLI. End-to-end evaluation of copied
tasks also requires a pullable `ghcr.io/benchflow-ai/env-0-base:latest` image.

## Pull Request Checklist

Before opening a PR:

- Run the validation command that matches your change.
- Update docs when changing seed, Docker, API, or devhub contracts.
- Add conformance coverage for committed real API fixtures.
- Keep unrelated refactors out of the PR.
- Make sure new commands in docs have been run or clearly state their
  preconditions.

In the PR body, include:

- What changed.
- Why it changed.
- The validation commands and results.
- Any credentials, image-publish permissions, or provider access that were
  intentionally not available.
