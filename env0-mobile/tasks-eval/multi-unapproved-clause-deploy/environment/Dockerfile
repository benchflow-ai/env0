FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env0-mobile/tasks-eval/multi-unapproved-clause-deploy/data /tasks/multi-unapproved-clause-deploy/data
ENV TASKS_DIR=/tasks

RUN gdrive --db /data/gdrive.db seed --scenario task:multi-unapproved-clause-deploy
RUN gdoc --db /data/gdoc.db seed --from-gdrive /data/gdrive.db
RUN gmail --db /data/gmail.db seed --scenario task:multi-unapproved-clause-deploy

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts
RUN chown agent:agent /logs/agent /logs/artifacts
