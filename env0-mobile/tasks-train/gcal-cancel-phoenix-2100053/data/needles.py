"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Phoenix",
        "location": "Zoom",
        "days_from_now": 9,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 Phoenix",
        "location": "Google Meet",
        "days_from_now": 3,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Phoenix",
        "location": "Phone",
        "days_from_now": 4,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Phoenix",
        "location": "Conference Room A",
        "days_from_now": 2,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Phoenix",
    "Analytics Review \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "All-Hands \u2014 Phoenix",
    "Lunch & Learn \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 18, 'include_needles': True}
