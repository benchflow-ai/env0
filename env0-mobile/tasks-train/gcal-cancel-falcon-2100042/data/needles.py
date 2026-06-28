"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Budget Planning \u2014 Falcon",
        "location": "Google Meet",
        "days_from_now": 11,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 Falcon",
        "location": "Auditorium",
        "days_from_now": 3,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Sprint Retro \u2014 Falcon",
        "location": "Auditorium",
        "days_from_now": 5,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Falcon",
        "location": "Google Meet",
        "days_from_now": 6,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Falcon",
        "location": "Auditorium",
        "days_from_now": 2,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Budget Planning \u2014 Falcon",
    "Analytics Review \u2014 Falcon",
    "Sprint Retro \u2014 Falcon"
]

KEEP_SUMMARIES = [
    "Eng Office Hours \u2014 Falcon",
    "Team Standup \u2014 Falcon"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
