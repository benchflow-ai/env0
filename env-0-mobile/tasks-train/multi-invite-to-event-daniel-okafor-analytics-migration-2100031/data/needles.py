"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Daniel Okafor"
SENDER_EMAIL = "daniel.okafor@harborstack.co"
MEETING_SUMMARY = "Analytics Migration Kickoff"
SUMMARY_KEYWORDS = ["analytics", "migration"]
START_WEEKDAY = 2  # 0=Mon
START_HOUR = 14
DECOY_SUMMARY = "Offsite Planning Call"
DECOY_KEYWORDS = ["offsite"]

NEEDLES = [
    {
        "sender_name": "Daniel Okafor",
        "sender_email": "daniel.okafor@harborstack.co",
        "subject": "Can we meet about the analytics migration kickoff?",
        "body_plain": "Hi,\n\nCould we meet about the analytics migration kickoff? I'm proposing Wednesday at 2:00 PM. Let me know if that works and I'll see you then.\n\nThanks,\nDaniel Okafor\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 3,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Marcus Abate",
        "sender_email": "marcus.abate@harborstack.co",
        "subject": "FYI on the offsite planning call",
        "body_plain": "Hi,\n\nFollowing up on the offsite planning call \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nMarcus Abate\n",
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
