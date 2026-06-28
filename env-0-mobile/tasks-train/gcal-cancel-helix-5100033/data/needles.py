"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Design Review \u2014 Helix",
        "location": "Conference Room B",
        "days_from_now": 13,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 Helix",
        "location": "Auditorium",
        "days_from_now": 5,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Helix",
        "location": "Conference Room B",
        "days_from_now": 3,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Helix",
        "location": "Google Meet",
        "days_from_now": 9,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Design Review \u2014 Helix",
    "Vendor Check-in \u2014 Helix"
]

KEEP_SUMMARIES = [
    "All-Hands \u2014 Helix",
    "Product Demo \u2014 Helix"
]

GCAL_FILL_CONFIG = {'target_count': 18, 'include_needles': True}
