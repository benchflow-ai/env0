"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Hiring Debrief \u2014 Q4 Kickoff",
        "location": "Auditorium",
        "days_from_now": 6,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 Q4 Kickoff",
        "location": "Auditorium",
        "days_from_now": 9,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Q4 Kickoff",
        "location": "Conference Room C",
        "days_from_now": 5,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Q4 Kickoff",
        "location": "Auditorium",
        "days_from_now": 12,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Q4 Kickoff",
        "location": "Google Meet",
        "days_from_now": 10,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Hiring Debrief \u2014 Q4 Kickoff",
    "Vendor Check-in \u2014 Q4 Kickoff"
]

KEEP_SUMMARIES = [
    "Team Standup \u2014 Q4 Kickoff",
    "1:1 with Manager \u2014 Q4 Kickoff",
    "Eng Office Hours \u2014 Q4 Kickoff"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
