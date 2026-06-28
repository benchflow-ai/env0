"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Vendor Check-in \u2014 Helix",
        "location": "Auditorium",
        "days_from_now": 3,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Helix",
        "location": "Zoom",
        "days_from_now": 12,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Helix",
        "location": "Zoom",
        "days_from_now": 4,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Helix",
        "location": "Conference Room B",
        "days_from_now": 11,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Vendor Check-in \u2014 Helix",
    "Partner Call \u2014 Helix"
]

KEEP_SUMMARIES = [
    "All-Hands \u2014 Helix",
    "Product Demo \u2014 Helix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
