FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env-0-mobile/tasks-train/multi-invite-to-event-tomas-reyes-handoff-5100006/data /tasks/multi-invite-to-event-tomas-reyes-handoff-5100006/data
ENV TASKS_DIR=/tasks

RUN gcal --db /data/gcal.db seed --scenario task:multi-invite-to-event-tomas-reyes-handoff-5100006
RUN gmail --db /data/gmail.db seed --scenario task:multi-invite-to-event-tomas-reyes-handoff-5100006

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
