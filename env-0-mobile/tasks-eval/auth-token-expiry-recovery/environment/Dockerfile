FROM ghcr.io/benchflow-ai/env-0-base:latest

# Auth wiring. The published base image predates auth, so set its env vars
# here. AUTH_ENABLED=1 turns on Bearer-JWT enforcement in gmail.
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV GMAIL_URL=http://localhost:9001

# Seed data
COPY env-0-mobile/tasks-eval/auth-token-expiry-recovery/data /tasks/auth-token-expiry-recovery/data
ENV TASKS_DIR=/tasks

RUN auth --db /data/auth.db seed --scenario task:auth-token-expiry-recovery
RUN gmail --db /data/gmail.db seed --scenario task:auth-token-expiry-recovery

# Create log dirs expected by Harbor verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth (port 9000) and
# gmail (port 9001) are started by env-0's service hooks
# (backend.py _build_service_hooks), which scan this Dockerfile for environment
# package names registered in config.toml.
