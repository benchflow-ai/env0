FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY tasks/multi-weekend-deploy-coverage/data /tasks/multi-weekend-deploy-coverage/data
ENV TASKS_DIR=/tasks

RUN slack --db /data/slack.db seed --scenario task:multi-weekend-deploy-coverage
RUN gcal --db /data/gcal.db seed --scenario task:multi-weekend-deploy-coverage

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts
RUN chown agent:agent /logs/agent /logs/artifacts
