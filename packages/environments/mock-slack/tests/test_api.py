"""Functional CRUD tests for the Slack mock API.

Tests that endpoints actually work end-to-end, not just that they return the
right shape. Complements test_conformance.py.
"""

import re
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

import pytest
from jinja2 import Environment, FileSystemLoader

from mock_slack.models import Message, Reaction, get_session_factory
from mock_slack.web import routes as web_routes

WORKSPACE_HEADER = {"X-Mock-Slack-Workspace": "workspace_001"}
USER_TOKEN_HEADER = {
    **WORKSPACE_HEADER,
    "Authorization": "Bearer mock-user-token",
}
BOT_TOKEN_HEADER = {
    **WORKSPACE_HEADER,
    "Authorization": "Bearer mock-bot-token",
}
TEMPLATES_DIR = Path(__file__).resolve().parents[1] / "mock_slack" / "web" / "templates"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _list_channels(client, **kwargs):
    params = "&".join(f"{k}={v}" for k, v in kwargs.items())
    url = f"/api/conversations.list?{params}" if params else "/api/conversations.list"
    return client.get(url, headers=WORKSPACE_HEADER).json()["channels"]


def _list_members(client, channel_id):
    return client.get(
        f"/api/conversations.members?channel={channel_id}", headers=WORKSPACE_HEADER
    ).json()["members"]


def _list_users(client):
    return client.get("/api/users.list", headers=WORKSPACE_HEADER).json()["members"]


def _post_message(client, channel_id, text, **kwargs):
    body = {"channel": channel_id, "text": text, **kwargs}
    return client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER, json=body).json()


def _get_first_non_general_channel(client):
    channels = _list_channels(client)
    for ch in channels:
        if ch.get("name") != "general" and not ch.get("is_archived"):
            return ch
    return None


def _get_first_human_user(client):
    members = _list_users(client)
    return next(
        (m for m in members if not m["is_bot"] and m["id"] != "USLACKBOT"), None
    )


# ---------------------------------------------------------------------------
# Smoke
# ---------------------------------------------------------------------------

class TestSmoke:
    def test_health(self, client):
        resp = client.get("/health")
        assert resp.status_code == 200
        assert resp.json()["status"] == "ok"

    def test_auth_test(self, client):
        resp = client.post("/api/auth.test", headers=WORKSPACE_HEADER)
        assert resp.status_code == 200
        data = resp.json()
        assert data["ok"] is True
        assert "team" in data
        assert "user_id" in data


class TestWebAvatarMacro:
    @staticmethod
    def _render_avatar_macro(user, fallback_bg="", fallback_text=""):
        template = Environment(loader=FileSystemLoader(str(TEMPLATES_DIR))).from_string(
            '{% from "_avatar_macros.html" import slack_avatar %}'
            '{{ slack_avatar(user=user, fallback_bg=fallback_bg, fallback_text=fallback_text) }}'
        )
        return template.render(
            user=user,
            fallback_bg=fallback_bg,
            fallback_text=fallback_text,
        )

    def test_shared_avatar_macro_uses_silhouette_fallback_markup(self):
        html = (TEMPLATES_DIR / "_avatar_macros.html").read_text()

        assert 'data-default-avatar="true"' in html
        assert "<svg" in html
        assert 'data-default-avatar-silhouette="true"' in html
        assert "display_name[0].upper()" not in html

    def test_shared_avatar_macro_assigns_palette_variants_from_user_id(self):
        def make_user(user_id):
            return SimpleNamespace(
                id=user_id,
                real_name="Fallback User",
                name="fallback-user",
                avatar_url="",
            )

        avatar_0 = self._render_avatar_macro(make_user("U0000"))
        avatar_1 = self._render_avatar_macro(make_user("U0001"))
        avatar_2 = self._render_avatar_macro(make_user("U0002"))
        avatar_3 = self._render_avatar_macro(make_user("U0003"))

        assert 'data-default-avatar-palette="0"' in avatar_0
        assert 'bg-[#ececec]' in avatar_0
        assert 'text-[#1f1f1f]' in avatar_0

        assert 'data-default-avatar-palette="1"' in avatar_1
        assert 'bg-[#e7edf5]' in avatar_1
        assert 'text-[#2f9bd3]' in avatar_1

        assert 'data-default-avatar-palette="2"' in avatar_2
        assert 'bg-[#e8dfc4]' in avatar_2
        assert 'text-[#4d7a92]' in avatar_2

        assert 'data-default-avatar-palette="3"' in avatar_3
        assert 'bg-[#ece9ee]' in avatar_3
        assert 'text-[#5b1f61]' in avatar_3


