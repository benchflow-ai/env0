FROM ghcr.io/benchflow-ai/env-0-base:latest

# The published base image predates auth, so it does not set the auth
# env vars from config.toml — set them explicitly (GMAIL_URL re-stated
# for symmetry; same value the base derives from config.toml).
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV GMAIL_URL=http://localhost:9001

# Task seed data
COPY tasks/auth-multi-account-isolation/data /tasks/auth-multi-account-isolation/data
ENV TASKS_DIR=/tasks

# Seed auth: base users (user1/user2) + AUTH_USERS (user_101) +
# AUTH_CLIENTS (work-client/personal-client) + AUTH_CONSENTS from needles.py.
RUN auth --db /data/auth.db seed --scenario task:auth-multi-account-isolation

# Seed gmail: work mailbox (user1) with the contract needles + filler.
RUN gmail --db /data/gmail.db seed --scenario task:auth-multi-account-isolation

# The gmail task seeder only seeds the primary work user. Add the personal
# account (user_101, alex.personal@gmail.local) using the env-owned fixture
# from the `multi_account` scenario, then refresh the "initial" snapshot so
# /_admin/diff stays empty pre-agent.
RUN python3 /tasks/auth-multi-account-isolation/data/seed_personal_account.py /data/gmail.db

# Create log dirs expected by Harbor verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth and gmail are
# started via env-0's pre-agent service hooks (_build_service_hooks scans
# this Dockerfile for environment names registered in config.toml).
