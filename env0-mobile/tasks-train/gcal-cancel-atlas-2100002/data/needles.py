"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Atlas",
        "location": "Conference Room A",
        "days_from_now": 12,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Sprint Retro \u2014 Atlas",
        "location": "Google Meet",
        "days_from_now": 1,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Atlas",
        "location": "Auditorium",
        "days_from_now": 4,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Atlas",
        "location": "Conference Room C",
        "days_from_now": 10,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Atlas",
    "Sprint Retro \u2014 Atlas"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Atlas",
    "Team Standup \u2014 Atlas"
]

GCAL_FILL_CONFIG = {'target_count': 18, 'include_needles': True}
