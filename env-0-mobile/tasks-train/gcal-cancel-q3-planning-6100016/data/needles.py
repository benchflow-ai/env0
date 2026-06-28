"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Q3 Planning",
        "location": "Zoom",
        "days_from_now": 2,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Q3 Planning",
        "location": "Zoom",
        "days_from_now": 9,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Q3 Planning",
        "location": "Auditorium",
        "days_from_now": 7,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Q3 Planning",
        "location": "Google Meet",
        "days_from_now": 10,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Q3 Planning",
    "Roadmap Sync \u2014 Q3 Planning"
]

KEEP_SUMMARIES = [
    "Lunch & Learn \u2014 Q3 Planning",
    "Eng Office Hours \u2014 Q3 Planning"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
