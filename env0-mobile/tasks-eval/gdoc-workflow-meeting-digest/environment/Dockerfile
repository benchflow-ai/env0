FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY env0-mobile/tasks-eval/gdoc-workflow-meeting-digest/data /tasks/gdoc-workflow-meeting-digest/data
ENV TASKS_DIR=/tasks

# gdrive seeds first (metadata + content authority, includes filler)
RUN gdrive --db /data/gdrive.db seed --scenario task:gdoc-workflow-meeting-digest
# gdoc mirrors gdrive (derives body_json from content_text)
RUN gdoc --db /data/gdoc.db seed --from-gdrive /data/gdrive.db

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
