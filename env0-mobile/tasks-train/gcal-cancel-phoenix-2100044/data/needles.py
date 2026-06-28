"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Roadmap Sync \u2014 Phoenix",
        "location": "Auditorium",
        "days_from_now": 8,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 3,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 Phoenix",
        "location": "Phone",
        "days_from_now": 6,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 11,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Phoenix",
        "location": "Conference Room A",
        "days_from_now": 2,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Roadmap Sync \u2014 Phoenix",
    "Partner Call \u2014 Phoenix",
    "Analytics Review \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "Customer Onboarding \u2014 Phoenix",
    "Eng Office Hours \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
