FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env-0-mobile/tasks-eval/gmail-label-loom-receipts-39/data /tasks/gmail-label-loom-receipts-39/data
ENV TASKS_DIR=/tasks

RUN gmail --db /data/gmail.db seed --scenario task:gmail-label-loom-receipts-39

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
