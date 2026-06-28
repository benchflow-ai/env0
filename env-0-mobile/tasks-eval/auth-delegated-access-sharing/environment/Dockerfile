FROM ghcr.io/benchflow-ai/env-0-base:latest

# --- Task seed data (tests/ + solution/ are uploaded by benchflow) ----------
COPY env-0-mobile/tasks-eval/auth-delegated-access-sharing/data /tasks/auth-delegated-access-sharing/data
ENV TASKS_DIR=/tasks

# --- Auth integration env ---------------------------------------------------
# The published base lacks the auth env vars, so set them explicitly.
# AUTH_ENABLED=1 makes the gcal/gdrive servers require a Bearer token on
# every API call and verify it against auth's JWKS at AUTH_URL.
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV CALENDAR_URL=http://localhost:9003
ENV DRIVE_URL=http://localhost:9005

# --- Seed each service from this task's needles.py --------------------------
RUN auth --db /data/auth.db seed --scenario task:auth-delegated-access-sharing
RUN gcal --db /data/gcal.db seed --scenario task:auth-delegated-access-sharing
# Post-seed augmentation: create user1's "Project Plans" calendar (not a built-in
# gcal template) and re-snapshot the gcal "initial" baseline.
RUN python3 /tasks/auth-delegated-access-sharing/data/seed_gcal_extra.py /data/gcal.db
RUN gdrive --db /data/gdrive.db seed --scenario task:auth-delegated-access-sharing

# Create log dirs expected by the verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth (9000), gcal (9003)
# and gdrive (9005) are started via env-0's _build_service_hooks, which
# scans this Dockerfile for "environment" names registered in config.toml and serves
# each (inheriting AUTH_ENABLED / AUTH_URL) before the agent runs.
