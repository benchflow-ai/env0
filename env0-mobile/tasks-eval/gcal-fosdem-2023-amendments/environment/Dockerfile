FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env0-mobile/tasks-eval/gcal-fosdem-2023-amendments/data /tasks/gcal-fosdem-2023-amendments/data
ENV TASKS_DIR=/tasks

RUN gcal --db /data/gcal.db seed --scenario task:gcal-fosdem-2023-amendments

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

RUN chown agent:agent /logs/agent /logs/artifacts
