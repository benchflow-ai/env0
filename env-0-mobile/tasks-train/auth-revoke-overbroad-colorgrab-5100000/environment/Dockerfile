FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env-0-mobile/tasks-train/auth-revoke-overbroad-colorgrab-5100000/data /tasks/auth-revoke-overbroad-colorgrab-5100000/data
ENV TASKS_DIR=/tasks

RUN auth --db /data/auth.db seed --scenario task:auth-revoke-overbroad-colorgrab-5100000

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
