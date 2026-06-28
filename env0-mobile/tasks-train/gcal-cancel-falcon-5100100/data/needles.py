"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Falcon",
        "location": "Conference Room C",
        "days_from_now": 9,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 Falcon",
        "location": "Conference Room B",
        "days_from_now": 1,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Falcon",
        "location": "Phone",
        "days_from_now": 3,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Falcon",
        "location": "Zoom",
        "days_from_now": 11,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Falcon",
    "Vendor Check-in \u2014 Falcon"
]

KEEP_SUMMARIES = [
    "Security Review \u2014 Falcon",
    "Team Standup \u2014 Falcon"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
