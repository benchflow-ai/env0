# Mock GCal API Notes

## Ground Truth

- Official Calendar REST API reference: https://developers.google.com/workspace/calendar/api/v3/reference
- Discovery document: https://www.googleapis.com/discovery/v1/apis/calendar/v3/rest
- Per-resource specs:
  - ACL: https://developers.google.com/workspace/calendar/api/v3/reference/acl
  - CalendarList: https://developers.google.com/workspace/calendar/api/v3/reference/calendarList
  - Calendars: https://developers.google.com/workspace/calendar/api/v3/reference/calendars
  - Channels: https://developers.google.com/workspace/calendar/api/v3/reference/channels
  - Colors: https://developers.google.com/workspace/calendar/api/v3/reference/colors
  - Events: https://developers.google.com/workspace/calendar/api/v3/reference/events
  - FreeBusy: https://developers.google.com/workspace/calendar/api/v3/reference/freebusy
  - Settings: https://developers.google.com/workspace/calendar/api/v3/reference/settings
- Test account for live verification: `fixture-user@example.com`
- Fixture capture script: `scripts/capture_fixtures.py`
- Seed validation script: `scripts/validate_seed.py`
- Endpoint spec: `tests/fixtures/gcal_api_spec.json`
- Coverage map: `tests/fixtures/mock_coverage.json`
- Golden fixtures: `tests/fixtures/real_gcal/`

## API Quirks

Discovered from the imported real Calendar fixtures and validated against the current mock implementation.

- `calendarList.list` returns `nextSyncToken` for the normal list flow, but pagination with `maxResults` should prefer `nextPageToken` and omit `nextSyncToken`.
- Secondary `calendarList` entries omit `primary` and `notificationSettings`; they still include `defaultReminders` and often include `description`.
- `calendars.clear` only works for the primary calendar. Clearing a secondary calendar returns a Google-style `400 Invalid Value`.
- Primary calendars cannot be deleted.
- Mutation responses are relatively sparse but still resource-shaped: calendar/event/acl insert, patch, and update return the mutated resource, not a separate wrapper object.
- `events.import` requires `iCalUID`; missing it should return a Google-style `400` with reason `required`.
- `events.move` returns the moved event in its destination calendar with the original event cancelled in the source calendar.
- `events.watch`, `acl.watch`, and `calendarList.watch` return channel objects without echoing request-only fields like `type` and `address`.
- `channels.stop` is effectively a no-op in the mock. The legacy imported fixture for this endpoint is not trustworthy and is intentionally not used for conformance.
- `freeBusy.query` and `settings.list/get` are shape-sensitive: top-level key sets matter more than exact values.
- `events.list` on the real primary calendar can legitimately return an empty first page with `nextPageToken`; for stable conformance we validate against a non-empty `singleEvents + orderBy + timeMin` variant instead.

## Intentionally Skipped

| Feature | Reason |
|---------|--------|
| Task Docker integration in this pass | Scoped out for a follow-up change |
| Push channel side effects beyond registration bookkeeping | Not needed for current evaluator workflows |
| Calendar `fields` partial-response parameter | Low agent relevance and no current task depends on it |
| Full discovery-schema-to-Pydantic fidelity table | Calendar spec fixture currently tracks endpoint coverage, not a populated schema map |

## Key Design Choices

- Stateful SQLite mock instead of replay-only fixtures so agents can perform multi-step Calendar workflows.
- Golden fixtures are used for response-shape conformance, while `test_api.py` covers behavior and Google-style error semantics.
- Verification framework mirrors the proven Gmail setup: endpoint inventory, coverage map, golden fixtures, capture script, seed validator, and dashboard surfacing.
- Legacy fixtures from the original PR are kept as the initial baseline so we can validate the migrated code immediately, even before refreshing live captures.
- Dashboard coverage is driven from `gcal_api_spec.json` plus `mock_coverage.json`, making completeness visible per Calendar resource.

## Open Questions

- Fresh fixture recapture still requires Calendar OAuth scopes for `fixture-user@example.com`. The workspace currently has a cached gws identity but not the needed encrypted Calendar credentials.
- `channels.stop` should be re-captured with fresh auth because the imported historical artifact looks like a downloaded HTML stub rather than a real Calendar API body.
- Calendar discovery schemas are not yet materialized into `gcal_api_spec.json`; if we want field-level schema fidelity like Gmail, we should enrich that artifact in a follow-up.
- `gws calendar calendarList list` still returns `insufficientPermissions` for this account even after re-auth with calendarList scopes, while `calendarList.get` succeeds. The live capture therefore retains the imported `calendarlist_list.json` baseline.
- `gws calendar events quickAdd` and `gws calendar events move` currently fail with `411 Length Required` because the CLI sends those POSTs without a `Content-Length` header. The imported golden fixtures remain the source of truth for those two endpoints until the CLI behavior is fixed.

## Known Parity Gaps (2026-03-27)

### EventActor sparse serialization (7 conformance test failures with strict=True)

The real Google Calendar API uses sparse serialization for `creator` and `organizer` objects:
- `self`: omitted when `false` (the default). Present as `true` only when the actor matches the calendar owner.
- `displayName`: omitted when the organizer is the primary calendar user. Present when the organizer is a secondary/shared calendar (which has a calendar name).

Our mock always includes `self=true` on GET responses and omits it on mutation responses, which doesn't perfectly match. The real API behavior varies by:
- Response type (GET vs insert vs list)  
- Calendar type (primary vs secondary)
- Whether the actor is the authenticated user

**Impact**: Low. No task evaluator or agent depends on the presence/absence of `creator.self` or `organizer.displayName`. These are metadata fields, not functional.

**To fix**: Implement context-aware serialization in `_to_event_resource()` that tracks whether the event is on the primary calendar and whether it's a mutation response. ~30 LoC.

**Ref**: https://developers.google.com/workspace/calendar/api/v3/reference/events — `creator.self` "defaults to False", `organizer.displayName` "if available".
