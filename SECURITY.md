# Security Policy

## Reporting A Vulnerability

Please report suspected vulnerabilities privately by emailing security@benchflow.ai.
Include the affected service, commit or version, reproduction steps, impact, and
any logs that do not contain credentials.

Do not open public issues for vulnerabilities involving credential exposure,
authorization bypass, container escape, or access to private task payloads.

## Scope

Security reports are in scope for:

- mock service APIs under `packages/environments/mock-*`
- local launcher and devhub control paths
- task image payload isolation under `/var/lib/task`
- Docker base image build scripts and runtime defaults
- fixture capture scripts that handle live provider credentials

Reports about downstream benchmark scoring policy are usually out of scope for
this repo unless they expose an env0 runtime vulnerability.

## Credential Hygiene

Do not commit OAuth tokens, API keys, real account exports, provider credential
files, or private customer data. Fixture captures must be reviewed and sanitized
before publication.
