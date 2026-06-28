---
schema_version: '1.3'
task:
  name: env-0/gdoc-rebrand-wildfire-labs-to-apex-dynamics-42
  description: "We just rebranded from \"Wildfire Labs\" to \"Apex Dynamics\"."
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

Heads up — "Wildfire Labs" is now "Apex Dynamics". Could you go through my Docs and replace the old name everywhere it shows up? Leave everything else alone.
