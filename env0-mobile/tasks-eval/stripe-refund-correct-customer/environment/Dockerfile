FROM ghcr.io/benchflow-ai/env-0-base:latest

# --- Task seed data ---------------------------------------------------------
COPY env0-mobile/tasks-eval/stripe-refund-correct-customer/data /tasks/stripe-refund-correct-customer/data
ENV TASKS_DIR=/tasks

# No auth: this is a capability+safety task on the legacy disabled-mode key
# (sk_test_env_0_51deterministic). AUTH_ENABLED stays unset so the seeded
# test key is the credential.

# --- Seed the mock Stripe account from this task's stripe_seed.py ------------
RUN stripe --db /data/stripe.db seed --scenario task:stripe-refund-correct-customer

# Create log dirs expected by the verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. stripe (port 9007) is started
# via env-0's _build_service_hooks, which scans this Dockerfile for "environment"
# names registered in config.toml and serves each before the agent runs.
