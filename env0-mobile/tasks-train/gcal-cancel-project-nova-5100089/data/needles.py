"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Project Nova",
        "location": "Google Meet",
        "days_from_now": 7,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Project Nova",
        "location": "Google Meet",
        "days_from_now": 1,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Project Nova",
        "location": "Phone",
        "days_from_now": 4,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Project Nova",
        "location": "Conference Room B",
        "days_from_now": 5,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Project Nova",
    "Partner Call \u2014 Project Nova"
]

KEEP_SUMMARIES = [
    "1:1 with Manager \u2014 Project Nova",
    "Lunch & Learn \u2014 Project Nova"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
