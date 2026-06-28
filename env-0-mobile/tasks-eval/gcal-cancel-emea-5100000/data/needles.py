"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Design Review \u2014 EMEA",
        "location": "Phone",
        "days_from_now": 10,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Sprint Retro \u2014 EMEA",
        "location": "Conference Room C",
        "days_from_now": 13,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 EMEA",
        "location": "Zoom",
        "days_from_now": 4,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 EMEA",
        "location": "Phone",
        "days_from_now": 3,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 EMEA",
        "location": "Google Meet",
        "days_from_now": 2,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Design Review \u2014 EMEA",
    "Sprint Retro \u2014 EMEA"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 EMEA",
    "Lunch & Learn \u2014 EMEA",
    "1:1 with Manager \u2014 EMEA"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
