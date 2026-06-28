FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env0-mobile/tasks-eval/gdrive-archive-stale-drafts/data /tasks/gdrive-archive-stale-drafts/data
ENV TASKS_DIR=/tasks

RUN gdrive --db /data/gdrive.db seed --scenario task:gdrive-archive-stale-drafts

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

RUN chown agent:agent /logs/agent /logs/artifacts
