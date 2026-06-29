FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env0-mobile/tasks-eval/slack-channel-audit-and-notify/data /tasks/slack-channel-audit-and-notify/data
ENV TASKS_DIR=/tasks

RUN slack --db /data/slack.db seed --scenario task:slack-channel-audit-and-notify

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# Mock Slack tokens for the agent
ENV SLACK_BOT_TOKEN=mock-bot-token
ENV SLACK_USER_TOKEN=mock-user-token
