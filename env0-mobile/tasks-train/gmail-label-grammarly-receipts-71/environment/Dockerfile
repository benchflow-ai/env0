FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env0-mobile/tasks-train/gmail-label-grammarly-receipts-71/data /tasks/gmail-label-grammarly-receipts-71/data
ENV TASKS_DIR=/tasks

RUN gmail --db /data/gmail.db seed --scenario task:gmail-label-grammarly-receipts-71

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
