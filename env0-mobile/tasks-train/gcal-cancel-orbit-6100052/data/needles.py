"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Orbit",
        "location": "Conference Room B",
        "days_from_now": 6,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Hiring Debrief \u2014 Orbit",
        "location": "Phone",
        "days_from_now": 7,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Orbit",
        "location": "Zoom",
        "days_from_now": 10,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Orbit",
        "location": "Auditorium",
        "days_from_now": 9,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Orbit",
        "location": "Conference Room C",
        "days_from_now": 13,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Orbit",
        "location": "Zoom",
        "days_from_now": 3,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Orbit",
    "Hiring Debrief \u2014 Orbit",
    "Design Review \u2014 Orbit"
]

KEEP_SUMMARIES = [
    "Security Review \u2014 Orbit",
    "Lunch & Learn \u2014 Orbit",
    "Eng Office Hours \u2014 Orbit"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
