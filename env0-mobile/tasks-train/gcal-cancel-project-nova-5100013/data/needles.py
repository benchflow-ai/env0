"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Project Nova",
        "location": "Phone",
        "days_from_now": 9,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Hiring Debrief \u2014 Project Nova",
        "location": "Conference Room C",
        "days_from_now": 2,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Project Nova",
        "location": "Phone",
        "days_from_now": 13,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Project Nova",
        "location": "Zoom",
        "days_from_now": 5,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Project Nova",
        "location": "Conference Room A",
        "days_from_now": 12,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Project Nova",
    "Hiring Debrief \u2014 Project Nova"
]

KEEP_SUMMARIES = [
    "Eng Office Hours \u2014 Project Nova",
    "Security Review \u2014 Project Nova",
    "Team Standup \u2014 Project Nova"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
