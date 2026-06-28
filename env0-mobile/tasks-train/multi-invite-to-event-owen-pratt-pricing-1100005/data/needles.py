"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Owen Pratt"
SENDER_EMAIL = "owen.pratt@brightlane.io"
MEETING_SUMMARY = "Pricing Experiment Readout"
SUMMARY_KEYWORDS = ["pricing"]
START_WEEKDAY = 4  # 0=Mon
START_HOUR = 10
DECOY_SUMMARY = "Offsite Planning Call"
DECOY_KEYWORDS = ["offsite"]

NEEDLES = [
    {
        "sender_name": "Owen Pratt",
        "sender_email": "owen.pratt@brightlane.io",
        "subject": "Can we meet about our pricing experiment readout?",
        "body_plain": "Hi,\n\nCould we meet about our pricing experiment readout? I'm proposing Friday at 10:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nOwen Pratt\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 1,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Tomas Reyes",
        "sender_email": "tomas.reyes@brightlane.io",
        "subject": "FYI on the offsite planning call",
        "body_plain": "Hi,\n\nFollowing up on the offsite planning call \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nTomas Reyes\n",
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
