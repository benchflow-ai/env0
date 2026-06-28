"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Lena Volkov"
SENDER_EMAIL = "lena.volkov@fernandlee.com"
MEETING_SUMMARY = "Support Handoff Planning"
SUMMARY_KEYWORDS = ["handoff"]
START_WEEKDAY = 4  # 0=Mon
START_HOUR = 16
DECOY_SUMMARY = "Vendor Demo"
DECOY_KEYWORDS = ["vendor demo"]

NEEDLES = [
    {
        "sender_name": "Lena Volkov",
        "sender_email": "lena.volkov@fernandlee.com",
        "subject": "Can we meet about the support handoff planning?",
        "body_plain": "Hi,\n\nCould we meet about the support handoff planning? I'm proposing Friday at 4:00 PM. Let me know if that works and I'll see you then.\n\nThanks,\nLena Volkov\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 2,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Hannah Berg",
        "sender_email": "hannah.berg@fernandlee.com",
        "subject": "FYI on the vendor demo",
        "body_plain": "Hi,\n\nFollowing up on the vendor demo \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nHannah Berg\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 4,
        "role": "decoy_declined",
        "params": {}
    }
]

# Calendar starts empty for this task; the agent creates the event.
NEEDLE_EVENTS = []

GMAIL_FILL_CONFIG = {"target_count": 40}
GCAL_FILL_CONFIG = {"target_count": "fixed_only", "include_needles": True}
