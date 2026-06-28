"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Roadmap Sync \u2014 Falcon",
        "location": "Conference Room A",
        "days_from_now": 2,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Budget Planning \u2014 Falcon",
        "location": "Google Meet",
        "days_from_now": 11,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Falcon",
        "location": "Phone",
        "days_from_now": 9,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Falcon",
        "location": "Conference Room A",
        "days_from_now": 7,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Roadmap Sync \u2014 Falcon",
    "Budget Planning \u2014 Falcon"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Falcon",
    "All-Hands \u2014 Falcon"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