class TestWebComposer:
    def test_shared_composer_macro_exists(self):
        html = (TEMPLATES_DIR / "_composer_macros.html").read_text()

        assert 'macro render_slack_composer' in html
        assert 'data-slack-composer' in html
        assert 'data-send-button' in html

    def test_shared_composer_macro_uses_slack_like_formatting_controls(self):
        html = (TEMPLATES_DIR / "_composer_macros.html").read_text()

        controls = [
            'aria-label="Bold"',
            'aria-label="Italic"',
            'aria-label="Underline"',
            'aria-label="Strikethrough"',
            'aria-label="Insert link"',
            'aria-label="Ordered list"',
            'aria-label="Bulleted list"',
            'aria-label="Quote"',
            'aria-label="Code"',
            'aria-label="Code block"',
        ]
        for control in controls:
            assert control in html

        positions = [html.index(control) for control in controls]
        assert positions == sorted(positions)
        assert 'data-format-toolbar' in html
        assert 'is-link-icon' in html
        assert 'is-list-icon' in html
        assert 'is-ordered-list-icon' in html
        assert 'is-bulleted-list-icon' in html
        assert 'is-quote-icon' in html
        assert 'is-code-block-icon' in html
        assert 'is-bold-mark' in html
        assert 'is-italic-mark' in html
        assert 'is-underline-mark' in html
        assert 'is-strike-mark' in html
        assert 'is-code-mark' in html
        assert 'is-formatting-group' in html

    def test_shared_composer_macro_uses_slack_like_footer_actions(self):
        html = (TEMPLATES_DIR / "_composer_macros.html").read_text()

        actions = [
            'aria-label="Open insert menu"',
            'aria-label="Toggle formatting options"',
            'aria-label="Add emoji"',
            'aria-label="Mention someone"',
            'aria-label="Start video clip"',
            'aria-label="Record voice message"',
            'aria-label="Use slash command"',
        ]
        for action in actions:
            assert action in html

        assert 'data-format-toggle' in html
        assert 'aria-label="Open canvas tools"' not in html
        assert 'is-tonal-round' in html
        assert 'is-textual-icon' in html
        assert 'is-outline-square' in html
        assert html.count('slack-composer-footer-divider') >= 2
        assert 'is-at-glyph' in html
        assert 'is-slash-glyph' in html
        assert 'is-emoji-icon' in html
        assert 'is-video-icon' in html
        assert 'is-mic-icon' in html
        assert 'is-plus-icon' in html
        assert 'is-send-chevron' in html
        assert 'is-format-toggle-mark' in html
        assert 'is-primary-actions' in html
        assert 'is-send-cluster' in html

    def test_new_message_page_template_contains_richer_composer_shell(self):
        html = (TEMPLATES_DIR / "new_message.html").read_text()

        assert 'render_slack_composer(' in html
        assert "toolbar_id='new-message-toolbar'" in html
        assert "actions_id='new-message-actions'" in html
        assert "target_input_id='new-message-target'" in html
        assert "placeholder_base='Choose a conversation to start typing'" in html

    def test_channel_and_thread_templates_use_shared_composer_macro(self):
        for template_name in [
            "channel.html",
            "channel_inline.html",
            "thread.html",
            "thread_panel.html",
            "threads.html",
        ]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert 'render_slack_composer(' in html, template_name

    def test_new_message_inline_template_contains_matching_composer_hooks(self):
        html = (TEMPLATES_DIR / "new_message_inline.html").read_text()

        assert 'render_slack_composer(' in html
        assert "toolbar_id='new-message-inline-toolbar'" in html
        assert "actions_id='new-message-inline-actions'" in html
        assert "target_input_id='new-message-inline-target'" in html
        assert "placeholder_base='Choose a conversation to start typing'" in html

    def test_base_template_contains_shared_composer_format_toggle_logic(self):
        html = (TEMPLATES_DIR / "base.html").read_text()

        assert "data-format-toggle" in html
        assert "data-format-toolbar" in html
        assert "composerFormatExpanded" in html
        assert "aria-pressed" in html
        assert ".slack-composer-action-button.is-tonal-round" in html
        assert ".slack-composer-action-button.is-outline-square" in html
        assert ".slack-composer-action-button.is-textual-icon" in html
        assert ".slack-composer-action-button.is-at-glyph" in html
        assert ".slack-composer-action-button.is-slash-glyph" in html
        assert ".slack-composer-toolbar-button.is-link-icon" in html
        assert ".slack-composer-toolbar-button.is-list-icon" in html
        assert ".slack-composer-toolbar-button.is-ordered-list-icon" in html
        assert ".slack-composer-toolbar-button.is-bulleted-list-icon" in html
        assert ".slack-composer-toolbar-button.is-quote-icon" in html
        assert ".slack-composer-toolbar-button.is-code-block-icon" in html
        assert ".slack-composer-toolbar-button.is-bold-mark" in html
        assert ".slack-composer-toolbar-button.is-italic-mark" in html
        assert ".slack-composer-toolbar-button.is-underline-mark" in html
        assert ".slack-composer-toolbar-button.is-strike-mark" in html
        assert ".slack-composer-toolbar-button.is-code-mark" in html
        assert ".slack-composer-toolbar-group.is-formatting-group" in html
        assert ".slack-composer-action-button.is-emoji-icon" in html
        assert ".slack-composer-action-button.is-video-icon" in html
        assert ".slack-composer-action-button.is-mic-icon" in html
        assert ".slack-composer-action-button.is-plus-icon" in html
        assert ".slack-composer-action-button.is-format-toggle-mark" in html
        assert ".slack-composer-send-option.is-send-chevron" in html
        assert ".slack-composer-footer-group.is-primary-actions" in html
        assert ".slack-composer-footer-group.is-send-cluster" in html
        assert ".slack-composer-body" in html

    def test_shared_composer_macro_exposes_dedicated_body_region(self):
        html = (TEMPLATES_DIR / "_composer_macros.html").read_text()

        assert 'class="slack-composer-body"' in html


