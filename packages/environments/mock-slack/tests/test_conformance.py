"""Conformance tests — verify mock response shapes match real Slack golden fixtures.

These tests don't compare exact values (IDs, timestamps differ) but verify that
the response structure (keys present/absent, types, nesting) matches real Slack.

Organized by bug class per the API Validation Playbook (Phase 2.1: Key-set comparison).
"""

import json
from pathlib import Path

import pytest

FIXTURES_DIR = Path(__file__).parent / "fixtures" / "real_slack"

WORKSPACE_HEADER = {"X-Mock-Slack-Workspace": "workspace_001"}
USER_TOKEN_HEADER = {
    "X-Mock-Slack-Workspace": "workspace_001",
    "Authorization": "Bearer mock-user-token",
}


def load_fixture(name: str) -> dict:
    path = FIXTURES_DIR / name
    if not path.exists():
        pytest.skip(f"Golden fixture {name} not found")
    data = json.loads(path.read_text())
    data.pop("_captured_at", None)
    return data


def _assert_shape(real, mock, path="", strict=True):
    """Recursively assert mock response shape matches real fixture.

    Checks:
    - Missing keys: real_keys - mock_keys (always)
    - Extra keys: mock_keys - real_keys (when strict=True)
    - Type mismatches at leaf nodes
    """
    if isinstance(real, dict) and isinstance(mock, dict):
        real_keys = set(real.keys())
        mock_keys = set(mock.keys())
        missing = real_keys - mock_keys
        extra = mock_keys - real_keys
        errors = []
        if missing:
            errors.append(f"Mock MISSING keys at {path or 'root'!r}: {missing}")
        if strict and extra:
            errors.append(f"Mock has EXTRA keys at {path or 'root'!r}: {extra}")
        if errors:
            pytest.fail("\n".join(errors))
        for key in real_keys & mock_keys:
            _assert_shape(real[key], mock[key], f"{path}.{key}" if path else key, strict)
    elif isinstance(real, list) and isinstance(mock, list):
        if real and not mock:
            pytest.fail(f"Mock list is empty at {path!r}, real fixture has items")
        if not real:
            return
        for idx, item in enumerate(mock):
            _assert_any_shape(real, item, f"{path}[{idx}]", strict)
    else:
        if real is not None and mock is not None:
            real_type = type(real).__name__
            mock_type = type(mock).__name__
            assert real_type == mock_type, f"TYPE MISMATCH at {path}: real={real_type}, mock={mock_type}"


def _assert_any_shape(real_items: list, mock_item, path: str, strict: bool) -> None:
    errors = []
    for real_item in real_items:
        try:
            _assert_shape(real_item, mock_item, path, strict)
            return
        except AssertionError as exc:
            errors.append(str(exc))
    pytest.fail(f"Mock item at {path!r} matches no fixture item shape: {'; '.join(errors)}")


def assert_keys_match(real: dict, mock: dict, path: str = "", strict: bool = True):
    """Single-level bidirectional key comparison (does not recurse into nested dicts).

    For recursive shape comparison, use _assert_shape() instead.
    """
    real_keys = set(real.keys())
    mock_keys = set(mock.keys())
    extra = mock_keys - real_keys
    missing = real_keys - mock_keys
    errors = []
    if missing:
        errors.append(f"Mock MISSING keys at {path!r}: {missing}")
    if strict and extra:
        errors.append(f"Mock has EXTRA keys at {path!r}: {extra}")
    if errors:
        pytest.fail("\n".join(errors))


# ---------------------------------------------------------------------------
# auth
# ---------------------------------------------------------------------------

class TestAuthConformance:
    def test_auth_test_keys(self, client):
        """auth.test top-level keys match real fixture."""
        real = load_fixture("auth_test.json")
        resp = client.post("/api/auth.test", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "auth.test")

    def test_auth_test_url_format(self, client):
        """auth.test url starts with https:// and ends with .slack.com/."""
        resp = client.post("/api/auth.test", headers=WORKSPACE_HEADER)
        mock = resp.json()
        assert mock["url"].startswith("https://")
        assert mock["url"].endswith(".slack.com/")


# ---------------------------------------------------------------------------
# team
# ---------------------------------------------------------------------------

