FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env-0-mobile/tasks-eval/gcal-ietf-interim-cancelled-sessions/data /tasks/gcal-ietf-interim-cancelled-sessions/data
ENV TASKS_DIR=/tasks

RUN gcal --db /data/gcal.db seed --scenario task:gcal-ietf-interim-cancelled-sessions

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

RUN chown agent:agent /logs/agent /logs/artifacts
