"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Hiring Debrief \u2014 Phoenix",
        "location": "Conference Room A",
        "days_from_now": 3,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Phoenix",
        "location": "Zoom",
        "days_from_now": 11,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Phoenix",
        "location": "Google Meet",
        "days_from_now": 6,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Phoenix",
        "location": "Auditorium",
        "days_from_now": 9,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Hiring Debrief \u2014 Phoenix",
    "Partner Call \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "Eng Office Hours \u2014 Phoenix",
    "1:1 with Manager \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 18, 'include_needles': True}
