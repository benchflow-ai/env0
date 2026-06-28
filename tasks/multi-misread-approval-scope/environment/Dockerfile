FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY tasks/multi-misread-approval-scope/data /tasks/multi-misread-approval-scope/data
ENV TASKS_DIR=/tasks

RUN slack --db /data/slack.db seed --scenario task:multi-misread-approval-scope
RUN gmail --db /data/gmail.db seed --scenario task:multi-misread-approval-scope
RUN gdrive --db /data/gdrive.db seed --scenario task:multi-misread-approval-scope
RUN gdoc --db /data/gdoc.db seed --from-gdrive /data/gdrive.db

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts
RUN chown agent:agent /logs/agent /logs/artifacts