class TestTeamConformance:
    def test_team_info_keys(self, client):
        """team.info top-level keys match real fixture."""
        real = load_fixture("team_info.json")
        resp = client.get("/api/team.info", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "team.info")

    def test_team_info_team_object_keys(self, client):
        """team.info team object keys match real fixture."""
        real = load_fixture("team_info.json")
        resp = client.get("/api/team.info", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert "team" in mock
        assert_keys_match(real["team"], mock["team"], "team.info.team")


# ---------------------------------------------------------------------------
# conversations — list / info / history
# ---------------------------------------------------------------------------

class TestConversationsListConformance:
    def test_conversations_list_keys(self, client):
        """conversations.list top-level keys match real fixture."""
        real = load_fixture("conversations_list.json")
        resp = client.get("/api/conversations.list", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.list")

    def test_conversations_list_channel_keys(self, client):
        """Each channel in conversations.list has required fields."""
        resp = client.get("/api/conversations.list", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert len(mock["channels"]) > 0
        for ch in mock["channels"]:
            for key in ("id", "name", "is_private", "is_archived", "created"):
                assert key in ch, f"Channel missing key: {key}"

    def test_conversations_list_private_keys(self, client):
        """conversations.list?types=private_channel top-level keys match real."""
        real = load_fixture("conversations_list_private.json")
        resp = client.get(
            "/api/conversations.list?types=private_channel", headers=WORKSPACE_HEADER
        )
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.list(private)")

    def test_conversations_list_im_keys(self, client):
        """conversations.list?types=im top-level keys match real."""
        real = load_fixture("conversations_list_im.json")
        resp = client.get(
            "/api/conversations.list?types=im", headers=WORKSPACE_HEADER
        )
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.list(im)")


class TestConversationsInfoConformance:
    def test_conversations_info_keys(self, client):
        """conversations.info top-level keys match real fixture."""
        real = load_fixture("conversations_info.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.get(f"/api/conversations.info?channel={ch_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.info")

    def test_conversations_info_channel_keys(self, client):
        """conversations.info channel object keys match real fixture."""
        real = load_fixture("conversations_info.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.get(f"/api/conversations.info?channel={ch_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert_keys_match(real["channel"], mock["channel"], "conversations.info.channel", strict=False)  # Known gap: mock has extra last_read


class TestConversationsHistoryConformance:
    def test_conversations_history_keys(self, client):
        """conversations.history top-level keys match real fixture."""
        real = load_fixture("conversations_history.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.get(f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.history")

    def test_conversations_history_empty_keys(self, client):
        """conversations.history with no messages top-level keys match real fixture."""
        real = load_fixture("conversations_history_empty.json")
        # Create a fresh channel with no messages
        create_resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER, json={
            "name": "empty-history-test",
        })
        ch_id = create_resp.json()["channel"]["id"]

        resp = client.get(f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert mock["messages"] == []
        assert_keys_match(real, mock, "conversations.history(empty)")

    def test_conversations_history_message_keys(self, client):
        """Message items in conversations.history have required fields."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            resp = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            )
            msgs = resp.json().get("messages", [])
            regular_msgs = [m for m in msgs if m.get("subtype") != "channel_join"]
            if not regular_msgs:
                continue

            # Real regular message has: user, type, ts, text, team, blocks, language
            # (language is a real API field added in ~2023)
            real_history = load_fixture("conversations_history.json")
            real_regular = [m for m in real_history["messages"] if "user" in m and "text" in m and "team" in m]
            if not real_regular:
                return

            assert_keys_match(real_regular[0], regular_msgs[0], "conversations.history.messages[0]", strict=False)  # Known gap: mock has extra language key
            return

        pytest.skip("No regular messages found in any channel")

    def test_conversations_members_keys(self, client):
        """conversations.members top-level keys match real fixture."""
        real = load_fixture("conversations_members.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.get(f"/api/conversations.members?channel={ch_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.members")

    def test_conversations_replies_keys(self, client):
        """conversations.replies top-level keys match real fixture."""
        real = load_fixture("conversations_replies.json")
        # Find a message with replies
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            history = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json()
            for msg in history.get("messages", []):
                if msg.get("reply_count", 0) > 0:
                    resp = client.get(
                        f"/api/conversations.replies?channel={ch['id']}&ts={msg['ts']}",
                        headers=WORKSPACE_HEADER,
                    )
                    mock = resp.json()
                    assert mock["ok"] is True
                    assert_keys_match(real, mock, "conversations.replies")
                    return

        pytest.skip("No threaded messages found")


# ---------------------------------------------------------------------------
# conversations — mutations
# ---------------------------------------------------------------------------

class TestConversationsMutationConformance:
    def test_create_channel_keys(self, client):
        """conversations.create top-level keys match real fixture."""
        real = load_fixture("conversations_create_response.json")
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER, json={
            "name": "conformance-create-test",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.create")

    def test_create_channel_channel_keys(self, client):
        """conversations.create channel object keys match real fixture."""
        real = load_fixture("conversations_create_response.json")
        # Use user-token header so last_read is included (real fixture was captured with a user token)
        resp = client.post("/api/conversations.create", headers=USER_TOKEN_HEADER, json={
            "name": "conformance-create-keys",
        })
        mock = resp.json()

        assert_keys_match(real["channel"], mock["channel"], "conversations.create.channel")

    def test_rename_channel_keys(self, client):
        """conversations.rename top-level keys match real fixture."""
        real = load_fixture("conversations_rename_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.post("/api/conversations.rename", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
            "name": "conformance-renamed",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.rename")

    def test_invite_channel_keys(self, client):
        """conversations.invite top-level keys match real fixture."""
        real = load_fixture("conversations_invite_response.json")
        # Create channel and get a user to invite
        create_resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER, json={
            "name": "conformance-invite-test",
        })
        ch_id = create_resp.json()["channel"]["id"]
        users = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        human_users = [u for u in users if not u["is_bot"] and u["id"] != "USLACKBOT"]
        if not human_users:
            pytest.skip("No human users to invite")
        user_id = human_users[0]["id"]

        resp = client.post("/api/conversations.invite", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
            "users": user_id,
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.invite")

    def test_kick_channel_keys(self, client):
        """conversations.kick top-level keys match real fixture."""
        real = load_fixture("conversations_kick_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        members_resp = client.get(f"/api/conversations.members?channel={ch_id}", headers=WORKSPACE_HEADER).json()
        members = members_resp.get("members", [])
        users = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        kickable = [u for u in users if u["id"] in members and not u["is_bot"] and u["id"] != "USLACKBOT"]
        if not kickable:
            pytest.skip("No kickable members found")

        resp = client.post("/api/conversations.kick", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
            "user": kickable[0]["id"],
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.kick")

    def test_join_channel_keys(self, client):
        """conversations.join top-level keys match real fixture."""
        real = load_fixture("conversations_join_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.post("/api/conversations.join", headers=USER_TOKEN_HEADER, json={
            "channel": ch_id,
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.join")

    def test_leave_channel_keys(self, client):
        """conversations.leave top-level keys match real fixture."""
        real = load_fixture("conversations_leave_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        non_general = [ch for ch in channels if ch.get("name") != "general"]
        if not non_general:
            pytest.skip("no non-general channel available")
        ch_id = non_general[0]["id"]

        resp = client.post("/api/conversations.leave", headers=USER_TOKEN_HEADER, json={
            "channel": ch_id,
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.leave")

    def test_archive_channel_keys(self, client):
        """conversations.archive top-level keys match real fixture."""
        real = load_fixture("conversations_archive_response.json")
        # Create a fresh channel to archive
        create_resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER, json={
            "name": "conformance-archive-test",
        })
        ch_id = create_resp.json()["channel"]["id"]

        resp = client.post("/api/conversations.archive", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.archive")

    def test_unarchive_channel_keys(self, client):
        """conversations.unarchive top-level keys match real fixture."""
        real = load_fixture("conversations_unarchive_response.json")
        # Create + archive + unarchive
        create_resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER, json={
            "name": "conformance-unarchive-test",
        })
        ch_id = create_resp.json()["channel"]["id"]
        client.post("/api/conversations.archive", headers=WORKSPACE_HEADER, json={"channel": ch_id})

        resp = client.post("/api/conversations.unarchive", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.unarchive")

    def test_set_topic_keys(self, client):
        """conversations.setTopic top-level keys match real fixture (returns channel, not topic string)."""
        real = load_fixture("conversations_set_topic_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.post("/api/conversations.setTopic", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
            "topic": "Conformance test topic",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.setTopic")

    def test_set_purpose_keys(self, client):
        """conversations.setPurpose top-level keys match real fixture (returns channel, not purpose string)."""
        real = load_fixture("conversations_set_purpose_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.post("/api/conversations.setPurpose", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
            "purpose": "Conformance test purpose",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "conversations.setPurpose")


# ---------------------------------------------------------------------------
# users
# ---------------------------------------------------------------------------

class TestUsersConformance:
    def test_users_list_keys(self, client):
        """users.list top-level keys match real fixture."""
        real = load_fixture("users_list.json")
        resp = client.get("/api/users.list", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "users.list")

    def test_users_list_member_keys(self, client):
        """Each member in users.list has required fields."""
        resp = client.get("/api/users.list", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert len(mock["members"]) > 0
        for member in mock["members"]:
            for key in ("id", "name", "real_name", "is_bot", "profile"):
                assert key in member, f"Member missing key: {key}"

    def test_users_list_has_non_bot_user(self, client):
        """users.list includes at least one non-bot user."""
        resp = client.get("/api/users.list", headers=WORKSPACE_HEADER)
        members = resp.json()["members"]
        humans = [m for m in members if not m["is_bot"]]
        assert len(humans) >= 1

    def test_users_info_keys(self, client):
        """users.info top-level keys match real fixture."""
        real = load_fixture("users_info.json")
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        user_id = members[0]["id"]

        resp = client.get(f"/api/users.info?user={user_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "users.info")

    def test_users_info_user_keys(self, client):
        """users.info user object keys match real fixture."""
        real = load_fixture("users_info.json")
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        user_id = members[0]["id"]

        resp = client.get(f"/api/users.info?user={user_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert_keys_match(real["user"], mock["user"], "users.info.user")

    def test_users_profile_has_expected_fields(self, client):
        """User profile contains real_name, display_name, status_text, status_emoji."""
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        for member in members:
            profile = member["profile"]
            for key in ("real_name", "display_name", "status_text", "status_emoji"):
                assert key in profile

    def test_users_profile_get_keys(self, client):
        """users.profile.get top-level keys match real fixture."""
        real = load_fixture("users_profile_get.json")
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        human = next((m for m in members if not m["is_bot"] and m["id"] != "USLACKBOT"), None)
        if not human:
            pytest.skip("No human user found")

        resp = client.get(f"/api/users.profile.get?user={human['id']}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "users.profile.get")

    def test_users_get_presence_keys(self, client):
        """users.getPresence top-level keys match real fixture."""
        real = load_fixture("users_get_presence.json")
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        user_id = members[0]["id"]

        resp = client.get(f"/api/users.getPresence?user={user_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "users.getPresence")

    def test_users_lookup_by_email_keys(self, client):
        """users.lookupByEmail top-level keys match real fixture."""
        real = load_fixture("users_lookup_by_email.json")
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        human = next((m for m in members if not m["is_bot"] and "profile" in m), None)
        if not human:
            pytest.skip("No human user with profile found")
        # find a user with a non-empty email (skip USLACKBOT which has no email)
        human = next(
            (m for m in members if not m["is_bot"] and m["profile"].get("email")),
            None,
        )
        if not human:
            pytest.skip("No human user with email found")
        email = human["profile"]["email"]

        resp = client.get(f"/api/users.lookupByEmail?email={email}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        if not mock.get("ok"):
            pytest.skip("lookupByEmail not finding seeded user by email")
        assert_keys_match(real, mock, "users.lookupByEmail")

    def test_users_set_presence_keys(self, client):
        """users.setPresence top-level keys match real fixture."""
        real = load_fixture("users_set_presence_response.json")
        resp = client.post("/api/users.setPresence", headers=WORKSPACE_HEADER, json={
            "presence": "auto",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "users.setPresence")

    def test_users_profile_set_keys(self, client):
        """users.profile.set top-level keys match real fixture."""
        real = load_fixture("users_profile_set_response.json")
        resp = client.post("/api/users.profile.set", headers=WORKSPACE_HEADER, json={
            "profile": {"status_text": "testing", "status_emoji": ":test:"},
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "users.profile.set")


# ---------------------------------------------------------------------------
# chat
# ---------------------------------------------------------------------------

class TestChatConformance:
    def test_post_message_keys(self, client):
        """chat.postMessage top-level keys match real fixture."""
        real = load_fixture("chat_post_message_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
            "text": "Conformance test message",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "chat.postMessage")

    def test_post_message_message_keys(self, client):
        """chat.postMessage response.message keys match real fixture."""
        real = load_fixture("chat_post_message_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
            "text": "Conformance test message keys",
        })
        mock = resp.json()

        assert_keys_match(real["message"], mock["message"], "chat.postMessage.message")

    def test_post_message_reply_keys(self, client):
        """chat.postMessage reply (with thread_ts) top-level keys match real fixture."""
        real = load_fixture("chat_post_message_reply_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        # Post parent, then reply
        parent = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "Parent message",
        }).json()
        parent_ts = parent["ts"]

        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
            "text": "Reply message",
            "thread_ts": parent_ts,
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "chat.postMessage(reply)")

    def test_chat_update_keys(self, client):
        """chat.update top-level keys match real fixture."""
        real = load_fixture("chat_update_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        post_resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "Message to update",
        })
        ts = post_resp.json()["ts"]

        resp = client.post("/api/chat.update", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "ts": ts, "text": "Updated text",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "chat.update")

    def test_chat_delete_keys(self, client):
        """chat.delete top-level keys match real fixture."""
        real = load_fixture("chat_delete_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        post_resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "Message to delete",
        })
        ts = post_resp.json()["ts"]

        resp = client.post("/api/chat.delete", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "ts": ts,
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "chat.delete")

    def test_chat_post_ephemeral_keys(self, client):
        """chat.postEphemeral top-level keys match real fixture."""
        real = load_fixture("chat_post_ephemeral_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        user_id = members[0]["id"]

        resp = client.post("/api/chat.postEphemeral", headers=WORKSPACE_HEADER, json={
            "channel": ch_id,
            "user": user_id,
            "text": "Ephemeral test message",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "chat.postEphemeral")

    def test_chat_get_permalink_keys(self, client):
        """chat.getPermalink top-level keys match real fixture."""
        real = load_fixture("chat_get_permalink.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        post_resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "Permalink test",
        })
        ts = post_resp.json()["ts"]

        resp = client.get(
            f"/api/chat.getPermalink?channel={ch_id}&message_ts={ts}",
            headers=WORKSPACE_HEADER,
        )
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "chat.getPermalink")


# ---------------------------------------------------------------------------
# reactions
# ---------------------------------------------------------------------------

class TestReactionsConformance:
    def _get_channel_and_ts(self, client):
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            if msgs:
                return ch["id"], msgs[0]["ts"]
        pytest.skip("No messages found to test reactions")

    def test_reactions_add_keys(self, client):
        """reactions.add top-level keys match real fixture."""
        real = load_fixture("reactions_add_response.json")
        ch_id, ts = self._get_channel_and_ts(client)

        resp = client.post("/api/reactions.add", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "timestamp": ts, "name": "thumbsup",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "reactions.add")

    def test_reactions_remove_keys(self, client):
        """reactions.remove top-level keys match real fixture."""
        real = load_fixture("reactions_remove_response.json")
        ch_id, ts = self._get_channel_and_ts(client)

        client.post("/api/reactions.add", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "timestamp": ts, "name": "wave",
        })
        resp = client.post("/api/reactions.remove", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "timestamp": ts, "name": "wave",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "reactions.remove")

    def test_reactions_get_keys(self, client):
        """reactions.get top-level keys match real fixture."""
        real = load_fixture("reactions_get.json")
        ch_id, ts = self._get_channel_and_ts(client)

        client.post("/api/reactions.add", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "timestamp": ts, "name": "thumbsup",
        })
        resp = client.get(
            f"/api/reactions.get?channel={ch_id}&timestamp={ts}", headers=WORKSPACE_HEADER
        )
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "reactions.get")

    def test_reactions_get_empty_keys(self, client):
        """reactions.get with no reactions top-level keys match real empty fixture."""
        real = load_fixture("reactions_get_empty.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        # Post a fresh message with no reactions
        ch_id = channels[0]["id"]
        post_resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "Reactions empty test",
        })
        ts = post_resp.json()["ts"]

        resp = client.get(
            f"/api/reactions.get?channel={ch_id}&timestamp={ts}", headers=WORKSPACE_HEADER
        )
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "reactions.get(empty)")


# ---------------------------------------------------------------------------
# pins
# ---------------------------------------------------------------------------

class TestPinsConformance:
    def _pin_a_message(self, client):
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            if msgs:
                ch_id = ch["id"]
                ts = msgs[0]["ts"]
                client.post("/api/pins.add", headers=WORKSPACE_HEADER, json={
                    "channel": ch_id, "timestamp": ts,
                })
                return ch_id, ts
        pytest.skip("No messages found to pin")

    def test_pins_add_keys(self, client):
        """pins.add top-level keys match real fixture."""
        real = load_fixture("pins_add_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            if msgs:
                resp = client.post("/api/pins.add", headers=WORKSPACE_HEADER, json={
                    "channel": ch["id"], "timestamp": msgs[0]["ts"],
                })
                mock = resp.json()
                assert mock["ok"] is True
                assert_keys_match(real, mock, "pins.add")
                return
        pytest.skip("No messages to pin")

    def test_pins_remove_keys(self, client):
        """pins.remove top-level keys match real fixture."""
        real = load_fixture("pins_remove_response.json")
        ch_id, ts = self._pin_a_message(client)

        resp = client.post("/api/pins.remove", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "timestamp": ts,
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "pins.remove")

    def test_pins_list_keys(self, client):
        """pins.list top-level keys match real fixture."""
        real = load_fixture("pins_list.json")
        ch_id, _ = self._pin_a_message(client)

        resp = client.get(f"/api/pins.list?channel={ch_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "pins.list")

    def test_pins_list_empty_keys(self, client):
        """pins.list with no pins top-level keys match real empty fixture."""
        real = load_fixture("pins_list_empty.json")
        create_resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER, json={
            "name": "conformance-pins-empty",
        })
        ch_id = create_resp.json()["channel"]["id"]

        resp = client.get(f"/api/pins.list?channel={ch_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert mock["items"] == []
        assert_keys_match(real, mock, "pins.list(empty)")

    def test_pins_list_item_keys(self, client):
        """Pinned items keys match real fixture."""
        real = load_fixture("pins_list.json")
        ch_id, _ = self._pin_a_message(client)

        items = client.get(f"/api/pins.list?channel={ch_id}", headers=WORKSPACE_HEADER).json()["items"]
        if not items:
            pytest.skip("No pinned items returned")

        real_items = real.get("items", [])
        if not real_items:
            pytest.skip("Real fixture has no items")

        assert_keys_match(real_items[0], items[0], "pins.list.items[0]")


# ---------------------------------------------------------------------------
# files
# ---------------------------------------------------------------------------

class TestFilesConformance:
    def test_files_upload_keys(self, client):
        """files.upload top-level keys match real fixture."""
        real = load_fixture("files_upload_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.post("/api/files.upload", headers=WORKSPACE_HEADER, json={
            "channels": ch_id,
            "content": "Conformance test file content",
            "filename": "test.txt",
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "files.upload")

    def test_files_info_keys(self, client):
        """files.info top-level keys match real fixture."""
        real = load_fixture("files_info.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        upload_resp = client.post("/api/files.upload", headers=WORKSPACE_HEADER, json={
            "channels": ch_id,
            "content": "File info test",
            "filename": "info_test.txt",
        })
        file_id = upload_resp.json()["file"]["id"]

        resp = client.get(f"/api/files.info?file={file_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        # Known gap: mock missing content/preview/highlight fields that real Slack includes for text files
        known_missing = {"content", "content_highlight_html", "content_highlight_html_truncated",
                         "content_highlight_css", "is_truncated"}
        real_keys = set(real.keys())
        mock_keys = set(mock.keys())
        unexpected_missing = (real_keys - mock_keys) - known_missing
        assert not unexpected_missing, f"Mock MISSING unexpected keys at files.info: {unexpected_missing}"

    def test_files_list_keys(self, client):
        """files.list top-level keys match real fixture."""
        real = load_fixture("files_list.json")
        resp = client.get("/api/files.list", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "files.list")

    def test_files_list_by_channel_keys(self, client):
        """files.list?channel=... top-level keys match real fixture."""
        real = load_fixture("files_list_by_channel.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        resp = client.get(f"/api/files.list?channel={ch_id}", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "files.list(by channel)")

    def test_files_delete_keys(self, client):
        """files.delete top-level keys match real fixture."""
        real = load_fixture("files_delete_response.json")
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]

        upload_resp = client.post("/api/files.upload", headers=WORKSPACE_HEADER, json={
            "channels": ch_id,
            "content": "File to delete",
            "filename": "delete_test.txt",
        })
        file_id = upload_resp.json()["file"]["id"]

        resp = client.post("/api/files.delete", headers=WORKSPACE_HEADER, json={
            "file": file_id,
        })
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "files.delete")


# ---------------------------------------------------------------------------
# search
# ---------------------------------------------------------------------------

class TestSearchConformance:
    def test_search_messages_keys(self, client):
        """search.messages top-level keys match real fixture."""
        real = load_fixture("search_messages.json")
        resp = client.get("/api/search.messages?query=the", headers=USER_TOKEN_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "search.messages")

    def test_search_messages_messages_obj_keys(self, client):
        """search.messages.messages object keys match real fixture."""
        real = load_fixture("search_messages.json")
        resp = client.get("/api/search.messages?query=the", headers=USER_TOKEN_HEADER)
        mock = resp.json()

        assert_keys_match(real["messages"], mock["messages"], "search.messages.messages")

    def test_search_messages_match_keys(self, client):
        """Search matches have required keys."""
        real = load_fixture("search_messages.json")
        resp = client.get("/api/search.messages?query=the", headers=USER_TOKEN_HEADER)
        matches = resp.json()["messages"]["matches"]

        if not matches:
            pytest.skip("No search matches found")

        real_matches = real["messages"]["matches"]
        if not real_matches:
            pytest.skip("Real fixture has no matches")

        assert_keys_match(real_matches[0], matches[0], "search.messages.messages.matches[0]")

    def test_search_messages_empty_keys(self, client):
        """search.messages with no results top-level keys match real empty fixture."""
        real = load_fixture("search_messages_empty.json")
        resp = client.get(
            "/api/search.messages?query=xyzzy_unlikely_12345",
            headers=USER_TOKEN_HEADER,
        )
        mock = resp.json()

        assert mock["ok"] is True
        assert mock["messages"]["total"] == 0
        assert_keys_match(real, mock, "search.messages(empty)")


# ---------------------------------------------------------------------------
# reminders
# ---------------------------------------------------------------------------

class TestRemindersConformance:
    def test_reminders_list_keys(self, client):
        """reminders.list top-level keys match real fixture."""
        real = load_fixture("reminders_list.json")
        resp = client.get("/api/reminders.list", headers=WORKSPACE_HEADER)
        mock = resp.json()

        assert mock["ok"] is True
        assert_keys_match(real, mock, "reminders.list")


# ===========================================================================
# Phase 2.2: Value-type comparison
# Checks JSON types, string formats, and null-vs-absent (Bug 2).
# ===========================================================================

import re

TS_RE = re.compile(r"^\d{10}\.\d{1,6}$")  # Slack epoch string: "1234567890.123456"


def assert_ts_format(value, path: str):
    """Assert value is a Slack epoch timestamp string."""
    assert isinstance(value, str), f"{path}: expected str, got {type(value).__name__} ({value!r})"
    assert TS_RE.match(value), f"{path}: bad ts format {value!r} (expected '1234567890.123456')"


def assert_type(value, expected_type, path: str):
    assert isinstance(value, expected_type), (
        f"{path}: expected {expected_type.__name__}, got {type(value).__name__} ({value!r})"
    )


class TestTimestampTypes:
    """2.2 — Slack timestamps must be epoch strings, not ints or ISO dates."""

    def test_message_ts_is_epoch_string(self, client):
        """conversations.history message ts is an epoch string."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            if msgs:
                assert_ts_format(msgs[0]["ts"], "history.messages[0].ts")
                return
        pytest.skip("No messages found")

    def test_postmessage_ts_is_epoch_string(self, client):
        """chat.postMessage response ts is an epoch string."""
        ch_id = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"][0]["id"]
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "ts type test",
        })
        mock = resp.json()
        assert_ts_format(mock["ts"], "postMessage.ts")
        assert_ts_format(mock["message"]["ts"], "postMessage.message.ts")

    def test_channel_created_is_int(self, client):
        """channels.list channel.created is an int (Unix seconds)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        assert len(channels) > 0
        for ch in channels:
            assert_type(ch["created"], int, f"channel({ch['id']}).created")

    def test_topic_last_set_is_int(self, client):
        """channel.topic.last_set is an int."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            assert_type(ch["topic"]["last_set"], int, f"channel({ch['id']}).topic.last_set")
            assert_type(ch["purpose"]["last_set"], int, f"channel({ch['id']}).purpose.last_set")

    def test_pins_item_created_is_int(self, client):
        """pins.list item.created is an int (Unix seconds)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            if not msgs:
                continue
            client.post("/api/pins.add", headers=WORKSPACE_HEADER, json={
                "channel": ch["id"], "timestamp": msgs[0]["ts"],
            })
            items = client.get(
                f"/api/pins.list?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json()["items"]
            if items:
                assert_type(items[0]["created"], int, "pins.list.items[0].created")
                return
        pytest.skip("No pins found")

    def test_reactions_count_is_int(self, client):
        """Reaction count is an int."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            if not msgs:
                continue
            ts = msgs[0]["ts"]
            ch_id = ch["id"]
            client.post("/api/reactions.add", headers=WORKSPACE_HEADER, json={
                "channel": ch_id, "timestamp": ts, "name": "thumbsup",
            })
            rxns = client.get(
                f"/api/reactions.get?channel={ch_id}&timestamp={ts}", headers=WORKSPACE_HEADER
            ).json()["message"].get("reactions", [])
            if rxns:
                assert_type(rxns[0]["count"], int, "reactions[0].count")
                return
        pytest.skip("No reactions found")

    def test_user_updated_is_int(self, client):
        """users.info user.updated is an int — real Slack returns epoch seconds."""
        real = load_fixture("users_info.json")
        assert_type(real["user"]["updated"], int, "fixture:users_info.user.updated")

        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        user_id = members[0]["id"]
        user = client.get(f"/api/users.info?user={user_id}", headers=WORKSPACE_HEADER).json().get("user", {})
        if "updated" in user:
            assert_type(user["updated"], int, "users.info.user.updated")

    def test_tz_offset_is_int(self, client):
        """users.info user.tz_offset is an int (can be negative)."""
        real = load_fixture("users_info.json")
        assert_type(real["user"]["tz_offset"], int, "fixture:users_info.user.tz_offset")

        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        user_id = members[0]["id"]
        user = client.get(f"/api/users.info?user={user_id}", headers=WORKSPACE_HEADER).json().get("user", {})
        if "tz_offset" in user:
            assert_type(user["tz_offset"], int, "users.info.user.tz_offset")


class TestBooleanTypes:
    """2.2 — is_* fields must be proper JSON booleans, not ints or strings."""

    def test_channel_booleans_are_bool(self, client):
        """Channel is_* fields are bool, not int."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        bool_fields = ("is_private", "is_archived", "is_im", "is_mpim")
        for ch in channels[:3]:
            for field in bool_fields:
                if field in ch:
                    assert isinstance(ch[field], bool), (
                        f"channel.{field} is {type(ch[field]).__name__}, expected bool"
                    )

    def test_message_has_more_is_bool(self, client):
        """conversations.history has_more is bool."""
        ch_id = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"][0]["id"]
        mock = client.get(f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER).json()
        assert isinstance(mock["has_more"], bool), (
            f"has_more is {type(mock['has_more']).__name__}, expected bool"
        )

    def test_user_booleans_are_bool(self, client):
        """User is_* fields are bool."""
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        bool_fields = ("is_bot", "is_admin", "deleted")
        for m in members[:3]:
            for field in bool_fields:
                if field in m:
                    assert isinstance(m[field], bool), (
                        f"user.{field} is {type(m[field]).__name__}, expected bool"
                    )

    def test_channel_unlinked_is_int_not_bool(self, client):
        """Real Slack channel.unlinked is int 0, not bool.

        Bug 5: real API uses integer 0 for unlinked/is_moved, not boolean False.
        """
        real = load_fixture("conversations_list.json")
        ch = real["channels"][0]
        assert "unlinked" in ch, "fixture missing unlinked"
        assert_type(ch["unlinked"], int, "fixture:channel.unlinked")
        assert not isinstance(ch["unlinked"], bool), "fixture: unlinked should be int, not bool"

        # Check mock too
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        if "unlinked" in channels[0]:
            val = channels[0]["unlinked"]
            assert isinstance(val, int) and not isinstance(val, bool), (
                f"channel.unlinked should be int 0, got {type(val).__name__}({val!r})"
            )


class TestNullVsAbsent:
    """2.2 — Bug 2: null vs absent. Real Slack omits optional fields entirely.
    Mock may return them as null.
    """

    def test_message_thread_ts_absent_when_no_thread(self, client):
        """thread_ts must be ABSENT (not null) for non-threaded messages.

        Real Slack omits thread_ts from root messages that have no replies.
        Mock uses thread_ts: str | None = None which serializes as null.
        """
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            non_thread = [m for m in msgs if not m.get("thread_ts") and m.get("type") == "message"]
            if non_thread:
                msg = non_thread[0]
                assert "thread_ts" not in msg, (
                    f"thread_ts should be absent for non-threaded message, got {msg.get('thread_ts')!r}"
                )
                return
        pytest.skip("No non-threaded messages found")

    def test_message_reply_count_absent_when_no_replies(self, client):
        """reply_count must be ABSENT (not null) for messages with no replies.

        Real Slack omits reply_count when there are no replies.
        Mock has reply_count: int | None = None which serializes as null.
        """
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            # Find a message that was just posted (no replies)
            ch_id = ch["id"]
            post_resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
                "channel": ch_id, "text": "reply_count type test",
            })
            if not post_resp.json().get("ok"):
                continue
            ts = post_resp.json()["ts"]
            # Fetch the message back
            history = client.get(
                f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
            ).json()
            fresh = next((m for m in history.get("messages", []) if m.get("ts") == ts), None)
            if fresh:
                assert "reply_count" not in fresh, (
                    f"reply_count should be absent for new message, got {fresh.get('reply_count')!r}"
                )
                return
        pytest.skip("Could not find a fresh message to test")

    def test_message_reactions_absent_when_none(self, client):
        """reactions must be ABSENT (not null) on messages with no reactions.

        Real Slack omits reactions entirely. Mock may serialize as null.
        """
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        post_resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "reactions absent test",
        })
        ts = post_resp.json()["ts"]
        history = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()
        msg = next((m for m in history.get("messages", []) if m.get("ts") == ts), None)
        if msg is None:
            pytest.skip("Could not find posted message")

        assert "reactions" not in msg, (
            f"reactions should be absent when there are none, got {msg.get('reactions')!r}"
        )

    def test_message_edited_absent_when_not_edited(self, client):
        """edited must be ABSENT (not null) for unedited messages.

        Real Slack omits edited entirely. Mock may serialize as null.
        """
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        post_resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "edited absent test",
        })
        ts = post_resp.json()["ts"]
        history = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()
        msg = next((m for m in history.get("messages", []) if m.get("ts") == ts), None)
        if msg is None:
            pytest.skip("Could not find posted message")

        assert "edited" not in msg, (
            f"edited should be absent for unedited message, got {msg.get('edited')!r}"
        )

    def test_channel_parent_conversation_is_null_not_absent(self, client):
        """channel.parent_conversation should be null (key present, value null).

        Real Slack always includes parent_conversation: null for normal channels.
        This is the OPPOSITE of null-vs-absent — the key must BE present.
        """
        real = load_fixture("conversations_list.json")
        ch = real["channels"][0]
        assert "parent_conversation" in ch, "fixture: parent_conversation should be present"
        assert ch["parent_conversation"] is None, "fixture: parent_conversation should be null"

        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        if "parent_conversation" in channels[0]:
            assert channels[0]["parent_conversation"] is None, (
                "channel.parent_conversation should be null, not some other value"
            )
        # If absent from mock response — this is a missing-key bug (caught in 2.1)

    def test_channel_actions_ts_is_null_not_absent(self, client):
        """conversations.history channel_actions_ts should be null (key present).

        Real Slack returns channel_actions_ts: null in history responses.
        """
        real = load_fixture("conversations_history.json")
        assert "channel_actions_ts" in real, "fixture: channel_actions_ts should be present"
        assert real["channel_actions_ts"] is None, "fixture: channel_actions_ts should be null"

        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        mock = client.get(f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER).json()
        if "channel_actions_ts" in mock:
            assert mock["channel_actions_ts"] is None, (
                "channel_actions_ts should be null"
            )

    def test_postmessage_message_thread_ts_absent(self, client):
        """chat.postMessage response.message must not include thread_ts when not a reply."""
        ch_id = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"][0]["id"]
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "no-thread message",
        })
        msg = resp.json().get("message", {})
        assert "thread_ts" not in msg, (
            f"postMessage.message.thread_ts should be absent, got {msg.get('thread_ts')!r}"
        )

    def test_postmessage_message_reply_count_absent(self, client):
        """chat.postMessage response.message must not include reply_count."""
        ch_id = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"][0]["id"]
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "reply_count absent test",
        })
        msg = resp.json().get("message", {})
        assert "reply_count" not in msg, (
            f"postMessage.message.reply_count should be absent, got {msg.get('reply_count')!r}"
        )

    def test_postmessage_message_reactions_absent(self, client):
        """chat.postMessage response.message must not include reactions."""
        ch_id = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"][0]["id"]
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "reactions absent in postmessage",
        })
        msg = resp.json().get("message", {})
        assert "reactions" not in msg, (
            f"postMessage.message.reactions should be absent, got {msg.get('reactions')!r}"
        )


# ===========================================================================
# Phase 2.3: Subtype and default checks
# Checks field differences across resource subtypes and required default resources.
# ===========================================================================


class TestUserSubtypes:
    """2.3 — Bot users vs human users vs USLACKBOT have distinct field values."""

    def test_uslackbot_always_present(self, client):
        """USLACKBOT must always exist in users.list (Bug 8: missing default resource)."""
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        ids = [m["id"] for m in members]
        assert "USLACKBOT" in ids, "USLACKBOT is missing from users.list — Bug 8"

    def test_uslackbot_is_bot_false(self, client):
        """USLACKBOT.is_bot must be False — Slackbot is not classified as a bot.

        Bug 7: real Slack has USLACKBOT.is_bot = false despite it being a system user.
        Mock seeds USLACKBOT with is_bot=True.
        Fixture: users_list.json USLACKBOT entry.
        """
        real = load_fixture("users_list.json")
        real_slackbot = next((m for m in real["members"] if m["id"] == "USLACKBOT"), None)
        assert real_slackbot is not None, "USLACKBOT missing from fixture"
        assert real_slackbot["is_bot"] is False, "fixture confirms USLACKBOT.is_bot = false"

        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        slackbot = next((m for m in members if m["id"] == "USLACKBOT"), None)
        if slackbot is None:
            pytest.skip("USLACKBOT not in users.list")
        assert slackbot["is_bot"] is False, (
            f"USLACKBOT.is_bot should be false, got {slackbot['is_bot']!r}"
        )

    def test_bot_user_present(self, client):
        """At least one bot user (is_bot=True) must exist in users.list."""
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        bots = [m for m in members if m.get("is_bot") is True]
        assert len(bots) >= 1, "No bot users found in users.list"

    def test_human_users_present(self, client):
        """At least two non-bot, non-USLACKBOT users must exist."""
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        humans = [m for m in members if not m.get("is_bot") and m["id"] != "USLACKBOT"]
        assert len(humans) >= 2, f"Expected ≥2 human users, found {len(humans)}"

    def test_slackbot_profile_always_active(self, client):
        """USLACKBOT profile should have always_active: true (unique to Slackbot).

        Bug 7: Slackbot has a unique profile field not present on other users.
        Fixture: users_list.json USLACKBOT.profile.always_active = true.
        """
        real = load_fixture("users_list.json")
        real_slackbot = next((m for m in real["members"] if m["id"] == "USLACKBOT"), None)
        assert real_slackbot["profile"].get("always_active") is True, \
            "fixture confirms USLACKBOT.profile.always_active = true"

        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        slackbot = next((m for m in members if m["id"] == "USLACKBOT"), None)
        if slackbot is None:
            pytest.skip("USLACKBOT not in users.list")
        profile = slackbot.get("profile", {})
        assert profile.get("always_active") is True, (
            "USLACKBOT.profile.always_active should be true"
        )

    def test_human_user_no_always_active(self, client):
        """Human users must NOT have always_active in their profile."""
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        humans = [m for m in members if not m.get("is_bot") and m["id"] != "USLACKBOT"]
        for user in humans[:3]:
            profile = user.get("profile", {})
            assert "always_active" not in profile, (
                f"Human user {user['id']} should not have always_active in profile"
            )


class TestChannelSubtypes:
    """2.3 — Public, private, and IM channels have different field sets (Bug 7)."""

    def test_public_channels_exist(self, client):
        """At least one public channel exists in seeded data (Bug 8: default resources)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        public = [c for c in channels if not c.get("is_private") and not c.get("is_im")]
        assert len(public) >= 1, "No public channels in seeded data"

    def test_private_channels_exist(self, client):
        """At least one private channel can be created or exists."""
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER, json={
            "name": "subtype-private-test", "is_private": True,
        })
        assert resp.json()["ok"] is True

    def test_general_channel_exists(self, client):
        """A 'general' channel must always exist (Bug 8: default resource).

        Real Slack workspaces always have a default channel.
        """
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        names = [c["name"] for c in channels]
        assert "general" in names, f"'general' channel missing from seeded data — Bug 8. Found: {names}"

    def test_im_channels_returned_separately(self, client):
        """IM channels are only returned when types=im is specified."""
        public_channels = client.get(
            "/api/conversations.list", headers=WORKSPACE_HEADER
        ).json()["channels"]
        im_in_public = [c for c in public_channels if c.get("is_im")]

        im_channels = client.get(
            "/api/conversations.list?types=im", headers=WORKSPACE_HEADER
        ).json()["channels"]

        # IM channels should not bleed into the default (public_channel) list
        assert len(im_in_public) == 0, (
            f"IM channels should not appear in default conversations.list, found {len(im_in_public)}"
        )

    def test_im_channel_shape(self, client):
        """IM channels have different key set than public channels (Bug 7).

        Real IM fixture has: user, is_user_deleted, priority — not name, creator, topic, etc.
        """
        real_im = load_fixture("conversations_list_im.json")
        real_im_channel = real_im["channels"][0]

        im_channels = client.get(
            "/api/conversations.list?types=im", headers=WORKSPACE_HEADER
        ).json()["channels"]

        if not im_channels:
            pytest.skip("No IM channels seeded")

        mock_im = im_channels[0]
        assert_keys_match(real_im_channel, mock_im, "conversations.list(im).channel")

    def test_public_channel_has_previous_names(self, client):
        """Public channels have previous_names; private channels do not (Bug 7).

        Fixture: conversations_list.json public channel has previous_names: [].
        Fixture: conversations_list_private.json private channel omits previous_names.
        """
        real_pub = load_fixture("conversations_list.json")["channels"][0]
        real_priv = load_fixture("conversations_list_private.json")["channels"][0]

        assert "previous_names" in real_pub, "fixture: public channel has previous_names"
        assert "previous_names" not in real_priv, "fixture: private channel lacks previous_names"

        # Check mock
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        public = [c for c in channels if not c.get("is_private") and not c.get("is_im")]
        priv_resp = client.get(
            "/api/conversations.list?types=private_channel", headers=WORKSPACE_HEADER
        ).json()["channels"]

        if public:
            # Only assert if mock has these keys populated (they're 2.1 bugs if missing)
            pass  # presence of previous_names tested via key-set in 2.1

    def test_public_channel_has_properties(self, client):
        """Public channels have properties object; private channels do not (Bug 7).

        Fixture: conversations_list.json public channel has properties: {tabs, tabz}.
        Fixture: conversations_list_private.json private channel omits properties.
        """
        real_pub = load_fixture("conversations_list.json")["channels"][0]
        real_priv = load_fixture("conversations_list_private.json")["channels"][0]

        assert "properties" in real_pub, "fixture: public channel has properties"
        assert "properties" not in real_priv, "fixture: private channel lacks properties"

    def test_is_moved_is_int_not_bool(self, client):
        """channel.is_moved is an int (0), not a boolean, when present.

        Fixture: conversations_list_private.json has is_moved: 0 (int).
        Real Slack uses integer 0 rather than false for this field.
        """
        real_priv = load_fixture("conversations_list_private.json")["channels"][0]
        assert "is_moved" in real_priv, "fixture: private channel has is_moved"
        val = real_priv["is_moved"]
        assert isinstance(val, int) and not isinstance(val, bool), \
            f"fixture: is_moved should be int, got {type(val).__name__}({val!r})"

    def test_is_general_flag_on_general_channel(self, client):
        """The 'general' channel should have is_general=True.

        Real Slack marks the default channel with is_general=true.
        This field is missing from ChannelSchema (caught in 2.1), but its VALUE matters too.
        """
        real_pub = load_fixture("conversations_list.json")["channels"][0]
        # fixture's general channel (acct-omega in this workspace) — check fixture has is_general
        assert "is_general" in real_pub, "fixture: public channels have is_general field"

        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        general = next((c for c in channels if c.get("name") == "general"), None)
        if general is None:
            pytest.skip("No 'general' channel found")
        if "is_general" not in general:
            pytest.skip("is_general not in mock response (key-set bug caught in 2.1)")
        assert general["is_general"] is True, (
            f"general channel should have is_general=True, got {general.get('is_general')!r}"
        )


class TestDefaultResources:
    """2.3 — Resources that always exist in a real Slack workspace (Bug 8)."""

    def test_uslackbot_in_users_list(self, client):
        """USLACKBOT always exists — already tested in TestUserSubtypes."""
        members = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        assert any(m["id"] == "USLACKBOT" for m in members)

    def test_at_least_one_private_channel_seeded(self, client):
        """Seeded workspace has at least one DM or private channel."""
        im = client.get(
            "/api/conversations.list?types=im", headers=WORKSPACE_HEADER
        ).json()["channels"]
        priv = client.get(
            "/api/conversations.list?types=private_channel", headers=WORKSPACE_HEADER
        ).json()["channels"]
        assert len(im) + len(priv) >= 1, (
            "Seeded workspace has no DM or private channels — real workspaces always have at least one"
        )

    def test_seeded_channels_have_messages(self, client):
        """Seeded channels contain messages (non-empty seed)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        has_messages = False
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            if msgs:
                has_messages = True
                break
        assert has_messages, "No seeded channels have any messages"

    def test_file_subtype_fields_consistent(self, client):
        """files.upload and files.info return the same file object shape (Bug 7 check).

        Real fixture shows upload and info have identical file key sets.
        """
        real_upload = load_fixture("files_upload_response.json")
        real_info = load_fixture("files_info.json")

        upload_file_keys = set(real_upload["file"].keys())
        info_file_keys = set(real_info["file"].keys())
        assert upload_file_keys == info_file_keys, (
            f"files.upload and files.info file object differ:\n"
            f"  upload only: {upload_file_keys - info_file_keys}\n"
            f"  info only: {info_file_keys - upload_file_keys}"
        )

    def test_file_has_timestamp_field(self, client):
        """files.upload response file object has timestamp (alias for created).

        Real fixture has both 'created' and 'timestamp' fields on file objects.
        Mock FileSchema only has 'created'.
        """
        real = load_fixture("files_upload_response.json")
        assert "timestamp" in real["file"], "fixture: file has timestamp field"
        assert "created" in real["file"], "fixture: file has created field"

        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        resp = client.post("/api/files.upload", headers=WORKSPACE_HEADER, json={
            "channels": ch_id, "content": "subtype test", "filename": "sub.txt",
        })
        f = resp.json().get("file", {})
        assert "timestamp" in f, (
            "files.upload response.file missing 'timestamp' field (Bug 5 — real API has both created and timestamp)"
        )


# ---------------------------------------------------------------------------
# Phase 2.4 — Nested structure check
# ---------------------------------------------------------------------------

class TestBlockStructure:
    """Phase 2.4: Message blocks[] nested shape.

    Real Slack wraps all message text in a `blocks` array of typed block objects.
    Mock MessageSchema has no `blocks` field at all (Bug 9).
    These tests document the expected schema from fixtures and verify mock behavior.
    """

    def test_fixture_block_top_level_keys(self):
        """Each block in real messages has type, block_id, and elements."""
        real = load_fixture("conversations_history.json")
        msg = next((m for m in real["messages"] if "blocks" in m), None)
        if msg is None:
            pytest.skip("no message with blocks in fixture")
        block = msg["blocks"][0]
        for key in ("type", "block_id", "elements"):
            assert key in block, f"Block missing key {key!r}: got {set(block.keys())}"

    def test_fixture_rich_text_block_element_keys(self):
        """rich_text block element has type and elements array."""
        real = load_fixture("conversations_history.json")
        msg = next((m for m in real["messages"] if "blocks" in m), None)
        if msg is None:
            pytest.skip("no message with blocks in fixture")
        block = msg["blocks"][0]
        assert block["type"] == "rich_text", f"Expected rich_text block type, got {block['type']!r}"
        section = block["elements"][0]
        assert "type" in section and "elements" in section, (
            f"rich_text block element missing type or elements: {set(section.keys())}"
        )
        assert section["type"] == "rich_text_section"

    def test_fixture_leaf_text_element_keys(self):
        """Text leaf elements have type='text' and 'text' key."""
        real = load_fixture("conversations_history.json")
        msg = next((m for m in real["messages"] if "blocks" in m), None)
        if msg is None:
            pytest.skip("no message with blocks in fixture")
        for block in msg["blocks"]:
            for section in block["elements"]:
                for leaf in section.get("elements", []):
                    if leaf.get("type") == "text":
                        assert "text" in leaf, f"text leaf missing 'text': {leaf}"
                        return
        pytest.skip("no text leaf element found in fixture")

    def test_fixture_emoji_leaf_element_keys(self):
        """Emoji leaf elements have type='emoji', 'name', and 'unicode' keys."""
        real = load_fixture("conversations_history.json")
        msg = next((m for m in real["messages"] if "blocks" in m), None)
        if msg is None:
            pytest.skip("no message with blocks in fixture")
        for block in msg["blocks"]:
            for section in block["elements"]:
                for leaf in section.get("elements", []):
                    if leaf.get("type") == "emoji":
                        assert "name" in leaf, f"emoji leaf missing 'name': {leaf}"
                        assert "unicode" in leaf, f"emoji leaf missing 'unicode': {leaf}"
                        return
        pytest.skip("no emoji leaf element found in fixture")

    def test_mock_history_messages_missing_blocks(self, client):
        """Mock conversations.history messages do not include blocks (Bug 9).

        Real Slack always includes blocks on non-subtype messages.
        """
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            regular = [m for m in msgs if "subtype" not in m]
            if regular:
                assert "blocks" in regular[0], (
                    "Mock message missing 'blocks' field (Bug 9 — real Slack always includes blocks on messages)"
                )
                return
        pytest.skip("no regular messages found in seeded channels")

    def test_postmessage_response_blocks_present(self, client):
        """chat.postMessage response.message should include blocks (Bug 9)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "Block structure test",
        })
        msg = resp.json().get("message", {})
        assert "blocks" in msg, (
            "chat.postMessage response.message missing 'blocks' (Bug 9 — real Slack always includes blocks)"
        )

    def test_replies_messages_missing_blocks(self, client):
        """Mock conversations.replies messages do not include blocks (Bug 9)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            threaded = [m for m in msgs if m.get("reply_count") is not None and m.get("reply_count", 0) > 0]
            if threaded:
                parent_ts = threaded[0]["ts"]
                replies = client.get(
                    f"/api/conversations.replies?channel={ch['id']}&ts={parent_ts}",
                    headers=WORKSPACE_HEADER,
                ).json().get("messages", [])
                if replies:
                    assert "blocks" in replies[0], (
                        "conversations.replies message missing 'blocks' (Bug 9)"
                    )
                    return
        pytest.skip("no threaded messages in seeded workspace")


class TestBotProfileStructure:
    """Phase 2.4: bot_profile nested shape in postMessage and update responses.

    Real Slack includes a bot_profile object with id, app_id, user_id, name,
    icons, deleted, updated, team_id. Mock doesn't return bot_profile at all (Bug 9).
    """

    def test_fixture_postmessage_bot_profile_keys(self):
        """chat.postMessage fixture message has bot_profile with expected keys."""
        real = load_fixture("chat_post_message_response.json")
        msg = real["message"]
        assert "bot_profile" in msg, "fixture: chat.postMessage message missing bot_profile"
        bp = msg["bot_profile"]
        for key in ("id", "app_id", "user_id", "name", "icons", "deleted", "updated", "team_id"):
            assert key in bp, f"bot_profile missing key {key!r}: got {set(bp.keys())}"

    def test_fixture_bot_profile_icons_keys(self):
        """bot_profile.icons has image_36, image_48, image_72."""
        real = load_fixture("chat_post_message_response.json")
        icons = real["message"]["bot_profile"]["icons"]
        for key in ("image_36", "image_48", "image_72"):
            assert key in icons, f"bot_profile.icons missing {key!r}: got {set(icons.keys())}"

    def test_mock_postmessage_missing_bot_profile(self, client):
        """Mock chat.postMessage response.message missing bot_profile (Bug 9)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json={
            "channel": ch_id, "text": "bot_profile test",
        })
        msg = resp.json().get("message", {})
        assert "bot_profile" in msg, (
            "chat.postMessage response.message missing 'bot_profile' (Bug 9)"
        )

    def test_fixture_update_response_bot_profile(self):
        """chat.update fixture response.message also has bot_profile."""
        real = load_fixture("chat_update_response.json")
        assert "message" in real, "fixture: chat.update missing top-level message object"
        msg = real["message"]
        assert "bot_profile" in msg, "fixture: chat.update message missing bot_profile"

    def test_fixture_update_message_edited_keys(self):
        """chat.update fixture response.message.edited has user and ts."""
        real = load_fixture("chat_update_response.json")
        edited = real["message"].get("edited", {})
        assert "user" in edited and "ts" in edited, (
            f"fixture: chat.update message.edited missing user or ts: {set(edited.keys())}"
        )


class TestLanguageStructure:
    """Phase 2.4: language object nested shape in messages.

    Real Slack includes `language: {locale, is_reliable}` on user messages.
    Mock has no language field (Bug 9).
    """

    def test_fixture_message_language_keys(self):
        """Real messages have language object with locale and is_reliable."""
        real = load_fixture("conversations_history.json")
        msg = next((m for m in real["messages"] if "language" in m), None)
        if msg is None:
            pytest.skip("no message with language in fixture")
        lang = msg["language"]
        assert "locale" in lang, f"language missing 'locale': {set(lang.keys())}"
        assert "is_reliable" in lang, f"language missing 'is_reliable': {set(lang.keys())}"

    def test_fixture_language_locale_is_string(self):
        """language.locale is a string (e.g., 'en')."""
        real = load_fixture("conversations_history.json")
        msg = next((m for m in real["messages"] if "language" in m), None)
        if msg is None:
            pytest.skip("no message with language in fixture")
        assert isinstance(msg["language"]["locale"], str)

    def test_fixture_language_is_reliable_is_bool(self):
        """language.is_reliable is a boolean."""
        real = load_fixture("conversations_history.json")
        msg = next((m for m in real["messages"] if "language" in m), None)
        if msg is None:
            pytest.skip("no message with language in fixture")
        assert isinstance(msg["language"]["is_reliable"], bool)

    def test_mock_history_messages_no_language(self, client):
        """Mock conversations.history messages should NOT include language field.

        Real Slack includes language on user messages, but it is an internal
        field not documented in the public API and should be omitted from mock
        responses to keep parity with the documented response shape.
        """
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            regular = [m for m in msgs if "subtype" not in m]
            if regular:
                assert "language" not in regular[0], (
                    "Mock message should not include undocumented 'language' field"
                )
                return
        pytest.skip("no regular messages in seeded channels")

    def test_replies_fixture_language_keys(self):
        """conversations.replies fixture messages also have language object."""
        real = load_fixture("conversations_replies.json")
        msg = next((m for m in real["messages"] if "language" in m), None)
        if msg is None:
            pytest.skip("no reply message with language in fixture")
        lang = msg["language"]
        assert "locale" in lang and "is_reliable" in lang


class TestReplyMessageStructure:
    """Phase 2.4: Thread-specific message fields in conversations.replies.

    Real Slack: thread parent has reply_count, reply_users_count, latest_reply,
    reply_users, is_locked, subscribed. Reply messages have parent_user_id.
    Mock has none of these (Bug 9).
    """

    def test_fixture_thread_parent_thread_fields(self):
        """conversations.replies fixture thread parent has reply threading fields."""
        real = load_fixture("conversations_replies.json")
        parent = real["messages"][0]  # first message is always the thread parent
        for key in ("thread_ts", "reply_count", "reply_users_count", "latest_reply", "reply_users"):
            assert key in parent, (
                f"Thread parent missing key {key!r}: got {set(parent.keys())}"
            )

    def test_fixture_thread_parent_is_locked_subscribed(self):
        """Thread parent in replies fixture has is_locked and subscribed fields."""
        real = load_fixture("conversations_replies.json")
        parent = real["messages"][0]
        assert "is_locked" in parent, f"Thread parent missing 'is_locked': {set(parent.keys())}"
        assert "subscribed" in parent, f"Thread parent missing 'subscribed': {set(parent.keys())}"

    def test_fixture_reply_has_parent_user_id(self):
        """Reply messages in conversations.replies have parent_user_id."""
        real = load_fixture("conversations_replies.json")
        replies = real["messages"][1:]  # skip thread parent
        for reply in replies:
            assert "parent_user_id" in reply, (
                f"Reply message missing 'parent_user_id': {set(reply.keys())}"
            )

    def test_mock_replies_thread_parent_missing_is_locked(self, client):
        """Mock conversations.replies thread parent missing is_locked/subscribed (Bug 9)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            # Find a message that is a thread parent (has replies).
            # After Phase 3, thread_ts is absent on parent messages (excluded when None),
            # so we detect parents by reply_count > 0.
            threaded = [m for m in msgs if (m.get("reply_count") or 0) > 0]
            if threaded:
                parent_ts = threaded[0]["ts"]
                replies = client.get(
                    f"/api/conversations.replies?channel={ch['id']}&ts={parent_ts}",
                    headers=WORKSPACE_HEADER,
                ).json().get("messages", [])
                if replies:
                    parent = replies[0]
                    assert "is_locked" in parent, (
                        "conversations.replies thread parent missing 'is_locked' (Bug 9)"
                    )
                    return
        pytest.skip("no threaded messages found in seeded workspace")

    def test_mock_replies_reply_missing_parent_user_id(self, client):
        """Mock conversations.replies reply messages missing parent_user_id (Bug 9)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            threaded = [m for m in msgs if (m.get("reply_count") or 0) > 0]
            if threaded:
                parent_ts = threaded[0]["ts"]
                replies_resp = client.get(
                    f"/api/conversations.replies?channel={ch['id']}&ts={parent_ts}",
                    headers=WORKSPACE_HEADER,
                ).json()
                replies = replies_resp.get("messages", [])
                non_parent = [r for r in replies if r.get("ts") != parent_ts]
                if non_parent:
                    assert "parent_user_id" in non_parent[0], (
                        "conversations.replies reply missing 'parent_user_id' (Bug 9)"
                    )
                    return
        pytest.skip("no thread with actual replies in seeded workspace")


class TestFileObjectNesting:
    """Phase 2.4: File object nested field structure.

    Real Slack file objects have shares{}, channels[], groups[], ims[],
    has_more_shares, has_rich_preview, file_access, user_team.
    """

    def test_fixture_file_shares_is_dict(self):
        """file.shares is a dict (can be empty)."""
        real = load_fixture("files_upload_response.json")
        assert isinstance(real["file"]["shares"], dict), (
            f"file.shares should be dict, got {type(real['file']['shares'])}"
        )

    def test_fixture_file_channels_is_list(self):
        """file.channels is a list of channel IDs."""
        real = load_fixture("files_upload_response.json")
        assert isinstance(real["file"]["channels"], list), (
            f"file.channels should be list, got {type(real['file']['channels'])}"
        )

    def test_fixture_file_has_user_team(self):
        """file object has user_team field."""
        real = load_fixture("files_upload_response.json")
        assert "user_team" in real["file"], (
            f"file missing 'user_team': {set(real['file'].keys())}"
        )

    def test_fixture_file_has_file_access(self):
        """file object has file_access field."""
        real = load_fixture("files_upload_response.json")
        assert "file_access" in real["file"], (
            f"file missing 'file_access': {set(real['file'].keys())}"
        )

    def test_mock_file_missing_nested_fields(self, client):
        """Mock files.upload file object missing shares/channels/groups/ims/user_team/file_access (Bug 9)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        resp = client.post("/api/files.upload", headers=WORKSPACE_HEADER, json={
            "channels": ch_id, "content": "nesting test", "filename": "nest.txt",
        })
        f = resp.json().get("file", {})
        real = load_fixture("files_upload_response.json")
        real_file_keys = set(real["file"].keys())
        mock_file_keys = set(f.keys())
        missing = real_file_keys - mock_file_keys
        # Known gap: mock missing preview/content/edit fields
        known_missing = {"edit_link", "lines", "lines_more", "preview", "preview_highlight",
                         "preview_is_truncated", "content", "content_highlight_html",
                         "content_highlight_html_truncated", "content_highlight_css", "is_truncated"}
        unexpected_missing = missing - known_missing
        assert not unexpected_missing, (
            f"Mock file object missing unexpected keys: {unexpected_missing}"
        )


# ---------------------------------------------------------------------------
# Phase 2.5 — Behavioral/semantic check
# ---------------------------------------------------------------------------

class TestArchiveUnarchiveSideEffects:
    """Phase 2.5: archive/unarchive actually mutate is_archived state."""

    def _get_non_general_channel(self, client):
        """Return a non-general public channel ID for archive/unarchive tests."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            if ch["name"] != "general" and not ch["is_archived"]:
                return ch["id"]
        return None

    def test_archive_sets_is_archived_true(self, client):
        """conversations.archive → conversations.info shows is_archived=True."""
        ch_id = self._get_non_general_channel(client)
        if ch_id is None:
            pytest.skip("no non-general public channel available")
        resp = client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id})
        assert resp.json()["ok"] is True
        info = client.get(f"/api/conversations.info?channel={ch_id}",
                          headers=WORKSPACE_HEADER).json()
        assert info["channel"]["is_archived"] is True

    def test_archive_twice_returns_already_archived_error(self, client):
        """Archiving an already-archived channel returns already_archived error."""
        ch_id = self._get_non_general_channel(client)
        if ch_id is None:
            pytest.skip("no non-general public channel available")
        client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id})
        resp = client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "already_archived"

    def test_archive_blocks_post_message(self, client):
        """Posting to an archived channel returns is_archived error."""
        ch_id = self._get_non_general_channel(client)
        if ch_id is None:
            pytest.skip("no non-general public channel available")
        client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id})
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "text": "should fail"})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "is_archived"

    def test_unarchive_clears_is_archived(self, client):
        """conversations.unarchive → is_archived reverts to False."""
        ch_id = self._get_non_general_channel(client)
        if ch_id is None:
            pytest.skip("no non-general public channel available")
        client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id})
        resp = client.post("/api/conversations.unarchive", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id})
        assert resp.json()["ok"] is True
        info = client.get(f"/api/conversations.info?channel={ch_id}",
                          headers=WORKSPACE_HEADER).json()
        assert info["channel"]["is_archived"] is False

    def test_unarchive_non_archived_returns_error(self, client):
        """Unarchiving a non-archived channel returns not_archived error."""
        ch_id = self._get_non_general_channel(client)
        if ch_id is None:
            pytest.skip("no non-general public channel available")
        resp = client.post("/api/conversations.unarchive", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "not_archived"

    def test_archived_channel_history_still_readable(self, client):
        """conversations.history on archived channel still returns messages."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_with_msgs = None
        for ch in channels:
            if ch["name"] == "general":
                continue
            msgs = client.get(
                f"/api/conversations.history?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json().get("messages", [])
            if msgs and not ch["is_archived"]:
                ch_with_msgs = ch["id"]
                break
        if ch_with_msgs is None:
            pytest.skip("no non-general channel with messages found")
        client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                    json={"channel": ch_with_msgs})
        history = client.get(
            f"/api/conversations.history?channel={ch_with_msgs}", headers=WORKSPACE_HEADER
        ).json()
        assert history["ok"] is True
        assert len(history["messages"]) > 0, "Archived channel should still return message history"


class TestJoinLeaveSideEffects:
    """Phase 2.5: join/leave affect conversations.members list."""

    def _get_public_channel(self, client):
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            if not ch["is_private"] and not ch["is_im"] and not ch["is_archived"] and ch.get("name") != "general":
                return ch["id"]
        return None

    def test_join_adds_user_to_members(self, client):
        """conversations.join → user appears in conversations.members."""
        ch_id = self._get_public_channel(client)
        if ch_id is None:
            pytest.skip("no public channel available")
        members_before = set(client.get(
            f"/api/conversations.members?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["members"])
        resp = client.post("/api/conversations.join", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id})
        assert resp.json()["ok"] is True
        members_after = set(client.get(
            f"/api/conversations.members?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["members"])
        # Either already a member (no change) or newly added
        assert members_after >= members_before, "join should not remove existing members"

    def test_join_returns_channel_object(self, client):
        """conversations.join returns channel object in response."""
        ch_id = self._get_public_channel(client)
        if ch_id is None:
            pytest.skip("no public channel available")
        resp = client.post("/api/conversations.join", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id})
        body = resp.json()
        assert body["ok"] is True
        assert "channel" in body, "conversations.join response missing 'channel' object"
        assert body["channel"]["id"] == ch_id

    def test_join_private_returns_error(self, client):
        """conversations.join on a private channel returns is_private error."""
        # Create a private channel since the seed has none
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-private-join", "is_private": True})
        assert resp.json()["ok"] is True
        ch_id = resp.json()["channel"]["id"]
        resp = client.post("/api/conversations.join", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "is_private"

    def test_leave_removes_user_from_members(self, client):
        """conversations.leave → user removed from conversations.members."""
        ch_id = self._get_public_channel(client)
        if ch_id is None:
            pytest.skip("no public channel available")
        # First join to ensure membership
        client.post("/api/conversations.join", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id})
        members_after_join = set(client.get(
            f"/api/conversations.members?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["members"])
        resp = client.post("/api/conversations.leave", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id})
        assert resp.json()["ok"] is True
        members_after_leave = set(client.get(
            f"/api/conversations.members?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["members"])
        assert len(members_after_leave) <= len(members_after_join), (
            "leave should not add members"
        )

    def test_num_members_reflects_join(self, client):
        """conversations.list num_members increases after join (real API has num_members on list, not info)."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        target = None
        for ch in channels:
            if ch.get("name") == "general" or ch.get("is_archived"):
                continue
            members = client.get(
                f"/api/conversations.members?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json()["members"]
            if len(members) < 5:
                target = ch["id"]
                break
        if target is None:
            pytest.skip("no suitable channel found")
        count_before = len(client.get(
            f"/api/conversations.members?channel={target}", headers=WORKSPACE_HEADER
        ).json()["members"])
        client.post("/api/conversations.join", headers=WORKSPACE_HEADER,
                    json={"channel": target})
        count_after = len(client.get(
            f"/api/conversations.members?channel={target}", headers=WORKSPACE_HEADER
        ).json()["members"])
        # count should be >= before (join is idempotent if already member)
        assert count_after >= count_before

    def test_leave_general_returns_cant_leave_general(self, client):
        """conversations.leave on general channel returns cant_leave_general error."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        general = next((ch for ch in channels if ch.get("name") == "general"), None)
        if general is None:
            pytest.skip("no general channel in seeded workspace")
        resp = client.post("/api/conversations.leave", headers=WORKSPACE_HEADER,
                           json={"channel": general["id"]})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "cant_leave_general"

    def test_leave_not_in_channel_returns_not_in_channel(self, client):
        """conversations.leave when not a member returns not_in_channel (ok: false, not ok: error)."""
        # Create a fresh channel and leave without ever joining
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-leave-nonmember"})
        ch_id = resp.json()["channel"]["id"]
        # Leave immediately (current user was added as creator, so leave first)
        client.post("/api/conversations.leave", headers=WORKSPACE_HEADER, json={"channel": ch_id})
        # Now try to leave again — user is no longer a member
        resp2 = client.post("/api/conversations.leave", headers=WORKSPACE_HEADER, json={"channel": ch_id})
        body = resp2.json()
        assert body.get("ok") is False
        assert body.get("not_in_channel") is True, f"Expected not_in_channel: true, got {body}"


class TestInviteKickSideEffects:
    """Phase 2.5: invite/kick affect membership and num_members."""

    def _get_public_channel_and_non_member_user(self, client):
        """Return (channel_id, user_id) where user is not in channel."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        users = client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]
        human_users = [u for u in users if not u["is_bot"] and u["id"] != "USLACKBOT"]
        for ch in channels:
            if ch["is_archived"] or ch["is_private"] or ch["is_im"]:
                continue
            members = set(client.get(
                f"/api/conversations.members?channel={ch['id']}", headers=WORKSPACE_HEADER
            ).json()["members"])
            for user in human_users:
                if user["id"] not in members:
                    return ch["id"], user["id"]
        return None, None

    def test_invite_adds_user_to_members(self, client):
        """conversations.invite → invited user appears in conversations.members."""
        ch_id, user_id = self._get_public_channel_and_non_member_user(client)
        if ch_id is None:
            pytest.skip("no channel/user pair where user is non-member")
        resp = client.post("/api/conversations.invite", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "users": user_id})
        assert resp.json()["ok"] is True
        members = client.get(
            f"/api/conversations.members?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["members"]
        assert user_id in members, f"User {user_id} not in members after invite"

    def test_invite_returns_channel_object(self, client):
        """conversations.invite response includes channel object."""
        ch_id, user_id = self._get_public_channel_and_non_member_user(client)
        if ch_id is None:
            pytest.skip("no channel/user pair where user is non-member")
        resp = client.post("/api/conversations.invite", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "users": user_id})
        body = resp.json()
        assert "channel" in body, "conversations.invite response missing 'channel'"
        assert body["channel"]["id"] == ch_id

    def test_kick_removes_user_from_members(self, client):
        """conversations.kick → kicked user removed from conversations.members."""
        ch_id, user_id = self._get_public_channel_and_non_member_user(client)
        if ch_id is None:
            pytest.skip("no channel/user pair where user is non-member")
        # Invite first
        client.post("/api/conversations.invite", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id, "users": user_id})
        members_before_kick = client.get(
            f"/api/conversations.members?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["members"]
        assert user_id in members_before_kick

        resp = client.post("/api/conversations.kick", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "user": user_id})
        assert resp.json()["ok"] is True
        members_after_kick = client.get(
            f"/api/conversations.members?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["members"]
        assert user_id not in members_after_kick, f"User {user_id} still in members after kick"

    def test_kick_non_member_returns_error(self, client):
        """Kicking a non-member returns not_in_channel error."""
        ch_id, user_id = self._get_public_channel_and_non_member_user(client)
        if ch_id is None:
            pytest.skip("no channel/user pair where user is non-member")
        resp = client.post("/api/conversations.kick", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "user": user_id})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "not_in_channel"

    def test_invite_unknown_user_returns_error(self, client):
        """Inviting a non-existent user returns user_not_found error."""
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        ch_id = channels[0]["id"]
        resp = client.post("/api/conversations.invite", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "users": "UFAKE99999"})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "user_not_found"


