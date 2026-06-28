FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env0-mobile/tasks-train-mini/auth-revoke-overbroad-threadweaver-6100012/data /tasks/auth-revoke-overbroad-threadweaver-6100012/data
ENV TASKS_DIR=/tasks

RUN auth --db /data/auth.db seed --scenario task:auth-revoke-overbroad-threadweaver-6100012

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
