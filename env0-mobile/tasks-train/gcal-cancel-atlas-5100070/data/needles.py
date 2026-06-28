"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Atlas",
        "location": "Phone",
        "days_from_now": 4,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Atlas",
        "location": "Auditorium",
        "days_from_now": 1,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Atlas",
        "location": "Zoom",
        "days_from_now": 11,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Atlas",
        "location": "Zoom",
        "days_from_now": 5,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Atlas",
    "Partner Call \u2014 Atlas"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Atlas",
    "Eng Office Hours \u2014 Atlas"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
