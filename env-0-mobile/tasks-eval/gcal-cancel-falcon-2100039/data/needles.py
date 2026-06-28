"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Roadmap Sync \u2014 Falcon",
        "location": "Conference Room B",
        "days_from_now": 4,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Hiring Debrief \u2014 Falcon",
        "location": "Phone",
        "days_from_now": 13,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Falcon",
        "location": "Phone",
        "days_from_now": 7,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Falcon",
        "location": "Auditorium",
        "days_from_now": 9,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Roadmap Sync \u2014 Falcon",
    "Hiring Debrief \u2014 Falcon"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Falcon",
    "Eng Office Hours \u2014 Falcon"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
