# Mockflow

Mockflow contains first-party mock environments for local agent testing and
API-parity workflows. It owns local env development, seed contracts, dev
tooling, API parity checks, and the shared Docker base image.

`example_tasks/` are fixtures and templates used to prove mockflow runtime
contracts. Benchmark scoring and canonical task authoring stay outside this
repo.

## Quick Start

Run commands from the `mockflow` repo root. Prerequisites:

- Python 3.12+
- `uv`
- Docker daemon for Docker/base-image smoke checks
- free local ports `9001`-`9005` and `9060`

Run the unit/control smoke:

```bash
scripts/smoke_dev.sh
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

The shared base image is published as:

```text
kywch/mockflow:0.1.0
```

`VERSION` is the source of truth for the semver tag. Task Dockerfiles should
pin `FROM kywch/mockflow:<VERSION>`. `latest` may exist as a convenience alias,
but task Dockerfiles should not depend on it.

Build and push:

```bash
docker/build-base.sh --push
```

Release checklist:

1. Bump `VERSION` if the base image contract changed.
2. Run `scripts/smoke_dev.sh`.
3. Run changed env tests, for example `cd packages/environments/mock-gdrive && uv run --extra dev pytest tests -q`.
4. Build locally with `docker/build-base.sh`.
5. Run `scripts/smoke_docker_examples.sh`.
6. Push with `docker/build-base.sh --push`.
7. Validate remote pull with `docker pull kywch/mockflow:$(cat VERSION)`.

Validate all example Dockerfiles against the published base:

```bash
scripts/smoke_docker_examples.sh
```

For faster local reruns:

```bash
PULL_BASE=0 scripts/smoke_docker_examples.sh
```

## Repo Layout

```text
mockflow/
├── packages/environments/mock-gmail/
├── packages/environments/mock-gcal/
├── packages/environments/mock-gdoc/
├── packages/environments/mock-gdrive/
├── packages/environments/mock-slack/
├── docker/
├── devhub/
├── docs/
├── example_tasks/
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
- Task Dockerfiles are thin and inherit from `kywch/mockflow:<VERSION>`.
- Hidden task payload lives under `/var/lib/task`.
- Task-aware seeding uses internal `--task-data` + `--task-name` plumbing.
- Dev/user UX stays task-name based: `scripts/dev.sh task <name>`.

Current implementation note: `config.toml` is the source of truth for runtime
metadata, but `scripts/smoke_docker_examples.sh` and `docker/gws-wrapper.sh`
still contain small service maps and must be kept in sync when adding services.

## Docs

- [Local dev and devhub](docs/dev.md)
- [Adding a new environment](docs/adding-new-environment.md)
- [API validation playbook](docs/api-validation-playbook.md)
- [Parity audit](docs/parity-audit/README.md)

## Example Tasks

`example_tasks/` currently covers:

- `email-confidential-forward`
- `gdoc-search-keyword-index`
- `gdrive-archive-stale-drafts`
- `multi-mail-cal-sync`
- `multi-misread-approval-scope`

These examples are mockflow fixtures/templates, not source-of-truth task
definitions.

## License

Mockflow is licensed under the GNU Affero General Public License v3.0 only
(`AGPL-3.0-only`). See [LICENSE](LICENSE).

You may self-host, use, modify, and redistribute Mockflow under the terms of
the AGPL. BenchFlow also offers an official hosted Mockflow service.
