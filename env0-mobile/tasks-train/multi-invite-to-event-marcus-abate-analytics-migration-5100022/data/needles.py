"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Marcus Abate"
SENDER_EMAIL = "marcus.abate@tinroofapp.com"
MEETING_SUMMARY = "Analytics Migration Kickoff"
SUMMARY_KEYWORDS = ["analytics", "migration"]
START_WEEKDAY = 1  # 0=Mon
START_HOUR = 9
DECOY_SUMMARY = "Offsite Planning Call"
DECOY_KEYWORDS = ["offsite"]

NEEDLES = [
    {
        "sender_name": "Marcus Abate",
        "sender_email": "marcus.abate@tinroofapp.com",
        "subject": "Can we meet about the analytics migration kickoff?",
        "body_plain": "Hi,\n\nCould we meet about the analytics migration kickoff? I'm proposing Tuesday at 9:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nMarcus Abate\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 1,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Priya Nair",
        "sender_email": "priya.nair@tinroofapp.com",
        "subject": "FYI on the offsite planning call",
        "body_plain": "Hi,\n\nFollowing up on the offsite planning call \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nPriya Nair\n",
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
