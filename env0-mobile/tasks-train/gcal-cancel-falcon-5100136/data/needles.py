"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Vendor Check-in \u2014 Falcon",
        "location": "Conference Room B",
        "days_from_now": 4,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Sprint Retro \u2014 Falcon",
        "location": "Google Meet",
        "days_from_now": 12,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Falcon",
        "location": "Google Meet",
        "days_from_now": 1,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Falcon",
        "location": "Zoom",
        "days_from_now": 11,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Falcon",
        "location": "Conference Room B",
        "days_from_now": 8,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Vendor Check-in \u2014 Falcon",
    "Sprint Retro \u2014 Falcon",
    "Partner Call \u2014 Falcon"
]

KEEP_SUMMARIES = [
    "Security Review \u2014 Falcon",
    "1:1 with Manager \u2014 Falcon"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
