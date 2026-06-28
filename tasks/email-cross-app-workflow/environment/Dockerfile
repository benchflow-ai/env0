FROM ghcr.io/benchflow-ai/env-0-base:latest

# Seed data
COPY tasks/email-cross-app-workflow/data /tasks/email-cross-app-workflow/data
ENV TASKS_DIR=/tasks

RUN gmail --db /data/gmail.db seed --scenario task:email-cross-app-workflow

# Create log dirs expected by Harbor verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. gmail is started via
# harbor_runner.py's AGENT_START hook (see _add_direct_mode_hook).
