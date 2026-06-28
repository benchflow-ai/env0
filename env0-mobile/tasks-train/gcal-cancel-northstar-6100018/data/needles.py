"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Northstar",
        "location": "Conference Room B",
        "days_from_now": 3,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Northstar",
        "location": "Conference Room A",
        "days_from_now": 12,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Northstar",
        "location": "Google Meet",
        "days_from_now": 8,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Northstar",
        "location": "Phone",
        "days_from_now": 11,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Northstar",
        "location": "Phone",
        "days_from_now": 5,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Northstar",
        "location": "Google Meet",
        "days_from_now": 1,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Northstar",
    "Design Review \u2014 Northstar",
    "Roadmap Sync \u2014 Northstar"
]

KEEP_SUMMARIES = [
    "Eng Office Hours \u2014 Northstar",
    "1:1 with Manager \u2014 Northstar",
    "Lunch & Learn \u2014 Northstar"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