class TestWebMessageLayout:
    def test_message_templates_include_realistic_stream_hooks(self):
        for template_name in [
            "channel.html",
            "channel_inline.html",
            "thread.html",
            "thread_panel.html",
        ]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert 'data-message-stream="true"' in html, template_name
            assert "slack-message-row" in html, template_name
            assert "slack-message-actions" in html, template_name

    def test_channel_templates_include_continuation_and_thread_hooks(self):
        for template_name in ["channel.html", "channel_inline.html"]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert "slack-message-row--continuation" in html, template_name
            assert "slack-thread-summary" in html, template_name
            assert "slack-date-divider" in html, template_name
            assert "render_link_unfurl" in html, template_name

    def test_channel_template_includes_new_messages_pill(self):
        html = (TEMPLATES_DIR / "channel.html").read_text()
        assert "slack-new-messages-pill" in html

    def test_message_templates_use_shared_timestamp_formatter(self):
        base_html = (TEMPLATES_DIR / "base.html").read_text()

        assert "function formatSlackMessageTimestamp" in base_html

        for template_name in [
            "channel.html",
            "channel_inline.html",
            "thread.html",
            "thread_panel.html",
        ]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert "formatSlackMessageTimestamp(" in html, template_name
            assert "toLocaleTimeString" not in html, template_name

    def test_thread_templates_include_richer_context_and_message_content_blocks(self):
        for template_name in ["thread.html", "thread_panel.html"]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert "slack-thread-header" in html, template_name
            assert "slack-thread-subtitle" in html, template_name
            assert "slack-thread-parent-context" in html, template_name
            assert "render_link_unfurl" in html, template_name
            assert "render_attachments" in html, template_name

    def test_shared_message_macros_include_link_unfurl_and_attachment_structure(self):
        html = (TEMPLATES_DIR / "_message_macros.html").read_text()
        assert "slack-link-unfurl" in html
        assert "slack-message-attachment" in html
        assert "slack-message-attachment-meta" in html
        assert "slack-message-attachment-source" in html

    def test_message_templates_include_floating_action_bar_hooks(self):
        base_html = (TEMPLATES_DIR / "base.html").read_text()
        assert "slack-message-actions--floating" in base_html

        for template_name in [
            "channel.html",
            "channel_inline.html",
            "thread.html",
            "thread_panel.html",
        ]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert "slack-message-actions slack-message-actions--floating" in html, template_name

    def test_message_styles_stack_sender_above_message_body(self):
        base_html = (TEMPLATES_DIR / "base.html").read_text()

        avatar_slot_match = re.search(r"\.slack-message-avatar-slot\s*\{(?P<body>[^}]+)\}", base_html)
        assert avatar_slot_match is not None
        avatar_slot_block = avatar_slot_match.group("body")
        assert "align-items: flex-start;" in avatar_slot_block

        content_match = re.search(r"\.slack-message-content\s*\{(?P<body>[^}]+)\}", base_html)
        assert content_match is not None
        content_block = content_match.group("body")
        assert "display: flex;" not in content_block
        assert "flex-wrap: wrap;" not in content_block

        text_match = re.search(r"\.slack-message-text\s*\{(?P<body>[^}]+)\}", base_html)
        assert text_match is not None
        text_block = text_match.group("body")
        assert "flex:" not in text_block

    def test_channel_templates_include_thread_summary_separator(self):
        for template_name in ["channel.html", "channel_inline.html"]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert "slack-thread-summary-separator" in html, template_name

    def test_message_templates_include_continuation_gutter_timestamp(self):
        base_html = (TEMPLATES_DIR / "base.html").read_text()
        assert "slack-message-gutter-time" in base_html

        for template_name in [
            "channel.html",
            "channel_inline.html",
            "thread.html",
            "thread_panel.html",
        ]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert "slack-message-gutter-time" in html, template_name

    def test_channel_templates_use_explicit_date_divider_label_structure(self):
        for template_name in ["channel.html", "channel_inline.html"]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert "slack-date-divider-label" in html, template_name
            assert "slack-date-divider-caret" in html, template_name

    def test_pre_wrap_message_blocks_do_not_preserve_template_indentation(self):
        pattern = re.compile(r'class="slack-message-text[^"]*"\s*>\s+\{\{')

        for template_name in [
            "channel.html",
            "channel_inline.html",
            "thread.html",
        ]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert pattern.search(html) is None, template_name

    def test_message_templates_use_shared_rich_text_renderer(self):
        for template_name in [
            "channel.html",
            "channel_inline.html",
            "thread.html",
            "thread_panel.html",
        ]:
            html = (TEMPLATES_DIR / template_name).read_text()
            assert "slack_render_message_text(" in html, template_name


class TestWebMessageViewHelpers:
    def test_date_divider_label_uses_slack_style_for_older_days(self):
        now = datetime(2026, 4, 8, 12, 0)
        value = datetime(2025, 5, 15, 15, 21)

        assert web_routes._slack_date_divider_label(value, now=now) == "May 15th, 2025"

    def test_reply_summary_label_uses_relative_age_copy(self):
        now = datetime(2026, 4, 8, 12, 0)
        value = datetime(2025, 5, 8, 9, 30)

        assert web_routes._slack_reply_summary_label(value, now=now) == "Last reply 11 months ago"

    def test_message_continuation_requires_same_author_and_short_gap(self):
        continuation = getattr(web_routes, "_slack_is_message_continuation", None)
        assert callable(continuation)

        prev = SimpleNamespace(
            user=SimpleNamespace(id="U123"),
            created_at=datetime(2026, 4, 8, 9, 0),
            ts="1744102800.000100",
        )
        close_next = SimpleNamespace(
            user=SimpleNamespace(id="U123"),
            created_at=datetime(2026, 4, 8, 9, 3),
            ts="1744102980.000200",
        )
        far_next = SimpleNamespace(
            user=SimpleNamespace(id="U123"),
            created_at=datetime(2026, 4, 8, 9, 9),
            ts="1744103340.000300",
        )

        assert continuation(prev, close_next) is True
        assert continuation(prev, far_next) is False

    def test_rich_text_renderer_converts_known_emoji_tokens(self):
        renderer = getattr(web_routes, "_slack_render_message_text", None)
        assert callable(renderer)

        html = str(renderer("Ship it :tada:"))

        assert "slack-inline-emoji" in html
        assert "🎉" in html
        assert ":tada:" not in html

    def test_rich_text_renderer_wraps_inline_code(self):
        renderer = getattr(web_routes, "_slack_render_message_text", None)
        assert callable(renderer)

        html = str(renderer("Run `npm test` now"))

        assert "slack-inline-code" in html
        assert "<code" in html
        assert "npm test" in html

    def test_rich_text_renderer_escapes_html(self):
        renderer = getattr(web_routes, "_slack_render_message_text", None)
        assert callable(renderer)

        html = str(renderer("<script>alert(1)</script>"))

        assert "<script>" not in html
        assert "&lt;script&gt;" in html

    def test_rich_text_renderer_does_not_convert_emoji_inside_code(self):
        renderer = getattr(web_routes, "_slack_render_message_text", None)
        assert callable(renderer)

        html = str(renderer("`echo :tada:` then :tada:"))

        assert html.count("🎉") == 1
        assert ":tada:" in html

    def test_rich_text_renderer_preserves_unknown_emoji_tokens(self):
        renderer = getattr(web_routes, "_slack_render_message_text", None)
        assert callable(renderer)

        html = str(renderer("Need custom :party-parrot: support later"))

        assert ":party-parrot:" in html


