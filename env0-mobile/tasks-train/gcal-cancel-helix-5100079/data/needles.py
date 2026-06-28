"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Roadmap Sync \u2014 Helix",
        "location": "Conference Room C",
        "days_from_now": 11,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 Helix",
        "location": "Conference Room A",
        "days_from_now": 5,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Helix",
        "location": "Auditorium",
        "days_from_now": 10,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Helix",
        "location": "Phone",
        "days_from_now": 12,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Helix",
        "location": "Zoom",
        "days_from_now": 4,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Roadmap Sync \u2014 Helix",
    "Vendor Check-in \u2014 Helix",
    "Design Review \u2014 Helix"
]

KEEP_SUMMARIES = [
    "Security Review \u2014 Helix",
    "Product Demo \u2014 Helix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
