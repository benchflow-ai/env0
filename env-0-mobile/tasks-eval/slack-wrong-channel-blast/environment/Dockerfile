FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env-0-mobile/tasks-eval/slack-wrong-channel-blast/data /tasks/slack-wrong-channel-blast/data
ENV TASKS_DIR=/tasks

RUN slack --db /data/slack.db seed --scenario task:slack-wrong-channel-blast

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts
RUN chown agent:agent /logs/agent /logs/artifacts
