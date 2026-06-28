"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Vendor Check-in \u2014 Helix",
        "location": "Conference Room B",
        "days_from_now": 9,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Helix",
        "location": "Auditorium",
        "days_from_now": 12,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Helix",
        "location": "Conference Room A",
        "days_from_now": 7,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Helix",
        "location": "Phone",
        "days_from_now": 13,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Helix",
        "location": "Conference Room C",
        "days_from_now": 11,
        "start_hour": 11,
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
    "Eng Office Hours \u2014 Helix",
    "Security Review \u2014 Helix",
    "Product Demo \u2014 Helix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
