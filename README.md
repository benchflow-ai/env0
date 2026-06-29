# env0

[![CI](https://github.com/benchflow-ai/env0/actions/workflows/ci.yml/badge.svg)](https://github.com/benchflow-ai/env0/actions/workflows/ci.yml)

env0 is the first-party mock-environment runtime for agent testing. It provides
stateful, deterministic mock services for local development, seed contracts,
API-parity checks, dev tooling, and a shared Docker base image.

The repo has two deliberately separate task surfaces:

- `example_tasks/` are small runtime fixtures used to prove env0 service and
  launcher contracts.
- `tasks/` contains the small selected BenchFlow-native task package set kept
  for reference and downstream evaluation.
- `env0-mobile/` contains larger copied task corpora for mobile/post-training
  workflows.

Canonical benchmark authoring and scoring policy still belong in downstream
benchmark repos, not in env0.

## Quick Start

Run commands from the `env0` repo root. Prerequisites:

- Python 3.12+
- `uv`
- Docker daemon for Docker/base-image smoke checks
- free local ports `9001`-`9005` and `9060`

Run the unit/control smoke:

```bash
scripts/smoke_dev.sh
```

Render the devhub once without starting services:

```bash
python3 devhub/app.py --render-once
```

Start every configured mock service plus devhub:

```bash
scripts/dev.sh
```

Stop with `Ctrl-C`. Local DBs and runtime state live under `.data/dev/`; remove
that directory if you want a clean local-dev state.

Start only services declared by an example task:

```bash
scripts/dev.sh task gdrive-archive-stale-drafts
```

Open devhub:

```text
http://127.0.0.1:9060
```

## Docker Base Image

The shared base image tag is:

```text
ghcr.io/benchflow-ai/env0:0.1.0
```

`VERSION` is the source of truth for the semver tag. Example task Dockerfiles
pin `FROM ghcr.io/benchflow-ai/env0:<VERSION>`.

Build locally:

```bash
docker/build-base.sh
```

Validate example task images against the locally built base:

```bash
PULL_BASE=0 scripts/smoke_docker_examples.sh
```

Push release tags only when the GHCR package exists and the maintainer account
has package-write permission:

```bash
docker/build-base.sh --push
```

Maintainers can also publish from GitHub Actions via the `Publish Base Image`
workflow. It builds from `VERSION`, pushes both `<VERSION>` and `latest`, and
verifies a remote pull.

Release checklist:

1. Bump `VERSION` if the base image contract changed.
2. Run `scripts/smoke_dev.sh`.
3. Run changed env tests, for example `cd packages/environments/mock-gdrive && uv run --extra dev pytest tests -q`.
4. Build locally with `docker/build-base.sh`.
5. Run `PULL_BASE=0 scripts/smoke_docker_examples.sh`.
6. Push with `docker/build-base.sh --push` if package permissions are configured,
   or run the `Publish Base Image` workflow.
7. Validate remote pull with `docker pull ghcr.io/benchflow-ai/env0:$(cat VERSION)` only after the push succeeds.

## Repo Layout

```text
env0/
├── packages/environments/mock-gmail/
├── packages/environments/mock-gcal/
├── packages/environments/mock-gdoc/
├── packages/environments/mock-gdrive/
├── packages/environments/mock-slack/
├── docker/
├── devhub/
├── docs/
├── example_tasks/
├── env0-mobile/
│   ├── tasks-eval/
│   ├── tasks-train/
│   └── tasks-train-mini/
├── tasks/
├── scripts/
├── tests/
├── config.toml
└── VERSION
```

## Runtime Contracts

- Service metadata comes from `config.toml`.
- Service ids and CLIs are canonical `mock-*` names.
- Service URLs use canonical `MOCK_*_URL` env vars.
- Task service declaration uses `task.toml [environment] services = [...]`.
- Task Dockerfiles are thin and inherit from `ghcr.io/benchflow-ai/env0:<VERSION>`.
- Hidden task payload lives under `/var/lib/task`.
- Task-aware seeding uses internal `--task-data` + `--task-name` plumbing.
- Dev/user UX stays task-name based: `scripts/dev.sh task <name>`.

Current implementation note: `config.toml` is the source of truth for runtime
metadata, but `scripts/smoke_docker_examples.sh` and `docker/gws-wrapper.sh`
still contain small service maps and must be kept in sync when adding services.

## Docs

- [Docs index](docs/README.md)
- [Local dev and devhub](docs/dev.md)
- [Good first contributions](docs/good-first-contributions.md)
- [Adding a new environment](docs/adding-new-environment.md)
- [API validation playbook](docs/api-validation-playbook.md)
- [Parity audit](docs/parity-audit/README.md)
- [Validated workflows](docs/validated-workflows.md)
- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)

## Example Tasks

`example_tasks/` currently covers:

- `email-confidential-forward`
- `gdoc-search-keyword-index`
- `gdrive-archive-stale-drafts`
- `multi-mail-cal-sync`
- `multi-misread-approval-scope`

These examples are env0 fixtures/templates, not source-of-truth task
definitions.

## Imported BenchFlow Tasks

`tasks/` is intentionally kept as the small public/env0 task reference set.
The standard 60-task env-0 evaluation set lives under
`env0-mobile/tasks-eval/`.

`env0-mobile/` contains:

- `tasks-eval/`: 60 standard eval tasks copied from `benchflow-ai/env-0/tasks`.
- `tasks-train/`: 1703 real task directories copied from the upstream env-0
  mobile training corpus.
- `tasks-train-mini/`: 300 real task directories copied from the upstream
  strong-model-verified mobile corpus.

## License

env0 is licensed under the GNU Affero General Public License v3.0 only
(`AGPL-3.0-only`). See [LICENSE](LICENSE).

You may self-host, use, modify, and redistribute env0 under the terms of
the AGPL. BenchFlow also offers an official hosted env0 service.
