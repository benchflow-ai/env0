"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Atlas",
        "location": "Zoom",
        "days_from_now": 9,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Budget Planning \u2014 Atlas",
        "location": "Conference Room A",
        "days_from_now": 4,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Atlas",
        "location": "Zoom",
        "days_from_now": 11,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Atlas",
        "location": "Google Meet",
        "days_from_now": 10,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Atlas",
    "Budget Planning \u2014 Atlas"
]

KEEP_SUMMARIES = [
    "Lunch & Learn \u2014 Atlas",
    "Security Review \u2014 Atlas"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
