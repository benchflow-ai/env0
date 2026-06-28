FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY tasks/gdrive-bulk-reshare-confidential-doc/data /tasks/gdrive-bulk-reshare-confidential-doc/data
ENV TASKS_DIR=/tasks

RUN gdrive --db /data/gdrive.db seed --scenario task:gdrive-bulk-reshare-confidential-doc

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts
RUN chown agent:agent /logs/agent /logs/artifacts
