"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Vendor Check-in \u2014 EMEA",
        "location": "Phone",
        "days_from_now": 3,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Sprint Retro \u2014 EMEA",
        "location": "Phone",
        "days_from_now": 1,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 EMEA",
        "location": "Auditorium",
        "days_from_now": 12,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 EMEA",
        "location": "Zoom",
        "days_from_now": 4,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Vendor Check-in \u2014 EMEA",
    "Sprint Retro \u2014 EMEA"
]

KEEP_SUMMARIES = [
    "Security Review \u2014 EMEA",
    "All-Hands \u2014 EMEA"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
