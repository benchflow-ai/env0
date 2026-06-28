"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Marcus Abate"
SENDER_EMAIL = "marcus.abate@brightlane.io"
MEETING_SUMMARY = "Q3 Roadmap Review"
SUMMARY_KEYWORDS = ["roadmap"]
START_WEEKDAY = 1  # 0=Mon
START_HOUR = 11
DECOY_SUMMARY = "All-Hands Rehearsal"
DECOY_KEYWORDS = ["all-hands", "rehearsal"]

NEEDLES = [
    {
        "sender_name": "Marcus Abate",
        "sender_email": "marcus.abate@brightlane.io",
        "subject": "Can we meet about Q3 roadmap review?",
        "body_plain": "Hi,\n\nCould we meet about Q3 roadmap review? I'm proposing Tuesday at 11:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nMarcus Abate\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 3,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Lena Volkov",
        "sender_email": "lena.volkov@brightlane.io",
        "subject": "FYI on the all-hands rehearsal",
        "body_plain": "Hi,\n\nFollowing up on the all-hands rehearsal \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nLena Volkov\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 2,
        "role": "decoy_declined",
        "params": {}
    }
]

# Calendar starts empty for this task; the agent creates the event.
NEEDLE_EVENTS = []

GMAIL_FILL_CONFIG = {"target_count": 40}
GCAL_FILL_CONFIG = {"target_count": "fixed_only", "include_needles": True}
