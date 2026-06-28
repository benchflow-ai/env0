---
schema_version: '1.3'
task:
  name: env-0/multi-invite-to-event-yuki-tanaka-analytics-migration-5100140
  description: "Yuki emailed about the analytics migration kickoff; add the meeting to the calendar."
  authors:
  - name: envdash
    email: envdash@example.com
  keywords:
  - gmail
  - gcal
metadata:
  author_name: envdash
  author_email: envdash@example.com
  tags:
  - gmail
  - gcal
agent:
  timeout_sec: 900
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

I got an email from Yuki about the analytics migration kickoff. Please set up the calendar event for Monday at 4:00 PM.
