"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Budget Planning \u2014 EMEA",
        "location": "Conference Room C",
        "days_from_now": 10,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 EMEA",
        "location": "Google Meet",
        "days_from_now": 8,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 EMEA",
        "location": "Conference Room C",
        "days_from_now": 11,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 EMEA",
        "location": "Zoom",
        "days_from_now": 4,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 EMEA",
        "location": "Zoom",
        "days_from_now": 12,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Budget Planning \u2014 EMEA",
    "Roadmap Sync \u2014 EMEA",
    "Design Review \u2014 EMEA"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 EMEA",
    "All-Hands \u2014 EMEA"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
