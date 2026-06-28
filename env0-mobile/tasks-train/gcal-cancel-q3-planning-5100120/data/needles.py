"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Q3 Planning",
        "location": "Conference Room B",
        "days_from_now": 13,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Q3 Planning",
        "location": "Conference Room B",
        "days_from_now": 1,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Q3 Planning",
        "location": "Google Meet",
        "days_from_now": 3,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Q3 Planning",
        "location": "Conference Room C",
        "days_from_now": 9,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Q3 Planning",
    "Partner Call \u2014 Q3 Planning"
]

KEEP_SUMMARIES = [
    "All-Hands \u2014 Q3 Planning",
    "Product Demo \u2014 Q3 Planning"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
