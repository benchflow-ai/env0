"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Q3 Planning",
        "location": "Conference Room B",
        "days_from_now": 7,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Q3 Planning",
        "location": "Auditorium",
        "days_from_now": 6,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Hiring Debrief \u2014 Q3 Planning",
        "location": "Zoom",
        "days_from_now": 5,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Q3 Planning",
        "location": "Conference Room B",
        "days_from_now": 13,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Q3 Planning",
        "location": "Conference Room A",
        "days_from_now": 2,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Q3 Planning",
    "Design Review \u2014 Q3 Planning",
    "Hiring Debrief \u2014 Q3 Planning"
]

KEEP_SUMMARIES = [
    "Team Standup \u2014 Q3 Planning",
    "Lunch & Learn \u2014 Q3 Planning"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
