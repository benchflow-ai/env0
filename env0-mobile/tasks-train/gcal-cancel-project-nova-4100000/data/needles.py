"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Hiring Debrief \u2014 Project Nova",
        "location": "Auditorium",
        "days_from_now": 8,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Project Nova",
        "location": "Conference Room A",
        "days_from_now": 11,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Project Nova",
        "location": "Conference Room C",
        "days_from_now": 12,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Project Nova",
        "location": "Zoom",
        "days_from_now": 3,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Project Nova",
        "location": "Conference Room B",
        "days_from_now": 4,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Hiring Debrief \u2014 Project Nova",
    "Design Review \u2014 Project Nova"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Project Nova",
    "Security Review \u2014 Project Nova",
    "Team Standup \u2014 Project Nova"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
