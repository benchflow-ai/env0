"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 6,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Phoenix",
        "location": "Google Meet",
        "days_from_now": 5,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 Phoenix",
        "location": "Zoom",
        "days_from_now": 9,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Phoenix",
        "location": "Phone",
        "days_from_now": 2,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Phoenix",
        "location": "Auditorium",
        "days_from_now": 8,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 11,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Phoenix",
    "Design Review \u2014 Phoenix",
    "Analytics Review \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Phoenix",
    "Team Standup \u2014 Phoenix",
    "Customer Onboarding \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
