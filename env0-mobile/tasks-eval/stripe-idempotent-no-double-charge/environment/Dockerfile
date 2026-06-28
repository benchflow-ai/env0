FROM ghcr.io/benchflow-ai/env-0-base:latest

COPY env0-mobile/tasks-eval/stripe-idempotent-no-double-charge/data /tasks/stripe-idempotent-no-double-charge/data
ENV TASKS_DIR=/tasks

# Seed the scenario (auto-discovered from data/stripe_seed.py via TASKS_DIR).
# db_path matches config.toml [stripe].db_path.
RUN stripe --db /data/stripe.db seed --scenario task:stripe-idempotent-no-double-charge

RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts
