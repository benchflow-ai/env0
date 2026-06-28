"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Tomas Reyes"
SENDER_EMAIL = "tomas.reyes@tinroofapp.com"
MEETING_SUMMARY = "Design System Review"
SUMMARY_KEYWORDS = ["design system"]
START_WEEKDAY = 1  # 0=Mon
START_HOUR = 9
DECOY_SUMMARY = "All-Hands Rehearsal"
DECOY_KEYWORDS = ["all-hands", "rehearsal"]

NEEDLES = [
    {
        "sender_name": "Tomas Reyes",
        "sender_email": "tomas.reyes@tinroofapp.com",
        "subject": "Can we meet about the design system review?",
        "body_plain": "Hi,\n\nCould we meet about the design system review? I'm proposing Tuesday at 9:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nTomas Reyes\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 3,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Hannah Berg",
        "sender_email": "hannah.berg@tinroofapp.com",
        "subject": "FYI on the all-hands rehearsal",
        "body_plain": "Hi,\n\nFollowing up on the all-hands rehearsal \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nHannah Berg\n",
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
