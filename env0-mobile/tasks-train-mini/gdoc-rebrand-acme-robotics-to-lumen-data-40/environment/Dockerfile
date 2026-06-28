FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env0-mobile/tasks-train-mini/gdoc-rebrand-acme-robotics-to-lumen-data-40/data /tasks/gdoc-rebrand-acme-robotics-to-lumen-data-40/data
ENV TASKS_DIR=/tasks

RUN gdrive --db /data/gdrive.db seed --scenario task:gdoc-rebrand-acme-robotics-to-lumen-data-40
RUN gdoc --db /data/gdoc.db seed --from-gdrive /data/gdrive.db

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