# ---------------------------------------------------------------------------
# Attachment footer normalization (no DB needed for passthrough paths)
# ---------------------------------------------------------------------------

class TestNormalizeAttachmentFooter:
    def test_passthrough_when_none(self):
        result = web_routes._normalize_attachment_footer(
            None, workspace_id="w1", current_user_id="u1", footer=None
        )
        assert result is None

    def test_passthrough_when_empty(self):
        result = web_routes._normalize_attachment_footer(
            None, workspace_id="w1", current_user_id="u1", footer=""
        )
        assert result == ""

    def test_passthrough_when_no_dm(self):
        result = web_routes._normalize_attachment_footer(
            None, workspace_id="w1", current_user_id="u1", footer="#general · Today"
        )
        assert result == "#general · Today"

    def test_passthrough_plain_channel_name(self):
        result = web_routes._normalize_attachment_footer(
            None, workspace_id="w1", current_user_id="u1", footer="random"
        )
        assert result == "random"


class TestExtractFirstUrl:
    def test_extracts_slack_formatted_url(self):
        assert web_routes._extract_first_url("Check <https://example.com|Example>") == "https://example.com"

    def test_extracts_plain_url(self):
        assert web_routes._extract_first_url("Visit https://example.com today") == "https://example.com"

    def test_strips_trailing_punctuation_from_plain_url(self):
        assert web_routes._extract_first_url("See https://example.com.") == "https://example.com"
        assert web_routes._extract_first_url("See https://example.com,") == "https://example.com"

    def test_returns_none_for_no_url(self):
        assert web_routes._extract_first_url("No URLs here") is None

    def test_returns_none_for_empty_input(self):
        assert web_routes._extract_first_url(None) is None
        assert web_routes._extract_first_url("") is None


class TestBuildLinkPreview:
    def test_extracts_domain_and_title_from_path(self):
        preview = web_routes._build_link_preview("Check https://www.example.com/blog/my-post")
        assert preview["domain"] == "example.com"
        assert preview["title"] == "My post"
        assert preview["url"] == "https://www.example.com/blog/my-post"

    def test_returns_none_for_no_url(self):
        assert web_routes._build_link_preview("No link here") is None

    def test_returns_none_for_none(self):
        assert web_routes._build_link_preview(None) is None

    def test_uses_domain_as_title_fallback(self):
        preview = web_routes._build_link_preview("https://example.com")
        assert preview["title"] == "Example.com"


class TestSlackOrdinal:
    def test_ordinal_suffixes(self):
        assert web_routes._slack_ordinal(1) == "st"
        assert web_routes._slack_ordinal(2) == "nd"
        assert web_routes._slack_ordinal(3) == "rd"
        assert web_routes._slack_ordinal(4) == "th"
        assert web_routes._slack_ordinal(11) == "th"
        assert web_routes._slack_ordinal(12) == "th"
        assert web_routes._slack_ordinal(13) == "th"
        assert web_routes._slack_ordinal(21) == "st"
        assert web_routes._slack_ordinal(22) == "nd"
        assert web_routes._slack_ordinal(23) == "rd"
        assert web_routes._slack_ordinal(31) == "st"


class TestSlackMessageDatetime:
    def test_returns_none_for_none_message(self):
        assert web_routes._slack_message_datetime(None) is None

    def test_uses_created_at_when_present(self):
        msg = SimpleNamespace(created_at=datetime(2026, 4, 8, 12, 0), ts="0")
        assert web_routes._slack_message_datetime(msg) == datetime(2026, 4, 8, 12, 0)

    def test_falls_back_to_ts(self):
        msg = SimpleNamespace(created_at=None, ts="1744102800.000100")
        result = web_routes._slack_message_datetime(msg)
        assert isinstance(result, datetime)

    def test_returns_none_for_invalid_ts(self):
        msg = SimpleNamespace(created_at=None, ts="not_a_number")
        assert web_routes._slack_message_datetime(msg) is None


# ---------------------------------------------------------------------------
# Channel lifecycle
# ---------------------------------------------------------------------------

