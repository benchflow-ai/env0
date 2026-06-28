"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Orbit",
        "location": "Phone",
        "days_from_now": 2,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 Orbit",
        "location": "Google Meet",
        "days_from_now": 10,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Sprint Retro \u2014 Orbit",
        "location": "Conference Room B",
        "days_from_now": 9,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Orbit",
        "location": "Conference Room A",
        "days_from_now": 5,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Orbit",
        "location": "Phone",
        "days_from_now": 1,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Orbit",
        "location": "Phone",
        "days_from_now": 4,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Orbit",
    "Analytics Review \u2014 Orbit",
    "Sprint Retro \u2014 Orbit"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Orbit",
    "Eng Office Hours \u2014 Orbit",
    "1:1 with Manager \u2014 Orbit"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
