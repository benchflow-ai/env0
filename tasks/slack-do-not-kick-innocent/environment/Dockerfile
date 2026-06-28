FROM ghcr.io/benchflow-ai/env-0-base:latest

# Seed data
COPY tasks/slack-do-not-kick-innocent/data /tasks/slack-do-not-kick-innocent/data
ENV TASKS_DIR=/tasks

RUN slack --db /data/slack.db seed --scenario task:slack-do-not-kick-innocent

# Create log dirs expected by Harbor verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
