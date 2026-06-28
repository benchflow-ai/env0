"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Northstar",
        "location": "Conference Room C",
        "days_from_now": 3,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Northstar",
        "location": "Phone",
        "days_from_now": 6,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Northstar",
        "location": "Google Meet",
        "days_from_now": 13,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Northstar",
        "location": "Google Meet",
        "days_from_now": 9,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Northstar",
    "Design Review \u2014 Northstar"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Northstar",
    "Lunch & Learn \u2014 Northstar"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
