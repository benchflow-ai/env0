FROM ghcr.io/benchflow-ai/env-0-base:latest

# Auth wiring — the published base predates auth, so set these explicitly.
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV GMAIL_URL=http://localhost:9001

# Task seed data
COPY env-0-mobile/tasks-eval/auth-least-privilege-summary/data /tasks/auth-least-privilege-summary/data
ENV TASKS_DIR=/tasks

# Seed both services (auth: gws-cli auto-consent; gmail: inbox needles)
RUN auth --db /data/auth.db seed --scenario task:auth-least-privilege-summary
RUN gmail --db /data/gmail.db seed --scenario task:auth-least-privilege-summary

# Create log dirs expected by Harbor verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth (9000) and gmail
# (9001) are started via env-0's pre-agent service hooks, which scan this
# Dockerfile for environment package names registered in config.toml.
