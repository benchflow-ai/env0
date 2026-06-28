"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Budget Planning \u2014 EMEA",
        "location": "Zoom",
        "days_from_now": 8,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 EMEA",
        "location": "Conference Room C",
        "days_from_now": 1,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 EMEA",
        "location": "Conference Room B",
        "days_from_now": 11,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 EMEA",
        "location": "Zoom",
        "days_from_now": 7,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Budget Planning \u2014 EMEA",
    "Analytics Review \u2014 EMEA"
]

KEEP_SUMMARIES = [
    "Eng Office Hours \u2014 EMEA",
    "Lunch & Learn \u2014 EMEA"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
