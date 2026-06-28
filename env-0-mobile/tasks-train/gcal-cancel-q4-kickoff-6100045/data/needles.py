"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Budget Planning \u2014 Q4 Kickoff",
        "location": "Google Meet",
        "days_from_now": 5,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Q4 Kickoff",
        "location": "Conference Room A",
        "days_from_now": 8,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Q4 Kickoff",
        "location": "Auditorium",
        "days_from_now": 9,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Q4 Kickoff",
        "location": "Phone",
        "days_from_now": 3,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Q4 Kickoff",
        "location": "Phone",
        "days_from_now": 1,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Budget Planning \u2014 Q4 Kickoff",
    "Design Review \u2014 Q4 Kickoff",
    "Partner Call \u2014 Q4 Kickoff"
]

KEEP_SUMMARIES = [
    "Customer Onboarding \u2014 Q4 Kickoff",
    "Lunch & Learn \u2014 Q4 Kickoff"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
