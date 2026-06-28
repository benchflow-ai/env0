"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Phoenix",
        "location": "Phone",
        "days_from_now": 10,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Phoenix",
        "location": "Conference Room B",
        "days_from_now": 2,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 4,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Phoenix",
        "location": "Conference Room A",
        "days_from_now": 11,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Phoenix",
    "Partner Call \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "Security Review \u2014 Phoenix",
    "1:1 with Manager \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