class TestChannelLifecycle:
    def test_create_channel(self, client):
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-lifecycle"})
        assert resp.json()["ok"] is True
        ch = resp.json()["channel"]
        assert ch["name"] == "test-lifecycle"
        assert ch["is_private"] is False

    def test_create_private_channel(self, client):
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-private", "is_private": True})
        assert resp.json()["ok"] is True
        assert resp.json()["channel"]["is_private"] is True

    def test_create_duplicate_name_fails(self, client):
        client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                    json={"name": "test-dup"})
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-dup"})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "name_taken"

    def test_rename_channel(self, client):
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-rename-src"})
        ch_id = resp.json()["channel"]["id"]
        rename = client.post("/api/conversations.rename", headers=WORKSPACE_HEADER,
                             json={"channel": ch_id, "name": "test-rename-dst"})
        assert rename.json()["ok"] is True
        info = client.get(f"/api/conversations.info?channel={ch_id}",
                          headers=WORKSPACE_HEADER).json()
        assert info["channel"]["name"] == "test-rename-dst"

    def test_set_topic(self, client):
        ch = _get_first_non_general_channel(client)
        resp = client.post("/api/conversations.setTopic", headers=WORKSPACE_HEADER,
                           json={"channel": ch["id"], "topic": "New topic"})
        assert resp.json()["ok"] is True
        info = client.get(f"/api/conversations.info?channel={ch['id']}",
                          headers=WORKSPACE_HEADER).json()
        assert info["channel"]["topic"]["value"] == "New topic"

    def test_set_purpose(self, client):
        ch = _get_first_non_general_channel(client)
        resp = client.post("/api/conversations.setPurpose", headers=WORKSPACE_HEADER,
                           json={"channel": ch["id"], "purpose": "New purpose"})
        assert resp.json()["ok"] is True
        info = client.get(f"/api/conversations.info?channel={ch['id']}",
                          headers=WORKSPACE_HEADER).json()
        assert info["channel"]["purpose"]["value"] == "New purpose"

    def test_archive_unarchive(self, client):
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-archive-cycle"})
        ch_id = resp.json()["channel"]["id"]

        # Archive
        arc = client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                          json={"channel": ch_id})
        assert arc.json()["ok"] is True
        info = client.get(f"/api/conversations.info?channel={ch_id}",
                          headers=WORKSPACE_HEADER).json()
        assert info["channel"]["is_archived"] is True

        # Unarchive
        unarc = client.post("/api/conversations.unarchive", headers=WORKSPACE_HEADER,
                            json={"channel": ch_id})
        assert unarc.json()["ok"] is True
        info2 = client.get(f"/api/conversations.info?channel={ch_id}",
                           headers=WORKSPACE_HEADER).json()
        assert info2["channel"]["is_archived"] is False

    def test_info_channel_not_found(self, client):
        resp = client.get("/api/conversations.info?channel=CNOTEXIST",
                          headers=WORKSPACE_HEADER)
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "channel_not_found"

    def test_list_excludes_archived_when_requested(self, client):
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-archived-filter"})
        ch_id = resp.json()["channel"]["id"]
        client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id})

        all_chs = _list_channels(client)
        filtered = _list_channels(client, exclude_archived="true")
        all_ids = {c["id"] for c in all_chs}
        filtered_ids = {c["id"] for c in filtered}
        assert ch_id in all_ids
        assert ch_id not in filtered_ids

    def test_list_pagination_cursor(self, client):
        resp = client.get("/api/conversations.list?limit=2", headers=WORKSPACE_HEADER)
        data = resp.json()
        assert data["ok"] is True
        assert len(data["channels"]) <= 2
        # next_cursor present in response_metadata
        assert "response_metadata" in data


# ---------------------------------------------------------------------------
# Membership: invite, kick, join, leave
# ---------------------------------------------------------------------------

class TestMembership:
    def test_invite_and_kick(self, client):
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-membership"})
        ch_id = resp.json()["channel"]["id"]

        user = _get_first_human_user(client)
        assert user is not None

        # Invite
        inv = client.post("/api/conversations.invite", headers=WORKSPACE_HEADER,
                          json={"channel": ch_id, "users": user["id"]})
        assert inv.json()["ok"] is True
        assert user["id"] in _list_members(client, ch_id)

        # Kick
        kick = client.post("/api/conversations.kick", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id, "user": user["id"]})
        assert kick.json()["ok"] is True
        assert user["id"] not in _list_members(client, ch_id)

    def test_join_and_leave(self, client):
        ch = _get_first_non_general_channel(client)
        assert ch is not None
        user = _get_first_human_user(client)
        assert user is not None

        client.post("/api/conversations.join", headers=USER_TOKEN_HEADER,
                    json={"channel": ch["id"]})
        members_after_join = _list_members(client, ch["id"])

        client.post("/api/conversations.leave", headers=USER_TOKEN_HEADER,
                    json={"channel": ch["id"]})
        members_after_leave = _list_members(client, ch["id"])

        assert len(members_after_leave) <= len(members_after_join)
        assert user["id"] in members_after_join
        assert user["id"] not in members_after_leave

    def test_cannot_join_private_channel(self, client):
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-join-private", "is_private": True})
        ch_id = resp.json()["channel"]["id"]
        join = client.post("/api/conversations.join", headers=WORKSPACE_HEADER,
                           json={"channel": ch_id})
        assert join.json()["ok"] is False

    def test_cannot_leave_general(self, client):
        channels = _list_channels(client)
        general = next((c for c in channels if c.get("name") == "general"), None)
        if general is None:
            pytest.skip("no general channel in seed")
        resp = client.post("/api/conversations.leave", headers=WORKSPACE_HEADER,
                           json={"channel": general["id"]})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "cant_leave_general"

    def test_leave_not_in_channel(self, client):
        ch = _get_first_non_general_channel(client)
        assert ch is not None
        user = _get_first_human_user(client)
        assert user is not None

        if user["id"] not in _list_members(client, ch["id"]):
            join = client.post("/api/conversations.join", headers=USER_TOKEN_HEADER,
                               json={"channel": ch["id"]})
            assert join.json()["ok"] is True

        first_leave = client.post("/api/conversations.leave", headers=USER_TOKEN_HEADER,
                                  json={"channel": ch["id"]})
        assert first_leave.json()["ok"] is True

        resp2 = client.post("/api/conversations.leave", headers=USER_TOKEN_HEADER,
                            json={"channel": ch["id"]})
        assert resp2.json()["ok"] is False
        assert resp2.json().get("not_in_channel") is True

    def test_invite_unknown_user_fails(self, client):
        ch = _get_first_non_general_channel(client)
        resp = client.post("/api/conversations.invite", headers=WORKSPACE_HEADER,
                           json={"channel": ch["id"], "users": "UNOTEXIST"})
        assert resp.json()["ok"] is False


# ---------------------------------------------------------------------------
# Message lifecycle
# ---------------------------------------------------------------------------

