---
schema_version: '1.3'
task:
  name: env-0/gdoc-rebrand-cinder-security-to-drift-mobility-2
  description: "We just rebranded from \"Cinder Security\" to \"Drift Mobility\"."
  authors:
  - name: envdash
    email: envdash@example.com
  keywords:
  - gdoc
metadata:
  author_name: envdash
  author_email: envdash@example.com
  tags:
  - gdoc
agent:
  timeout_sec: 600
verifier:
  timeout_sec: 120
environment:
  cpus: 1
  memory_mb: 2048
  network_mode: public
  build_timeout_sec: 600
  os: linux
  storage_mb: 10240
  gpus: 0
  mcp_servers: []
  env: {}
benchflow:
  environment:
    manifest: ../_manifests/env-0.toml
---

## prompt

We finished the rename from "Cinder Security" to "Drift Mobility". Please find every doc that still says the old name and fix it.
