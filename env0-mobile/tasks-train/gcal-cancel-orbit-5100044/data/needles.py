"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Design Review \u2014 Orbit",
        "location": "Conference Room B",
        "days_from_now": 9,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Orbit",
        "location": "Auditorium",
        "days_from_now": 13,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Orbit",
        "location": "Conference Room A",
        "days_from_now": 4,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Orbit",
        "location": "Google Meet",
        "days_from_now": 2,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Orbit",
        "location": "Conference Room A",
        "days_from_now": 1,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Design Review \u2014 Orbit",
    "Partner Call \u2014 Orbit",
    "Roadmap Sync \u2014 Orbit"
]

KEEP_SUMMARIES = [
    "All-Hands \u2014 Orbit",
    "Security Review \u2014 Orbit"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
