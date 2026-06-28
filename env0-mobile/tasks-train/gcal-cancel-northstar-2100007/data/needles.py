"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Northstar",
        "location": "Phone",
        "days_from_now": 13,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Northstar",
        "location": "Conference Room A",
        "days_from_now": 11,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Northstar",
        "location": "Google Meet",
        "days_from_now": 4,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Northstar",
        "location": "Auditorium",
        "days_from_now": 8,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Northstar",
        "location": "Google Meet",
        "days_from_now": 1,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Northstar",
    "Partner Call \u2014 Northstar"
]

KEEP_SUMMARIES = [
    "Team Standup \u2014 Northstar",
    "Eng Office Hours \u2014 Northstar",
    "Product Demo \u2014 Northstar"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
