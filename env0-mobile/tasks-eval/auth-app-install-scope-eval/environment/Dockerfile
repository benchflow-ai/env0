FROM ghcr.io/benchflow-ai/env-0-base:latest

# --- Task seed data ---------------------------------------------------------
COPY env0-mobile/tasks-eval/auth-app-install-scope-eval/data /tasks/auth-app-install-scope-eval/data
ENV TASKS_DIR=/tasks

# --- Auth integration env ---------------------------------------------------
# The published base lacks the auth env vars, so set them explicitly.
# AUTH_ENABLED=1 makes the gmail server require a Bearer token on every
# /gmail/v1 call; the agent must complete the OAuth flow to obtain one.
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV GMAIL_URL=http://localhost:9001

# --- Seed both services from this task's needles.py -------------------------
RUN auth --db /data/auth.db seed --scenario task:auth-app-install-scope-eval
RUN gmail --db /data/gmail.db seed --scenario task:auth-app-install-scope-eval

# Create log dirs expected by the verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth (port 9000) and gmail
# (port 9001) are started via env-0's _build_service_hooks, which scans this
# Dockerfile for "environment" names registered in config.toml and serves each before
# the agent runs. The gmail server inherits AUTH_ENABLED / AUTH_URL.
