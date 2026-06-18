# Imported env-0 Tasks

This directory contains a selected set of BenchFlow-native task packages copied
from `benchflow-ai/env-0`.

These tasks intentionally keep their original `env-0` runtime contract:

- `task.md` uses BenchFlow `schema_version: '1.3'`.
- `environment/Dockerfile` uses `ghcr.io/benchflow-ai/env-0-base:latest`.
- `tasks/_manifests/env-0.toml` declares the env-0 service plane.

They are not wired into `example_tasks/`, which remain env0's local runtime
fixtures for mock service development.
