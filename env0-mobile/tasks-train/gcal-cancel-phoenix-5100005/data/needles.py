"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Design Review \u2014 Phoenix",
        "location": "Auditorium",
        "days_from_now": 13,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Hiring Debrief \u2014 Phoenix",
        "location": "Auditorium",
        "days_from_now": 1,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Phoenix",
        "location": "Google Meet",
        "days_from_now": 9,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Phoenix",
        "location": "Conference Room B",
        "days_from_now": 10,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Phoenix",
        "location": "Phone",
        "days_from_now": 5,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Design Review \u2014 Phoenix",
    "Hiring Debrief \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "Team Standup \u2014 Phoenix",
    "All-Hands \u2014 Phoenix",
    "Lunch & Learn \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
