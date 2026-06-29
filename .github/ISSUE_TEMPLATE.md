## Summary

Describe the env0 behavior, documentation gap, or mock-service issue.

## Reproduction Or Proposal

For bugs, include exact commands, task names, services, and relevant output.
For proposals, describe the mock API, seed, Docker, devhub, or documentation
change and why it belongs in env0.

## Validation

List any checks already run, for example:

- `scripts/smoke_dev.sh`
- `cd packages/environments/mock-gdrive && uv run --extra dev pytest tests -q`
- `docker/build-base.sh`
- `PULL_BASE=0 scripts/smoke_docker_examples.sh`

## Notes

Do not include credentials, OAuth tokens, live account exports, customer data, or
security-sensitive details. Report vulnerabilities privately through
`SECURITY.md`.
