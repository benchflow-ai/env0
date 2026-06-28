FROM ghcr.io/benchflow-ai/env-0-base:latest

# Auth wiring — the published base sets service URL only for the older envs,
# so set the auth-related env vars explicitly.
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV GMAIL_URL=http://localhost:9001

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY tasks/auth-emergency-revocation/data /tasks/auth-emergency-revocation/data
ENV TASKS_DIR=/tasks

# Seed auth (users + 6 clients + 6 consents from this task's needles.py),
# then run the session hook to mint one real access token per active session
# and write the suspicious-sign-in audit trail for unknown-device-x. Finally
# seed gmail's inbox (security alert + filler) from the same needles.py.
RUN auth --db /data/auth.db seed --scenario task:auth-emergency-revocation
RUN python3 /tasks/auth-emergency-revocation/data/seed_sessions.py /data/auth.db
RUN gmail --db /data/gmail.db seed --scenario task:auth-emergency-revocation

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth and gmail are
# started via env-0's pre-agent service hooks (_build_service_hooks scans
# this Dockerfile for "auth" / "gmail" and serves them on 9000/9001).
