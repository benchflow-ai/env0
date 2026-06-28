"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Q3 Planning",
        "location": "Zoom",
        "days_from_now": 7,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Q3 Planning",
        "location": "Conference Room B",
        "days_from_now": 11,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Q3 Planning",
        "location": "Phone",
        "days_from_now": 4,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Q3 Planning",
        "location": "Conference Room C",
        "days_from_now": 2,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Q3 Planning",
        "location": "Auditorium",
        "days_from_now": 1,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Q3 Planning",
    "Design Review \u2014 Q3 Planning",
    "Roadmap Sync \u2014 Q3 Planning"
]

KEEP_SUMMARIES = [
    "Team Standup \u2014 Q3 Planning",
    "Lunch & Learn \u2014 Q3 Planning"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
