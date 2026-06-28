"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Budget Planning \u2014 Q4 Kickoff",
        "location": "Conference Room C",
        "days_from_now": 10,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Q4 Kickoff",
        "location": "Auditorium",
        "days_from_now": 7,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Q4 Kickoff",
        "location": "Conference Room A",
        "days_from_now": 3,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Q4 Kickoff",
        "location": "Auditorium",
        "days_from_now": 2,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Budget Planning \u2014 Q4 Kickoff",
    "Roadmap Sync \u2014 Q4 Kickoff"
]

KEEP_SUMMARIES = [
    "1:1 with Manager \u2014 Q4 Kickoff",
    "Product Demo \u2014 Q4 Kickoff"
]

GCAL_FILL_CONFIG = {'target_count': 18, 'include_needles': True}
