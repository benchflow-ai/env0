FROM ghcr.io/benchflow-ai/env-0-base:latest

# Auth wiring — the published base sets service URL only for the older envs,
# so set the auth-related env vars explicitly.
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV GMAIL_URL=http://localhost:9001

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env0-mobile/tasks-eval/auth-overpermissioned-app-audit/data /tasks/auth-overpermissioned-app-audit/data
ENV TASKS_DIR=/tasks

# Seed both services from this task's needles.py
RUN auth --db /data/auth.db seed --scenario task:auth-overpermissioned-app-audit
RUN gmail --db /data/gmail.db seed --scenario task:auth-overpermissioned-app-audit

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth and gmail are
# started via env-0's pre-agent service hooks (_build_service_hooks scans
# this Dockerfile for "auth" / "gmail" and serves them on 9000/9001).
