"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Helix",
        "location": "Conference Room A",
        "days_from_now": 10,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Helix",
        "location": "Zoom",
        "days_from_now": 8,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Helix",
        "location": "Google Meet",
        "days_from_now": 4,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Helix",
        "location": "Google Meet",
        "days_from_now": 1,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Helix",
    "Roadmap Sync \u2014 Helix"
]

KEEP_SUMMARIES = [
    "All-Hands \u2014 Helix",
    "Security Review \u2014 Helix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
