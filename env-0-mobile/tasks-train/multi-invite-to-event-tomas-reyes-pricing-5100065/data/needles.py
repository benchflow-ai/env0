"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Tomas Reyes"
SENDER_EMAIL = "tomas.reyes@harborstack.co"
MEETING_SUMMARY = "Pricing Experiment Readout"
SUMMARY_KEYWORDS = ["pricing"]
START_WEEKDAY = 1  # 0=Mon
START_HOUR = 15
DECOY_SUMMARY = "Offsite Planning Call"
DECOY_KEYWORDS = ["offsite"]

NEEDLES = [
    {
        "sender_name": "Tomas Reyes",
        "sender_email": "tomas.reyes@harborstack.co",
        "subject": "Can we meet about our pricing experiment readout?",
        "body_plain": "Hi,\n\nCould we meet about our pricing experiment readout? I'm proposing Tuesday at 3:00 PM. Let me know if that works and I'll see you then.\n\nThanks,\nTomas Reyes\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 2,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Hannah Berg",
        "sender_email": "hannah.berg@harborstack.co",
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
