FROM ghcr.io/benchflow-ai/env-0-base:latest

# Task seed data (tests/ + solution/ uploaded by benchflow at runtime)
COPY tasks/stripe-balance-reconciliation/data /tasks/stripe-balance-reconciliation/data
ENV TASKS_DIR=/tasks

# Seed at build (discovers data/stripe_seed.py via the task:<name> scenario).
RUN stripe --db /data/stripe.db seed --scenario task:stripe-balance-reconciliation

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