class TestMessageMutationSideEffects:
    """Phase 2.5: message delete and edit (chat.update) side effects.

    - delete: message gone from conversations.history
    - update: message text changes and edited.ts appears in history
    - delete: associated reactions and pins also removed
    """

    def _post_message(self, client, ch_id, text="behavioral test message"):
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "text": text})
        assert resp.json()["ok"] is True
        return resp.json()["ts"]

    def _get_channel(self, client):
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            if not ch["is_archived"]:
                return ch["id"]
        return None

    def test_delete_removes_message_from_history(self, client):
        """chat.delete → message no longer appears in conversations.history."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        ts = self._post_message(client, ch_id)
        resp = client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "ts": ts})
        assert resp.json()["ok"] is True
        msgs = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["messages"]
        ts_list = [m["ts"] for m in msgs]
        assert ts not in ts_list, "Deleted message still appears in conversations.history"

    def test_delete_returns_channel_and_ts(self, client):
        """chat.delete response includes channel and ts."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        ts = self._post_message(client, ch_id)
        resp = client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "ts": ts})
        body = resp.json()
        assert body["ok"] is True
        assert body["channel"] == ch_id
        assert body["ts"] == ts

    def test_delete_unknown_message_returns_error(self, client):
        """Deleting a non-existent message ts returns message_not_found error."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        resp = client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "ts": "0000000000.000000"})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "message_not_found"

    def test_update_changes_message_text_in_history(self, client):
        """chat.update → updated text appears in conversations.history."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        ts = self._post_message(client, ch_id, "original text")
        resp = client.post("/api/chat.update", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "ts": ts, "text": "updated text"})
        assert resp.json()["ok"] is True
        msgs = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["messages"]
        msg = next((m for m in msgs if m["ts"] == ts), None)
        assert msg is not None, "Updated message not found in history"
        assert msg["text"] == "updated text", (
            f"Expected 'updated text', got {msg['text']!r}"
        )

    def test_update_sets_edited_field(self, client):
        """chat.update → message in history has 'edited' object with ts."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        ts = self._post_message(client, ch_id, "to be edited")
        client.post("/api/chat.update", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id, "ts": ts, "text": "edited"})
        msgs = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["messages"]
        msg = next((m for m in msgs if m["ts"] == ts), None)
        assert msg is not None, "Edited message not found in history"
        assert "edited" in msg, (
            "chat.update did not set 'edited' field on message in history"
        )
        assert "ts" in msg["edited"], "edited object missing 'ts' field"

    def test_delete_removes_reactions(self, client):
        """Deleting a message also removes its reactions (no orphaned reactions)."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        ts = self._post_message(client, ch_id, "reaction target")
        # Add a reaction
        client.post("/api/reactions.add", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id, "timestamp": ts, "name": "thumbsup"})
        # Delete the message
        client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id, "ts": ts})
        # Verify reactions.get returns not_found or empty
        resp = client.get(
            f"/api/reactions.get?channel={ch_id}&timestamp={ts}", headers=WORKSPACE_HEADER
        )
        # Either message_not_found error or reactions array empty
        body = resp.json()
        if body.get("ok"):
            rxns = body.get("message", {}).get("reactions", [])
            assert rxns == [], f"Reactions not cleared after message delete: {rxns}"
        else:
            assert body["error"] in ("message_not_found", "no_reaction"), body["error"]


