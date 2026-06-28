"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Owen Pratt"
SENDER_EMAIL = "owen.pratt@fernandlee.com"
MEETING_SUMMARY = "Partner Integration Walkthrough"
SUMMARY_KEYWORDS = ["integration"]
START_WEEKDAY = 0  # 0=Mon
START_HOUR = 9
DECOY_SUMMARY = "Vendor Demo"
DECOY_KEYWORDS = ["vendor demo"]

NEEDLES = [
    {
        "sender_name": "Owen Pratt",
        "sender_email": "owen.pratt@fernandlee.com",
        "subject": "Can we meet about the partner integration walkthrough?",
        "body_plain": "Hi,\n\nCould we meet about the partner integration walkthrough? I'm proposing Monday at 9:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nOwen Pratt\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 3,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Lena Volkov",
        "sender_email": "lena.volkov@fernandlee.com",
        "subject": "FYI on the vendor demo",
        "body_plain": "Hi,\n\nFollowing up on the vendor demo \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nLena Volkov\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 5,
        "role": "decoy_declined",
        "params": {}
    }
]

# Calendar starts empty for this task; the agent creates the event.
NEEDLE_EVENTS = []

GMAIL_FILL_CONFIG = {"target_count": 40}
GCAL_FILL_CONFIG = {"target_count": "fixed_only", "include_needles": True}
