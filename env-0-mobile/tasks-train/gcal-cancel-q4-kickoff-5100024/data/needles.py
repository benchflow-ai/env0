"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Q4 Kickoff",
        "location": "Zoom",
        "days_from_now": 1,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Budget Planning \u2014 Q4 Kickoff",
        "location": "Phone",
        "days_from_now": 13,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Q4 Kickoff",
        "location": "Auditorium",
        "days_from_now": 10,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Q4 Kickoff",
        "location": "Conference Room C",
        "days_from_now": 6,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Q4 Kickoff",
    "Budget Planning \u2014 Q4 Kickoff"
]

KEEP_SUMMARIES = [
    "1:1 with Manager \u2014 Q4 Kickoff",
    "Product Demo \u2014 Q4 Kickoff"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
