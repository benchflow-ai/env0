FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env0-mobile/tasks-train/gdrive-lock-down-greenfield-confidential-100/data /tasks/gdrive-lock-down-greenfield-confidential-100/data
ENV TASKS_DIR=/tasks

RUN gdrive --db /data/gdrive.db seed --scenario task:gdrive-lock-down-greenfield-confidential-100

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
