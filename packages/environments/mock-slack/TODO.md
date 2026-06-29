# mock-slack: API Validation TODO

Based on the [API Validation Playbook](../../../docs/api-validation-playbook.md). Reference implementation: mock-gmail.

---

## Phase 0: Gather Prerequisites

- [x] 0a. Identify the mock (FastAPI, 42 endpoints, `mock_slack/api/`)
- [x] 0b. Get access to the real Slack API (test workspace, bot token or OAuth app)
- [x] 0c. Golden fixtures — 19 exist in `tests/fixtures/real_slack/`, but coverage gaps (19/42 endpoints)
- [x] 0d. API documentation — `slack_api_spec.json` exists; no `API_NOTES.md` yet

## Phase 1: Inventory and Capture

- [x] 1.1 Build endpoint inventory with fixture gap analysis → `tests/fixtures/mock_coverage.json`
  - 41 implemented endpoints, 11 with fixtures (27% coverage)
  - 30 endpoints need fixtures (see mock_coverage.json for full list)
  - Shape-changing params noted per endpoint
- [x] 1.2 Write `scripts/slack_auth.py` — authenticate with real Slack API
- [x] 1.3 Write `scripts/capture_fixtures.py` — capture golden fixtures from real workspace
  - Cover all 42 implemented endpoints
  - Capture mutation responses (archive, unarchive, rename, invite, kick, join, leave, etc.)
  - Capture empty-collection states
  - Capture pagination responses (cursor-based)
  - Add `_captured_at` timestamps to all fixtures
  - Generate `_capture_metadata.json`
- [x] 1.4 Capture missing fixtures (priority targets):
  - `conversations.archive` / `unarchive` / `rename` / `invite` / `kick` / `join` / `leave` responses
  - `conversations.setPurpose` / `setTopic` responses
  - `conversations.replies` response
  - `chat.postEphemeral` response
  - `chat.update` / `chat.delete` responses
  - `files.upload` / `files.info` / `files.delete` responses
  - `reminders.list` response
  - `apps.list` response (if available)
  - `users.profile.set` / `users.setPresence` / `users.getPresence` responses
  - Empty channel list, empty search results

## Phase 2: Compare

- [x] 2.1 Key-set comparison for all endpoints with fixtures
  - Run `set(real.keys()) vs set(mock.keys())` at every nesting level
  - Check nested structures (message attachments, blocks, file objects)
  - 63 tests written, 38 failures = 38 mismatches documented (see fidelity report below)
- [x] 2.2 Value-type comparison
  - Timestamp formats (Slack uses epoch seconds as strings, e.g., `"1234567890.123456"`)
  - Boolean vs string representations
  - `null` vs absent keys
  - 21 tests written, 7 failures (all Bug 2 — null vs absent on MessageSchema optional fields)
- [x] 2.3 Subtype and default checks
  - Channel types (public, private, DM, group DM, shared)
  - Bot users vs human users vs app users
  - File types (uploaded, shared, external)
  - 20 tests written, 5 failures (see fidelity report below)
- [x] 2.4 Nested structure check
  - Message `blocks` array: type/block_id/elements, rich_text_section shape, text/emoji leaf elements (all from fixtures ✓)
  - Mock missing blocks entirely (Bug 9) — `test_mock_history_messages_missing_blocks` FAILS
  - `bot_profile` object: id/app_id/user_id/name/icons/deleted/updated/team_id (from fixtures ✓); mock missing it (Bug 9) — `test_mock_postmessage_missing_bot_profile` FAILS
  - `language` object: locale/is_reliable (from fixtures ✓); mock missing it (Bug 9) — `test_mock_history_messages_missing_language` FAILS
  - File object: shares{}/channels[]/groups[]/ims[]/user_team/file_access (Bug 9) — `test_mock_file_missing_nested_fields` FAILS
  - Thread parent fields: reply_users_count/latest_reply/reply_users/is_locked/subscribed (fixture ✓); mock missing (Bug 9)
  - Reply messages: parent_user_id present in real fixture ✓; mock missing (Bug 9)
  - 54 tests written: 6 failed (new Bug 9 mock mismatches) · 45 passed · 3 skipped
- [x] 2.5 Behavioral/semantic check
  - Archive → is_archived=True in conversations.info ✓; blocks postMessage with is_archived error ✓
  - Unarchive → reverts is_archived=False ✓; double-archive returns already_archived ✓
  - Archived channel history still readable ✓
  - Join → user added to members ✓; join private returns is_private ✓
  - Leave → user removed from members ✓; num_members reflects join ✓
  - Invite → user in members ✓; unknown user returns user_not_found ✓
  - Kick → user removed from members ✓; non-member kick returns not_in_channel ✓
  - Delete → message gone from history ✓; returns channel+ts ✓; unknown ts returns message_not_found ✓
  - Update → new text in history ✓; edited.ts set in history ✓
  - Delete → clears associated reactions ✓
  - Reply → increments parent reply_count ✓; reply appears in conversations.replies ✓
  - Reply → does not appear in channel history ✓; unknown thread_ts returns thread_not_found ✓
  - Delete reply → decrements parent reply_count ✓
  - All behavioral tests pass (mock state management is correct)

