"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Yuki Tanaka"
SENDER_EMAIL = "yuki.tanaka@meadowcph.com"
MEETING_SUMMARY = "Q3 Roadmap Review"
SUMMARY_KEYWORDS = ["roadmap"]
START_WEEKDAY = 1  # 0=Mon
START_HOUR = 10
DECOY_SUMMARY = "Offsite Planning Call"
DECOY_KEYWORDS = ["offsite"]

NEEDLES = [
    {
        "sender_name": "Yuki Tanaka",
        "sender_email": "yuki.tanaka@meadowcph.com",
        "subject": "Can we meet about Q3 roadmap review?",
        "body_plain": "Hi,\n\nCould we meet about Q3 roadmap review? I'm proposing Tuesday at 10:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nYuki Tanaka\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 2,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Hannah Berg",
        "sender_email": "hannah.berg@meadowcph.com",
        "subject": "FYI on the offsite planning call",
        "body_plain": "Hi,\n\nFollowing up on the offsite planning call \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nHannah Berg\n",
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
