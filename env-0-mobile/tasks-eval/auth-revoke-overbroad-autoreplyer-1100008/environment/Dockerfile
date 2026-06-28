FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env-0-mobile/tasks-eval/auth-revoke-overbroad-autoreplyer-1100008/data /tasks/auth-revoke-overbroad-autoreplyer-1100008/data
ENV TASKS_DIR=/tasks

RUN auth --db /data/auth.db seed --scenario task:auth-revoke-overbroad-autoreplyer-1100008

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
