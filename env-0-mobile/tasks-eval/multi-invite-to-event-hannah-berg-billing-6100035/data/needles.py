"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Hannah Berg"
SENDER_EMAIL = "hannah.berg@brightlane.io"
MEETING_SUMMARY = "Billing Cleanup Discussion"
SUMMARY_KEYWORDS = ["billing"]
START_WEEKDAY = 3  # 0=Mon
START_HOUR = 9
DECOY_SUMMARY = "Offsite Planning Call"
DECOY_KEYWORDS = ["offsite"]

NEEDLES = [
    {
        "sender_name": "Hannah Berg",
        "sender_email": "hannah.berg@brightlane.io",
        "subject": "Can we meet about the billing cleanup discussion?",
        "body_plain": "Hi,\n\nCould we meet about the billing cleanup discussion? I'm proposing Thursday at 9:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nHannah Berg\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 1,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Owen Pratt",
        "sender_email": "owen.pratt@brightlane.io",
        "subject": "FYI on the offsite planning call",
        "body_plain": "Hi,\n\nFollowing up on the offsite planning call \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nOwen Pratt\n",
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