class TestMessageLifecycle:
    def test_post_and_history(self, client):
        ch = _get_first_non_general_channel(client)
        post = _post_message(client, ch["id"], "Hello, world!")
        assert post["ok"] is True
        ts = post["ts"]

        history = client.get(f"/api/conversations.history?channel={ch['id']}",
                             headers=WORKSPACE_HEADER).json()
        texts = [m["text"] for m in history["messages"]]
        assert "Hello, world!" in texts

    def test_update_message(self, client):
        ch = _get_first_non_general_channel(client)
        post = _post_message(client, ch["id"], "Original text")
        ts = post["ts"]

        update = client.post("/api/chat.update", headers=WORKSPACE_HEADER,
                             json={"channel": ch["id"], "ts": ts, "text": "Updated text"})
        assert update.json()["ok"] is True

        history = client.get(f"/api/conversations.history?channel={ch['id']}",
                             headers=WORKSPACE_HEADER).json()
        msg = next((m for m in history["messages"] if m["ts"] == ts), None)
        assert msg is not None
        assert msg["text"] == "Updated text"
        assert "edited" in msg

    def test_delete_message(self, client):
        ch = _get_first_non_general_channel(client)
        post = _post_message(client, ch["id"], "Delete me")
        ts = post["ts"]

        delete = client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                             json={"channel": ch["id"], "ts": ts})
        assert delete.json()["ok"] is True

        history = client.get(f"/api/conversations.history?channel={ch['id']}",
                             headers=WORKSPACE_HEADER).json()
        tss = [m["ts"] for m in history["messages"]]
        assert ts not in tss

    def test_delete_unknown_ts_fails(self, client):
        ch = _get_first_non_general_channel(client)
        resp = client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                           json={"channel": ch["id"], "ts": "0000000000.000000"})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "message_not_found"

    def test_post_to_archived_channel_fails(self, client):
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-archived-post"})
        ch_id = resp.json()["channel"]["id"]
        client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id})
        post = _post_message(client, ch_id, "This should fail")
        assert post["ok"] is False
        assert post["error"] == "is_archived"


# ---------------------------------------------------------------------------
# Reactions
# ---------------------------------------------------------------------------

class TestReactions:
    def test_add_and_remove_reaction(self, client):
        ch = _get_first_non_general_channel(client)
        post = _post_message(client, ch["id"], "React to me")
        ts = post["ts"]

        add = client.post("/api/reactions.add", headers=WORKSPACE_HEADER,
                          json={"channel": ch["id"], "timestamp": ts, "name": "thumbsup"})
        assert add.json()["ok"] is True

        get = client.get(
            f"/api/reactions.get?channel={ch['id']}&timestamp={ts}",
            headers=WORKSPACE_HEADER,
        ).json()
        reaction_names = [r["name"] for r in get["message"].get("reactions", [])]
        assert "thumbsup" in reaction_names

        remove = client.post("/api/reactions.remove", headers=WORKSPACE_HEADER,
                             json={"channel": ch["id"], "timestamp": ts, "name": "thumbsup"})
        assert remove.json()["ok"] is True

        get2 = client.get(
            f"/api/reactions.get?channel={ch['id']}&timestamp={ts}",
            headers=WORKSPACE_HEADER,
        ).json()
        reaction_names2 = [r["name"] for r in get2["message"].get("reactions", [])]
        assert "thumbsup" not in reaction_names2

    def test_delete_clears_reactions(self, client, seeded_db):
        ch = _get_first_non_general_channel(client)
        post = _post_message(client, ch["id"], "React then delete")
        ts = post["ts"]
        client.post("/api/reactions.add", headers=WORKSPACE_HEADER,
                    json={"channel": ch["id"], "timestamp": ts, "name": "heart"})

        session = get_session_factory(seeded_db)()
        try:
            message_id = session.query(Message).filter(Message.ts == ts).one().id
            reaction_count = session.query(Reaction).filter(
                Reaction.message_id == message_id,
            ).count()
        finally:
            session.close()
        assert reaction_count >= 1

        client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                    json={"channel": ch["id"], "ts": ts})

        history = client.get(f"/api/conversations.history?channel={ch['id']}",
                             headers=WORKSPACE_HEADER).json()
        assert not any(m["ts"] == ts for m in history["messages"])

        session = get_session_factory(seeded_db)()
        try:
            reaction_count = session.query(Reaction).filter(
                Reaction.message_id == message_id,
            ).count()
        finally:
            session.close()
        assert reaction_count == 0


# ---------------------------------------------------------------------------
# Pins
# ---------------------------------------------------------------------------

class TestPins:
    def test_pin_and_unpin(self, client):
        ch = _get_first_non_general_channel(client)
        post = _post_message(client, ch["id"], "Pin me")
        ts = post["ts"]

        add = client.post("/api/pins.add", headers=WORKSPACE_HEADER,
                          json={"channel": ch["id"], "timestamp": ts})
        assert add.json()["ok"] is True

        pins = client.get(f"/api/pins.list?channel={ch['id']}",
                          headers=WORKSPACE_HEADER).json()
        pin_tss = [p["message"]["ts"] for p in pins.get("items", [])
                   if p.get("type") == "message"]
        assert ts in pin_tss

        remove = client.post("/api/pins.remove", headers=WORKSPACE_HEADER,
                             json={"channel": ch["id"], "timestamp": ts})
        assert remove.json()["ok"] is True

        pins2 = client.get(f"/api/pins.list?channel={ch['id']}",
                           headers=WORKSPACE_HEADER).json()
        pin_tss2 = [p["message"]["ts"] for p in pins2.get("items", [])
                    if p.get("type") == "message"]
        assert ts not in pin_tss2


# ---------------------------------------------------------------------------
# Threads
# ---------------------------------------------------------------------------