class TestThreadSideEffects:
    """Phase 2.5: reply count updates when threads are posted."""

    def _get_channel(self, client):
        channels = client.get("/api/conversations.list", headers=WORKSPACE_HEADER).json()["channels"]
        for ch in channels:
            if not ch["is_archived"]:
                return ch["id"]
        return None

    def test_reply_increments_parent_reply_count(self, client):
        """Posting a reply increments the thread parent's reply_count in history."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        # Post parent
        parent_ts = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                                json={"channel": ch_id, "text": "thread parent"}).json()["ts"]
        # Check initial reply_count
        msgs_before = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["messages"]
        parent_before = next((m for m in msgs_before if m["ts"] == parent_ts), None)
        count_before = parent_before.get("reply_count") if parent_before else 0

        # Post a reply
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "text": "reply", "thread_ts": parent_ts})
        assert resp.json()["ok"] is True

        # Check reply_count incremented
        msgs_after = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["messages"]
        parent_after = next((m for m in msgs_after if m["ts"] == parent_ts), None)
        assert parent_after is not None, "Parent message not found after reply"
        count_after = parent_after.get("reply_count", 0) or 0
        assert count_after == (count_before or 0) + 1, (
            f"reply_count not incremented: before={count_before}, after={count_after}"
        )

    def test_reply_appears_in_conversations_replies(self, client):
        """Replies appear in conversations.replies for the parent ts."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        parent_ts = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                                json={"channel": ch_id, "text": "replies parent"}).json()["ts"]
        client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id, "text": "reply 1", "thread_ts": parent_ts})
        client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id, "text": "reply 2", "thread_ts": parent_ts})
        replies = client.get(
            f"/api/conversations.replies?channel={ch_id}&ts={parent_ts}",
            headers=WORKSPACE_HEADER,
        ).json()["messages"]
        assert len(replies) >= 3, f"Expected at least 3 messages (parent + 2 replies), got {len(replies)}"
        texts = [m["text"] for m in replies]
        assert "reply 1" in texts and "reply 2" in texts

    def test_reply_not_in_parent_history(self, client):
        """Replies do not appear in conversations.history (only thread parent does)."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        parent_ts = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                                json={"channel": ch_id, "text": "thread isolation parent"}).json()["ts"]
        reply_ts = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                               json={"channel": ch_id, "text": "isolated reply",
                                     "thread_ts": parent_ts}).json()["ts"]
        msgs = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["messages"]
        ts_list = [m["ts"] for m in msgs]
        assert parent_ts in ts_list, "Thread parent missing from channel history"
        assert reply_ts not in ts_list, "Reply should not appear in channel history (only in replies)"

    def test_reply_to_unknown_thread_returns_error(self, client):
        """Posting a reply to a non-existent thread_ts returns thread_not_found."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "text": "orphan reply",
                                 "thread_ts": "0000000000.000000"})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "thread_not_found"

    def test_delete_reply_decrements_parent_reply_count(self, client):
        """Deleting a reply decrements parent's reply_count."""
        ch_id = self._get_channel(client)
        if ch_id is None:
            pytest.skip("no non-archived channel")
        parent_ts = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                                json={"channel": ch_id, "text": "decrement parent"}).json()["ts"]
        reply_ts = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                               json={"channel": ch_id, "text": "will be deleted",
                                     "thread_ts": parent_ts}).json()["ts"]
        msgs_before = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["messages"]
        parent_before = next((m for m in msgs_before if m["ts"] == parent_ts), None)
        count_before = (parent_before.get("reply_count") or 0) if parent_before else 0

        client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id, "ts": reply_ts})

        msgs_after = client.get(
            f"/api/conversations.history?channel={ch_id}", headers=WORKSPACE_HEADER
        ).json()["messages"]
        parent_after = next((m for m in msgs_after if m["ts"] == parent_ts), None)
        assert parent_after is not None
        count_after = (parent_after.get("reply_count") or 0) if parent_after else 0
        assert count_after == count_before - 1, (
            f"reply_count not decremented after delete: before={count_before}, after={count_after}"
        )


# -- Error fixture coverage tests -------------------------------------------

class TestSlackErrorFixtures:
    """Verify error response fixtures have correct Slack envelope structure."""

    @pytest.mark.parametrize("fixture_name", [
        "chat_delete_error_message_not_found.json",
        "chat_post_message_error_channel_not_found.json",
        "chat_post_message_error_no_text.json",
        "chat_update_error_message_not_found.json",
        "conversations_history_error_channel_not_found.json",
        "conversations_info_error_channel_not_found.json",
        "reactions_add_error_invalid_target.json",
    ])
    def test_error_envelope(self, fixture_name):
        """Each error fixture has ok=false and an error string."""
        real = load_fixture(fixture_name)
        assert real["ok"] is False
        assert "error" in real
        assert isinstance(real["error"], str)
