FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env-0-mobile/tasks-eval/multi-doc-embedded-override/data /tasks/multi-doc-embedded-override/data
ENV TASKS_DIR=/tasks

# gdrive seeds first (metadata + content + comments + filler)
RUN gdrive --db /data/gdrive.db seed --scenario task:multi-doc-embedded-override
# gdoc mirrors gdrive (derives body_json from content_text)
RUN gdoc --db /data/gdoc.db seed --from-gdrive /data/gdrive.db
RUN slack --db /data/slack.db seed --scenario task:multi-doc-embedded-override

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
