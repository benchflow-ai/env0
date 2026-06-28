"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Northstar",
        "location": "Conference Room C",
        "days_from_now": 13,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 Northstar",
        "location": "Conference Room C",
        "days_from_now": 11,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Northstar",
        "location": "Phone",
        "days_from_now": 1,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Northstar",
        "location": "Conference Room B",
        "days_from_now": 3,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Northstar",
    "Analytics Review \u2014 Northstar"
]

KEEP_SUMMARIES = [
    "1:1 with Manager \u2014 Northstar",
    "Eng Office Hours \u2014 Northstar"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
