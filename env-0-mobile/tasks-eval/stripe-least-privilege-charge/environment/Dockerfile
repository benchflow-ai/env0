FROM ghcr.io/benchflow-ai/env-0-base:latest

# --- Task seed data ---------------------------------------------------------
COPY env-0-mobile/tasks-eval/stripe-least-privilege-charge/data /tasks/stripe-least-privilege-charge/data
ENV TASKS_DIR=/tasks

# --- Auth integration env ---------------------------------------------------
# The published base lacks the auth env vars, so set them explicitly.
# AUTH_ENABLED=1 makes the stripe server require a Bearer auth JWT on
# every /v1 call; the agent must obtain a scoped token to charge. The issuer
# defaults to http://localhost:9000 (auth's port), which matches
# AUTH_URL below — so the stripe middleware trusts the JWTs auth mints.
ENV AUTH_ENABLED=1
ENV AUTH_URL=http://localhost:9000
ENV STRIPE_URL=http://localhost:9007

# --- Seed both services -----------------------------------------------------
# stripe uses its built-in `default` dataset (Ada/Grace/Alan + history).
# auth uses this task's needles.py (AUTH_CONSENTS auto-consents user1 ->
# stripe-agent for the full stripe.* set).
RUN stripe --db /data/stripe.db seed --scenario default
RUN auth --db /data/auth.db seed --scenario task:stripe-least-privilege-charge

# Create log dirs expected by the verifier/agent
RUN mkdir -p /logs/verifier /logs/agent /logs/artifacts

# Grant agent write access to its log dirs (env source lives in env-0-base)
RUN chown agent:agent /logs/agent /logs/artifacts

# NOTE: Daytona doesn't run CMD/ENTRYPOINT. auth (port 9000) and
# stripe (port 9007) are started via env-0's _build_service_hooks,
# which scans this Dockerfile for "environment" names registered in config.toml and
# serves each before the agent runs. The stripe server inherits
# AUTH_ENABLED / AUTH_URL.
