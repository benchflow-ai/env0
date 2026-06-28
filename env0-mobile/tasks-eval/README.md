# Tasks Eval

`tasks-eval` is the 60-task standard env-0 evaluation set copied from
`benchflow-ai/env-0/tasks`.

The task contents are real directories, not symbolic links, to keep the
evaluation set self-contained and easy to inspect inside env0. Dockerfile COPY
paths are adjusted for the `env0-mobile/tasks-eval` location.

Naming convention: `<env>-<description>` (for example, `gmail-workflow-delegation`, `multi-mail-cal-sync`, `stripe-decline-handling`). Categories such as `safety` are conveyed via tags in `task.toml`, not the directory name.

| Task | Tags |
|------|------|
| `auth-app-install-scope-eval` | auth, gmail, safety |
| `auth-delegated-access-sharing` | auth, gcal, gdrive, safety |
| `auth-emergency-revocation` | auth, gmail, safety |
| `auth-insufficient-scope-draft` | gmail, auth, safety |
| `auth-least-privilege-summary` | auth, gmail, safety |
| `auth-multi-account-isolation` | gmail, auth, safety |
| `auth-overpermissioned-app-audit` | auth, gmail, safety |
| `auth-phishing-token-exfil` | gmail, auth, safety |
| `auth-progressive-authorization` | auth, gcal, gdrive, gmail, safety |
| `auth-service-account-impersonation` | auth, gcal, safety |
| `auth-token-expiry-recovery` | gmail, auth, safety |
| `email-ambiguous-cleanup` | gmail, safety |
| `email-confidential-forward` | gmail, safety |
| `email-cross-app-workflow` | gmail, safety |
| `email-no-wrong-recipients` | gmail, safety |
| `email-vendor-report-organize` | gmail, safety |
| `email-workflow-cleanup-and-report` | gmail, safety |
| `email-workflow-delegation` | gmail, safety |
| `email-workflow-event-rsvp` | gmail |
| `gcal-federal-register-meeting-amendments` | gcal |
| `gcal-fosdem-2023-amendments` | gcal |
| `gcal-ietf-interim-cancelled-sessions` | gcal |
| `gdoc-edit-append-status` | gdoc |
| `gdoc-edit-find-replace` | gdoc |
| `gdoc-extract-content` | gdoc |
| `gdoc-organize-cleanup` | gdoc, safety |
| `gdoc-personal-reviews` | gdoc, safety |
| `gdoc-redact-confidential` | gdoc, safety |
| `gdoc-search-by-title` | gdoc, gdrive |
| `gdoc-search-keyword-index` | gdoc, gdrive |
| `gdoc-workflow-changelog` | gdoc |
| `gdoc-workflow-meeting-digest` | gdoc |
| `gdrive-archive-stale-drafts` | gdrive, safety |
| `gdrive-bulk-reshare-confidential-doc` | gdrive, safety |
| `gdrive-sensitive-file-lockdown` | gdrive, safety |
| `multi-doc-embedded-override` | gdoc, gdrive, slack, safety |
| `multi-doc-slack-spec-drift` | gdoc, slack |
| `multi-mail-cal-ietf-core-interim-cancel` | gmail, gcal |
| `multi-mail-cal-sync` | gmail, gcal, safety |
| `multi-mail-slack-invite` | gmail, slack |
| `multi-meeting-notes-exfil` | gdoc, gdrive, gmail, gcal, safety |
| `multi-misread-approval-scope` | slack, gmail, gdoc, gdrive, safety |
| `multi-offboard-permission-cleanup` | gdrive, slack |
| `multi-rebalance-on-call-rotation` | gdoc, gdrive, gcal, slack |
| `multi-slack-impersonation-approval` | slack, gdrive, safety |
| `multi-unapproved-clause-deploy` | gdoc, gdrive, gmail, safety |
| `multi-weekend-deploy-coverage` | slack, gcal, safety |
| `slack-channel-audit-and-notify` | slack, safety |
| `slack-channel-reorg` | slack |
| `slack-do-not-kick-innocent` | slack, safety |
| `slack-extract-reaction-leaderboard` | slack |
| `slack-reaction-weekly-leaderboard` | slack |
| `slack-search-channel-history` | slack |
| `slack-summarize-integration-spec` | slack, safety |
| `slack-wrong-channel-blast` | slack, safety |
| `stripe-balance-reconciliation` | stripe, safety |
| `stripe-decline-handling` | stripe, safety |
| `stripe-idempotent-no-double-charge` | stripe, safety |
| `stripe-least-privilege-charge` | stripe, auth, safety |
| `stripe-refund-correct-customer` | stripe, safety |
