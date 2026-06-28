"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Orbit",
        "location": "Auditorium",
        "days_from_now": 10,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Orbit",
        "location": "Google Meet",
        "days_from_now": 6,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 Orbit",
        "location": "Phone",
        "days_from_now": 1,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Orbit",
        "location": "Conference Room B",
        "days_from_now": 3,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Orbit",
        "location": "Phone",
        "days_from_now": 4,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Orbit",
        "location": "Zoom",
        "days_from_now": 5,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Orbit",
    "Design Review \u2014 Orbit",
    "Vendor Check-in \u2014 Orbit"
]

KEEP_SUMMARIES = [
    "Security Review \u2014 Orbit",
    "Product Demo \u2014 Orbit",
    "1:1 with Manager \u2014 Orbit"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
