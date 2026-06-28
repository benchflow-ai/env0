"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 EMEA",
        "location": "Auditorium",
        "days_from_now": 9,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 EMEA",
        "location": "Auditorium",
        "days_from_now": 3,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 EMEA",
        "location": "Google Meet",
        "days_from_now": 10,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 EMEA",
        "location": "Zoom",
        "days_from_now": 4,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 EMEA",
        "location": "Conference Room C",
        "days_from_now": 5,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 EMEA",
    "Roadmap Sync \u2014 EMEA",
    "Vendor Check-in \u2014 EMEA"
]

KEEP_SUMMARIES = [
    "Eng Office Hours \u2014 EMEA",
    "Product Demo \u2014 EMEA"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
