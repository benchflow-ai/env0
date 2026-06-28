"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Hiring Debrief \u2014 Phoenix",
        "location": "Conference Room B",
        "days_from_now": 4,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 Phoenix",
        "location": "Conference Room B",
        "days_from_now": 5,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 Phoenix",
        "location": "Zoom",
        "days_from_now": 2,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Phoenix",
        "location": "Zoom",
        "days_from_now": 12,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 7,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Hiring Debrief \u2014 Phoenix",
    "Analytics Review \u2014 Phoenix",
    "Vendor Check-in \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "All-Hands \u2014 Phoenix",
    "Product Demo \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
