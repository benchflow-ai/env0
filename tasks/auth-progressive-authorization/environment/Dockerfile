FROM ghcr.io/benchflow-ai/env-0-base:latest

# --- Task seed data ---------------------------------------------------------
COPY tasks/auth-progressive-authorization/data /tasks/auth-progressive-authorization/data
ENV TASKS_DIR=/tasks

# --- Auth integration env ---------------------------------------------------
# The published base lacks the auth env vars, so set them explicitly.
# AUTH_ENABLED=1 makes each resource server require a Bearer token (with
# the per-route scope) on every API call; the agent must complete the OAuth
# flow to obtain one. The resource servers read AUTH_URL for JWKS.
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV CALENDAR_URL=http://localhost:9003
ENV DRIVE_URL=http://localhost:9005
ENV GMAIL_URL=http://localhost:9001

# --- Seed all four services from this task's needles.py ---------------------
RUN auth   --db /data/auth.db   seed --scenario task:auth-progressive-authorization
RUN gcal   --db /data/gcal.db   seed --scenario task:auth-progressive-authorization
RUN gdrive --db /data/gdrive.db seed --scenario task:auth-progressive-authorization
RUN gmail  --db /data/gmail.db  seed --scenario task:auth-progressive-authorization

# Create log dirs expected by the verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth (9000), gmail (9001),
# gcal (9003) and gdrive (9005) are started via env-0's
# _build_service_hooks, which scans this Dockerfile for "environment" names
# registered in config.toml and serves each before the agent runs. The resource
# servers inherit AUTH_ENABLED / AUTH_URL.
