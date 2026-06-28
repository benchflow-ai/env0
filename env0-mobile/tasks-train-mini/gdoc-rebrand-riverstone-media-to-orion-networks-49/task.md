---
schema_version: '1.3'
task:
  name: env-0/gdoc-rebrand-riverstone-media-to-orion-networks-49
  description: "We just rebranded from \"Riverstone Media\" to \"Orion Networks\"."
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

We just rebranded from "Riverstone Media" to "Orion Networks". Can you update all my Google Docs and swap out every mention of the old name? Don't change anything else.
