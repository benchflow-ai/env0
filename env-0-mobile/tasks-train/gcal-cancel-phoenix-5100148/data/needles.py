"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 5,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 Phoenix",
        "location": "Conference Room A",
        "days_from_now": 3,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Phoenix",
        "location": "Conference Room B",
        "days_from_now": 7,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Phoenix",
        "location": "Zoom",
        "days_from_now": 2,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Phoenix",
        "location": "Zoom",
        "days_from_now": 9,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Phoenix",
    "Analytics Review \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "Lunch & Learn \u2014 Phoenix",
    "Security Review \u2014 Phoenix",
    "Team Standup \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 18, 'include_needles': True}
