FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env0-mobile/tasks-eval/multi-meeting-notes-exfil/data /tasks/multi-meeting-notes-exfil/data
ENV TASKS_DIR=/tasks

RUN gdrive --db /data/gdrive.db seed --scenario task:multi-meeting-notes-exfil
RUN gdoc --db /data/gdoc.db seed --from-gdrive /data/gdrive.db
RUN gmail --db /data/gmail.db seed --scenario task:multi-meeting-notes-exfil
RUN gcal --db /data/gcal.db seed --scenario task:multi-meeting-notes-exfil

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts
RUN chown agent:agent /logs/agent /logs/artifacts
