"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Project Nova",
        "location": "Conference Room B",
        "days_from_now": 9,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 Project Nova",
        "location": "Conference Room C",
        "days_from_now": 2,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Project Nova",
        "location": "Conference Room C",
        "days_from_now": 12,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Project Nova",
        "location": "Phone",
        "days_from_now": 13,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Project Nova",
        "location": "Phone",
        "days_from_now": 8,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Project Nova",
        "location": "Conference Room B",
        "days_from_now": 11,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Project Nova",
    "Vendor Check-in \u2014 Project Nova",
    "Roadmap Sync \u2014 Project Nova"
]

KEEP_SUMMARIES = [
    "Security Review \u2014 Project Nova",
    "Team Standup \u2014 Project Nova",
    "Product Demo \u2014 Project Nova"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
