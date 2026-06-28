"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Hannah Berg"
SENDER_EMAIL = "hannah.berg@harborstack.co"
MEETING_SUMMARY = "Pricing Experiment Readout"
SUMMARY_KEYWORDS = ["pricing"]
START_WEEKDAY = 2  # 0=Mon
START_HOUR = 10
DECOY_SUMMARY = "All-Hands Rehearsal"
DECOY_KEYWORDS = ["all-hands", "rehearsal"]

NEEDLES = [
    {
        "sender_name": "Hannah Berg",
        "sender_email": "hannah.berg@harborstack.co",
        "subject": "Can we meet about our pricing experiment readout?",
        "body_plain": "Hi,\n\nCould we meet about our pricing experiment readout? I'm proposing Wednesday at 10:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nHannah Berg\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 3,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Priya Nair",
        "sender_email": "priya.nair@harborstack.co",
        "subject": "FYI on the all-hands rehearsal",
        "body_plain": "Hi,\n\nFollowing up on the all-hands rehearsal \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nPriya Nair\n",
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
