FROM ghcr.io/benchflow-ai/env-0-base:latest

# Remove config so agent cannot discover the DB path
RUN rm -f /etc/env-0/config.toml /etc/env-0/env.sh

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env-0-mobile/tasks-eval/slack-summarize-integration-spec/data /tasks/slack-summarize-integration-spec/data
ENV TASKS_DIR=/tasks

# Seed the task-specific scenario
RUN slack --db /data/slack.db seed --scenario task:slack-summarize-integration-spec

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
