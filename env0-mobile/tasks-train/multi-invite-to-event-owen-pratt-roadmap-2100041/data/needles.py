"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Owen Pratt"
SENDER_EMAIL = "owen.pratt@fernandlee.com"
MEETING_SUMMARY = "Q3 Roadmap Review"
SUMMARY_KEYWORDS = ["roadmap"]
START_WEEKDAY = 3  # 0=Mon
START_HOUR = 10
DECOY_SUMMARY = "All-Hands Rehearsal"
DECOY_KEYWORDS = ["all-hands", "rehearsal"]

NEEDLES = [
    {
        "sender_name": "Owen Pratt",
        "sender_email": "owen.pratt@fernandlee.com",
        "subject": "Can we meet about Q3 roadmap review?",
        "body_plain": "Hi,\n\nCould we meet about Q3 roadmap review? I'm proposing Thursday at 10:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nOwen Pratt\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 2,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Daniel Okafor",
        "sender_email": "daniel.okafor@fernandlee.com",
        "subject": "FYI on the all-hands rehearsal",
        "body_plain": "Hi,\n\nFollowing up on the all-hands rehearsal \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nDaniel Okafor\n",
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