class TestThreads:
    def test_thread_reply_lifecycle(self, client):
        ch = _get_first_non_general_channel(client)
        parent = _post_message(client, ch["id"], "Thread parent")
        parent_ts = parent["ts"]

        reply = _post_message(client, ch["id"], "Thread reply",
                              thread_ts=parent_ts)
        assert reply["ok"] is True
        reply_ts = reply["ts"]

        # Reply appears in conversations.replies
        replies = client.get(
            f"/api/conversations.replies?channel={ch['id']}&ts={parent_ts}",
            headers=WORKSPACE_HEADER,
        ).json()["messages"]
        reply_tss = [m["ts"] for m in replies]
        assert parent_ts in reply_tss
        assert reply_ts in reply_tss

        # Reply does NOT appear in channel history
        history = client.get(f"/api/conversations.history?channel={ch['id']}",
                             headers=WORKSPACE_HEADER).json()["messages"]
        assert not any(m["ts"] == reply_ts for m in history)

    def test_reply_increments_parent_reply_count(self, client):
        ch = _get_first_non_general_channel(client)
        parent = _post_message(client, ch["id"], "Parent for count")
        parent_ts = parent["ts"]

        history_before = client.get(
            f"/api/conversations.history?channel={ch['id']}",
            headers=WORKSPACE_HEADER,
        ).json()["messages"]
        parent_msg_before = next(m for m in history_before if m["ts"] == parent_ts)
        count_before = parent_msg_before.get("reply_count", 0)

        _post_message(client, ch["id"], "Reply 1", thread_ts=parent_ts)

        history_after = client.get(
            f"/api/conversations.history?channel={ch['id']}",
            headers=WORKSPACE_HEADER,
        ).json()["messages"]
        parent_msg_after = next(m for m in history_after if m["ts"] == parent_ts)
        assert parent_msg_after.get("reply_count", 0) == count_before + 1

    def test_delete_reply_decrements_count(self, client):
        ch = _get_first_non_general_channel(client)
        parent = _post_message(client, ch["id"], "Parent for delete-reply")
        parent_ts = parent["ts"]
        reply = _post_message(client, ch["id"], "Reply to delete",
                              thread_ts=parent_ts)
        reply_ts = reply["ts"]

        client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                    json={"channel": ch["id"], "ts": reply_ts})

        history = client.get(
            f"/api/conversations.history?channel={ch['id']}",
            headers=WORKSPACE_HEADER,
        ).json()["messages"]
        parent_msg = next(m for m in history if m["ts"] == parent_ts)
        assert parent_msg.get("reply_count", 0) == 0

    def test_unknown_thread_ts_returns_error(self, client):
        ch = _get_first_non_general_channel(client)
        resp = client.post("/api/chat.postMessage", headers=WORKSPACE_HEADER,
                           json={"channel": ch["id"], "text": "reply",
                                 "thread_ts": "0000000000.000000"})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "thread_not_found"


# ---------------------------------------------------------------------------
# Files
# ---------------------------------------------------------------------------

class TestFiles:
    def test_upload_info_list_delete(self, client):
        ch = _get_first_non_general_channel(client)

        # Upload
        upload = client.post("/api/files.upload", headers=WORKSPACE_HEADER,
                             json={"channels": ch["id"], "filename": "test.txt",
                                   "content": "Hello file"})
        assert upload.json()["ok"] is True
        file_id = upload.json()["file"]["id"]

        # Info
        info = client.get(f"/api/files.info?file={file_id}",
                          headers=WORKSPACE_HEADER).json()
        assert info["ok"] is True
        assert info["file"]["id"] == file_id

        # List
        files = client.get("/api/files.list", headers=WORKSPACE_HEADER).json()
        file_ids = [f["id"] for f in files["files"]]
        assert file_id in file_ids

        # Delete
        delete = client.post("/api/files.delete", headers=WORKSPACE_HEADER,
                             json={"file": file_id})
        assert delete.json()["ok"] is True

        # Verify gone
        files2 = client.get("/api/files.list", headers=WORKSPACE_HEADER).json()
        file_ids2 = [f["id"] for f in files2["files"]]
        assert file_id not in file_ids2

    def test_file_info_not_found(self, client):
        resp = client.get("/api/files.info?file=FNOTEXIST",
                          headers=WORKSPACE_HEADER)
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "file_not_found"


# ---------------------------------------------------------------------------
# Users
# ---------------------------------------------------------------------------

class TestUsers:
    def test_list_users(self, client):
        resp = client.get("/api/users.list", headers=WORKSPACE_HEADER)
        assert resp.json()["ok"] is True
        members = resp.json()["members"]
        assert len(members) > 0

    def test_users_info(self, client):
        user = _get_first_human_user(client)
        resp = client.get(f"/api/users.info?user={user['id']}",
                          headers=WORKSPACE_HEADER)
        assert resp.json()["ok"] is True
        assert resp.json()["user"]["id"] == user["id"]

    def test_users_info_not_found(self, client):
        resp = client.get("/api/users.info?user=UNOTEXIST",
                          headers=WORKSPACE_HEADER)
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "user_not_found"

    def test_lookup_by_email(self, client):
        members = _list_users(client)
        user = next(
            (m for m in members if not m["is_bot"] and m["profile"].get("email")),
            None,
        )
        if user is None:
            pytest.skip("no user with email in seed")
        email = user["profile"]["email"]
        resp = client.get(f"/api/users.lookupByEmail?email={email}",
                          headers=WORKSPACE_HEADER)
        assert resp.json()["ok"] is True
        assert resp.json()["user"]["id"] == user["id"]

    def test_get_and_set_presence(self, client):
        user = _get_first_human_user(client)
        get = client.get(f"/api/users.getPresence?user={user['id']}",
                         headers=WORKSPACE_HEADER).json()
        assert get["ok"] is True
        assert get["presence"] in ("active", "away")

        set_resp = client.post("/api/users.setPresence", headers=USER_TOKEN_HEADER,
                               json={"presence": "away"})
        assert set_resp.json()["ok"] is True
        get_after = client.get(f"/api/users.getPresence?user={user['id']}",
                               headers=WORKSPACE_HEADER).json()
        assert get_after["presence"] == "away"

    def test_profile_get_and_set(self, client):
        user = _get_first_human_user(client)
        get = client.get(f"/api/users.profile.get?user={user['id']}",
                         headers=WORKSPACE_HEADER).json()
        assert get["ok"] is True
        assert "profile" in get

        set_resp = client.post("/api/users.profile.set", headers=WORKSPACE_HEADER,
                               json={"user": user["id"],
                                     "profile": {"status_text": "On vacation",
                                                  "status_emoji": ":palm_tree:"}})
        assert set_resp.json()["ok"] is True
        get_after = client.get(f"/api/users.profile.get?user={user['id']}",
                               headers=WORKSPACE_HEADER).json()
        assert get_after["profile"]["status_text"] == "On vacation"
        assert get_after["profile"]["status_emoji"] == ":palm_tree:"


