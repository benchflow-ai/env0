"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Tomas Reyes"
SENDER_EMAIL = "tomas.reyes@brightlane.io"
MEETING_SUMMARY = "Design System Review"
SUMMARY_KEYWORDS = ["design system"]
START_WEEKDAY = 3  # 0=Mon
START_HOUR = 15
DECOY_SUMMARY = "Offsite Planning Call"
DECOY_KEYWORDS = ["offsite"]

NEEDLES = [
    {
        "sender_name": "Tomas Reyes",
        "sender_email": "tomas.reyes@brightlane.io",
        "subject": "Can we meet about the design system review?",
        "body_plain": "Hi,\n\nCould we meet about the design system review? I'm proposing Thursday at 3:00 PM. Let me know if that works and I'll see you then.\n\nThanks,\nTomas Reyes\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 1,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Priya Nair",
        "sender_email": "priya.nair@brightlane.io",
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
