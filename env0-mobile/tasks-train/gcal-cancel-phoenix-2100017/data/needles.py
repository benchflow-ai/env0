"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Roadmap Sync \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 8,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Phoenix",
        "location": "Conference Room A",
        "days_from_now": 5,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Phoenix",
        "location": "Conference Room A",
        "days_from_now": 3,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 11,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Phoenix",
        "location": "Zoom",
        "days_from_now": 7,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Roadmap Sync \u2014 Phoenix",
    "Partner Call \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "1:1 with Manager \u2014 Phoenix",
    "Product Demo \u2014 Phoenix",
    "Team Standup \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
