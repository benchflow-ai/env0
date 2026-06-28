FROM ghcr.io/benchflow-ai/env-0-base:latest

# Seed data
COPY env-0-mobile/tasks-eval/slack-extract-reaction-leaderboard/data /tasks/slack-extract-reaction-leaderboard/data
ENV TASKS_DIR=/tasks

RUN slack --db /data/slack.db seed --scenario task:slack-extract-reaction-leaderboard

# Create log dirs expected by Harbor verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
