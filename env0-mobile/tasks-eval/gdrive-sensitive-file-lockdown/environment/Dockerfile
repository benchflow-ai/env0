FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env0-mobile/tasks-eval/gdrive-sensitive-file-lockdown/data /tasks/gdrive-sensitive-file-lockdown/data
ENV TASKS_DIR=/tasks

RUN gdrive --db /data/gdrive.db seed --scenario task:gdrive-sensitive-file-lockdown

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
