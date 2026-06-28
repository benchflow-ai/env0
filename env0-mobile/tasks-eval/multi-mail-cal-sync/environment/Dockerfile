FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (shared needles.py dispatches to per-env modules)
COPY env0-mobile/tasks-eval/multi-mail-cal-sync/data /tasks/multi-mail-cal-sync/data
ENV TASKS_DIR=/tasks

# Seed gmail (emails with meeting arrangements)
RUN gmail --db /data/gmail.db seed --scenario task:multi-mail-cal-sync

# Seed gcal (hectic week + planted events)
RUN gcal --db /data/gcal.db seed --scenario task:multi-mail-cal-sync

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