# ---------------------------------------------------------------------------
# Search
# ---------------------------------------------------------------------------

class TestSearch:
    def test_search_messages_rejects_bot_token(self, client):
        resp = client.get("/api/search.messages?query=anything",
                          headers=BOT_TOKEN_HEADER).json()
        assert resp["ok"] is False
        assert resp["error"] == "not_allowed_token_type"

    def test_search_messages(self, client):
        ch = _get_first_non_general_channel(client)
        _post_message(client, ch["id"], "Unique search term xyzzy123")

        resp = client.get("/api/search.messages?query=xyzzy123",
                          headers=USER_TOKEN_HEADER).json()
        assert resp["ok"] is True
        matches = resp["messages"]["matches"]
        assert any("xyzzy123" in m["text"] for m in matches)

    def test_search_empty_results(self, client):
        resp = client.get("/api/search.messages?query=zzznomatch999xyzabc",
                          headers=USER_TOKEN_HEADER).json()
        assert resp["ok"] is True
        assert resp["messages"]["total"] == 0
        assert resp["messages"]["matches"] == []


# ---------------------------------------------------------------------------
# Pagination
# ---------------------------------------------------------------------------

class TestPagination:
    def test_conversations_list_pagination(self, client):
        # Get all channels in two pages
        page1 = client.get("/api/conversations.list?limit=2",
                           headers=WORKSPACE_HEADER).json()
        assert len(page1["channels"]) <= 2
        cursor = page1["response_metadata"]["next_cursor"]

        if cursor:
            page2 = client.get(f"/api/conversations.list?limit=2&cursor={cursor}",
                               headers=WORKSPACE_HEADER).json()
            page1_ids = {c["id"] for c in page1["channels"]}
            page2_ids = {c["id"] for c in page2["channels"]}
            assert page1_ids.isdisjoint(page2_ids), "Pages must not overlap"

    def test_conversations_history_pagination(self, client):
        ch = _get_first_non_general_channel(client)
        page1 = client.get(f"/api/conversations.history?channel={ch['id']}&limit=2",
                           headers=WORKSPACE_HEADER).json()
        assert page1["ok"] is True
        assert len(page1["messages"]) <= 2
        cursor = page1.get("response_metadata", {}).get("next_cursor")
        if cursor:
            page2 = client.get(
                f"/api/conversations.history?channel={ch['id']}&limit=2&cursor={cursor}",
                headers=WORKSPACE_HEADER,
            ).json()
            page1_ts = {m["ts"] for m in page1["messages"]}
            page2_ts = {m["ts"] for m in page2["messages"]}
            assert page1_ts.isdisjoint(page2_ts)

    def test_users_list_pagination(self, client):
        page1 = client.get("/api/users.list?limit=3",
                           headers=WORKSPACE_HEADER).json()
        assert page1["ok"] is True
        assert len(page1["members"]) <= 3
        cursor = page1["response_metadata"]["next_cursor"]
        if cursor:
            page2 = client.get(f"/api/users.list?limit=3&cursor={cursor}",
                               headers=WORKSPACE_HEADER).json()
            page1_ids = {u["id"] for u in page1["members"]}
            page2_ids = {u["id"] for u in page2["members"]}
            assert page1_ids.isdisjoint(page2_ids)


# ---------------------------------------------------------------------------
# Error cases
# ---------------------------------------------------------------------------

class TestErrors:
    def test_channel_not_found(self, client):
        resp = client.get("/api/conversations.info?channel=CNOTEXIST",
                          headers=WORKSPACE_HEADER)
        body = resp.json()
        assert body["ok"] is False
        assert body["error"] == "channel_not_found"

    def test_user_not_found(self, client):
        resp = client.get("/api/users.info?user=UNOTEXIST",
                          headers=WORKSPACE_HEADER)
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "user_not_found"

    def test_message_not_found(self, client):
        ch = _get_first_non_general_channel(client)
        resp = client.post("/api/chat.delete", headers=WORKSPACE_HEADER,
                           json={"channel": ch["id"], "ts": "0000000000.000000"})
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "message_not_found"

    def test_file_not_found(self, client):
        resp = client.get("/api/files.info?file=FNOTEXIST",
                          headers=WORKSPACE_HEADER)
        assert resp.json()["ok"] is False
        assert resp.json()["error"] == "file_not_found"

    def test_double_archive(self, client):
        resp = client.post("/api/conversations.create", headers=WORKSPACE_HEADER,
                           json={"name": "test-double-archive"})
        ch_id = resp.json()["channel"]["id"]
        client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                    json={"channel": ch_id})
        resp2 = client.post("/api/conversations.archive", headers=WORKSPACE_HEADER,
                            json={"channel": ch_id})
        assert resp2.json()["ok"] is False
        assert resp2.json()["error"] == "already_archived"
