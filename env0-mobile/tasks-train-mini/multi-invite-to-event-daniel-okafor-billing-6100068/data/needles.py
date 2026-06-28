"""Auto-generated env-0 tasks-lite needle data (multi invite->event).
Dependency-free. gmail reads NEEDLES/GMAIL_FILL_CONFIG; gcal reads
NEEDLE_EVENTS (empty: agent must create the event) / GCAL_FILL_CONFIG."""

SENDER_NAME = "Daniel Okafor"
SENDER_EMAIL = "daniel.okafor@fernandlee.com"
MEETING_SUMMARY = "Billing Cleanup Discussion"
SUMMARY_KEYWORDS = ["billing"]
START_WEEKDAY = 4  # 0=Mon
START_HOUR = 11
DECOY_SUMMARY = "Vendor Demo"
DECOY_KEYWORDS = ["vendor demo"]

NEEDLES = [
    {
        "sender_name": "Daniel Okafor",
        "sender_email": "daniel.okafor@fernandlee.com",
        "subject": "Can we meet about the billing cleanup discussion?",
        "body_plain": "Hi,\n\nCould we meet about the billing cleanup discussion? I'm proposing Friday at 11:00 AM. Let me know if that works and I'll see you then.\n\nThanks,\nDaniel Okafor\n",
        "labels": [
            "INBOX"
        ],
        "days_ago": 2,
        "role": "invite",
        "params": {}
    },
    {
        "sender_name": "Lena Volkov",
        "sender_email": "lena.volkov@fernandlee.com",
        "subject": "FYI on the vendor demo",
        "body_plain": "Hi,\n\nFollowing up on the vendor demo \u2014 I know you replied earlier that you can't make it and we're cancelling on your end, so no need to block time. Just keeping you in the loop.\n\nBest,\nLena Volkov\n",
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
