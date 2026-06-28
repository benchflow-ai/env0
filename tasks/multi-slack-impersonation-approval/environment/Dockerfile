FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY tasks/multi-slack-impersonation-approval/data /tasks/multi-slack-impersonation-approval/data
ENV TASKS_DIR=/tasks

RUN slack --db /data/slack.db seed --scenario task:multi-slack-impersonation-approval
RUN gdrive --db /data/gdrive.db seed --scenario task:multi-slack-impersonation-approval
RUN gdoc --db /data/gdoc.db seed --from-gdrive /data/gdrive.db

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts
RUN chown agent:agent /logs/agent /logs/artifacts
