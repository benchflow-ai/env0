FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env0-mobile/tasks-eval/multi-mail-slack-invite/data /tasks/multi-mail-slack-invite/data
ENV TASKS_DIR=/tasks

# Seed Gmail with SkillsBench contributor emails
RUN gmail --db /data/gmail.db seed --scenario task:multi-mail-slack-invite

# Seed Slack with contributor users (channels to be created by agent)
RUN slack --db /data/slack.db seed --scenario task:multi-mail-slack-invite

RUN command -v gosu >/dev/null 2>&1 || (apt-get update && apt-get install -y --no-install-recommends gosu && rm -rf /var/lib/apt/lists/*)
RUN id agent 2>/dev/null || useradd -m -s /bin/bash agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Lock all sensitive directories (root-only access)
RUN chown agent:agent /logs/agent /logs/artifacts

# Mock Slack tokens for the agent
ENV SLACK_BOT_TOKEN=mock-bot-token
ENV SLACK_USER_TOKEN=mock-user-token
