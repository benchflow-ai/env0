"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Atlas",
        "location": "Conference Room A",
        "days_from_now": 11,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Atlas",
        "location": "Conference Room A",
        "days_from_now": 8,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Atlas",
        "location": "Conference Room B",
        "days_from_now": 3,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Atlas",
        "location": "Conference Room A",
        "days_from_now": 6,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Atlas",
    "Partner Call \u2014 Atlas"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Atlas",
    "Lunch & Learn \u2014 Atlas"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
