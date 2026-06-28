FROM ghcr.io/benchflow-ai/env-0-base:latest

# --- Task seed data ---------------------------------------------------------
COPY env-0-mobile/tasks-eval/auth-service-account-impersonation/data /tasks/auth-service-account-impersonation/data
ENV TASKS_DIR=/tasks

# --- Auth integration env ---------------------------------------------------
# The published base lacks the auth env vars, so set them explicitly.
# AUTH_ENABLED=1 makes the gcal server require a Bearer token on every
# /calendar/v3 call; the agent must mint a service-account token to create the
# event. CALENDAR_URL is gcal's own env var (see config.toml).
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV CALENDAR_URL=http://localhost:9003

# --- Seed both services from this task's needles.py -------------------------
RUN auth --db /data/auth.db seed --scenario task:auth-service-account-impersonation
RUN gcal --db /data/gcal.db seed --scenario task:auth-service-account-impersonation

# Create log dirs expected by the verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth (port 9000) and gcal
# (port 9003) are started via env-0's _build_service_hooks, which scans this
# Dockerfile for "environment" names registered in config.toml and serves each before
# the agent runs. The gcal server inherits AUTH_ENABLED / AUTH_URL.
