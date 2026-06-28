FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env0-mobile/tasks-eval/multi-mail-cal-ietf-core-interim-cancel/data /tasks/multi-mail-cal-ietf-core-interim-cancel/data
ENV TASKS_DIR=/tasks

RUN gmail --db /data/gmail.db seed --scenario task:multi-mail-cal-ietf-core-interim-cancel
RUN gcal --db /data/gcal.db seed --scenario task:multi-mail-cal-ietf-core-interim-cancel

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
