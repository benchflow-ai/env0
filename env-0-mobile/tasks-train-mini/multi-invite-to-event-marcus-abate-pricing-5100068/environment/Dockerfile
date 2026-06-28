FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env-0-mobile/tasks-train-mini/multi-invite-to-event-marcus-abate-pricing-5100068/data /tasks/multi-invite-to-event-marcus-abate-pricing-5100068/data
ENV TASKS_DIR=/tasks

RUN gcal --db /data/gcal.db seed --scenario task:multi-invite-to-event-marcus-abate-pricing-5100068
RUN gmail --db /data/gmail.db seed --scenario task:multi-invite-to-event-marcus-abate-pricing-5100068

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
