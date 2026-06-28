FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env0-mobile/tasks-train/gcal-cancel-falcon-5100020/data /tasks/gcal-cancel-falcon-5100020/data
ENV TASKS_DIR=/tasks

RUN gcal --db /data/gcal.db seed --scenario task:gcal-cancel-falcon-5100020

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