## Phase 3: Report and Fix

- [x] 3.1 Document mismatches with bug class and severity in this tracker and `API_NOTES.md`
- [x] 3.2 Fix high-severity mismatches
  - Bug 2: `MessageSchema.model_config = ConfigDict(exclude_none=True)` — 7 null-vs-absent fixed ✓
  - Bug 1: `warning` + `response_metadata` on all 18+ write endpoints ✓
  - Bug 10: IM channels no longer bleed into `conversations.list?types=public_channel` ✓
  - Bug 3: `setTopic`/`setPurpose` return full `ConversationInfoResponse` ✓
  - Bug 9: `ChannelSchema` expanded from 11 → 30+ fields ✓
  - Bug 9: `UserSchema` expanded from 8 → 20+ fields ✓
  - Bug 9: Messages now include `blocks`, `team`, `language` ✓
  - Bug 7: IM channels use `IMChannelSchema` (correct shape) ✓
  - Bug 31-34: Nested blocks/bot_profile/language/thread fields now present ✓
  - Bug 35: `FileSchema` expanded with 20+ missing fields ✓
- [x] 3.3 Fix medium-severity mismatches
  - Bug 5: `users.getPresence` returns only `{ok, presence}` ✓
  - Bug 5: `conversations.history` has `pin_count`, `channel_actions_ts`, `channel_actions_count` ✓
  - Bug 5: `conversations.kick` has `errors: {}` ✓
  - Bug 7: USLACKBOT `is_bot=False` (fixed in seed) ✓
  - Bug 5: `search.messages` matches have `team`, `score`, `db_message`, `blocks` ✓
  - Bug 5: `auth.test` has `enterprise_id`, `is_enterprise_install` ✓
  - Bug 5: `users.list` has `cache_ts` ✓
  - Bug 9: `team.info` expanded with 11 missing fields ✓
  - Bug 5: `files.upload`/`files.info` have `timestamp` field ✓
  - Bug 7: USLACKBOT profile has `always_active: true` ✓
  - Bug 1: `chat.postMessage.message` has `bot_id`, `app_id`, `team`, `blocks` ✓
  - Bug 1: `chat.update` has `message` object + `warning`/`response_metadata` ✓
  - Bug 1: `files.info` has `comments` + `response_metadata` ✓
  - Bug 5: `UserProfileSchema` expanded with normalized/image fields ✓
- [x] 3.4 Expand `test_conformance.py` for any new fixtures — no new fixtures needed; all conformance tests now pass
- [x] 3.5 Fix remaining skipped tests (was 4 skipped → 0 skipped)
  - Bug 9: `conversations.replies` thread parents now include `is_locked`, `subscribed`, `latest_reply`, `reply_users`, `reply_users_count` ✓
  - Bug 9: `conversations.replies` reply messages now include `parent_user_id` ✓
  - Fixed thread parent detection in tests (use `reply_count > 0` not `thread_ts == ts`) ✓
  - Fixed `test_join_private_returns_error` to create private channel via API ✓
  - Fixed `test_users_lookup_by_email_keys` to filter for users with non-empty email ✓
- **Final result: 158 passed · 0 skipped · 0 failed (was 56 failed)**

## Phase 4: Document and Organize Artifacts

- [x] 4.1 Create `API_NOTES.md` with all 5 sections:
  - Ground Truth (official docs, real workspace, auth/capture scripts)
  - API Quirks (append-only, dated, with fixture references)
  - Intentionally Skipped (endpoints/features not implemented, with reasons)
  - Key Design Choices
  - Open Questions
- [x] 4.2 Create `mock_coverage.json` — 41/83 endpoints implemented, all 41 mapped to fixtures + tests
- [x] 4.3 Create `_capture_metadata.json` in `tests/fixtures/real_slack/` — enriched with fixture_count, api_version, auth_method
- [x] 4.4 Write `tests/test_api.py` — 48 functional CRUD tests
  - Channel lifecycle: create → rename → set topic/purpose → archive → unarchive ✓
  - Message lifecycle: post → update → add reaction → pin → delete ✓
  - Membership: invite → kick, join → leave, cant_leave_general, not_in_channel ✓
  - Files: upload → info → list → delete ✓
  - User profile: get → set, presence get → set ✓
  - Search: post messages → search → verify results, empty results ✓
  - Pagination: cursor-based for conversations.list, history, users.list ✓
  - Error cases: channel_not_found, user_not_found, message_not_found, file_not_found, already_archived ✓
- [x] 4.5 Write `scripts/validate_seed.py` — validates workspace, users, channels, messages, threads, files, pins, reminders
- [x] 4.6 Verify all conformance tests pass — 160 passed · 0 failed · 0 skipped ✓
- [x] 4.7 Verify all CRUD tests pass — 48 passed · 0 failed ✓
- **Final result: 208 passed (160 conformance + 48 CRUD) · 0 failed · 0 skipped**
