"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Vendor Check-in \u2014 EMEA",
        "location": "Conference Room B",
        "days_from_now": 8,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Budget Planning \u2014 EMEA",
        "location": "Conference Room C",
        "days_from_now": 2,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 EMEA",
        "location": "Auditorium",
        "days_from_now": 1,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 EMEA",
        "location": "Google Meet",
        "days_from_now": 6,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Vendor Check-in \u2014 EMEA",
    "Budget Planning \u2014 EMEA"
]

KEEP_SUMMARIES = [
    "Team Standup \u2014 EMEA",
    "Eng Office Hours \u2014 EMEA"
]

GCAL_FILL_CONFIG = {'target_count': 18, 'include_needles': True}
