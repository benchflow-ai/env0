FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data
COPY env-0-mobile/tasks-eval/auth-insufficient-scope-draft/data /tasks/auth-insufficient-scope-draft/data
ENV TASKS_DIR=/tasks

# The published base image predates auth: set the auth env explicitly.
# (gmail picks up AUTH_ENABLED=1 at server start and enforces OAuth.)
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV GMAIL_URL=http://localhost:9001

# Seed both services at build time
RUN auth --db /data/auth.db seed --scenario task:auth-insufficient-scope-draft
RUN gmail --db /data/gmail.db seed --scenario task:auth-insufficient-scope-draft

# Create log dirs expected by Harbor verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: no CMD/ENTRYPOINT — env-0's service hooks scan this Dockerfile for
# "auth" / "gmail" (config.toml registry) and start both servers as
# background processes before the agent runs.
