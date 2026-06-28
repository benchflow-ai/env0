"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Design Review \u2014 Q3 Planning",
        "location": "Auditorium",
        "days_from_now": 7,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Budget Planning \u2014 Q3 Planning",
        "location": "Conference Room A",
        "days_from_now": 9,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Q3 Planning",
        "location": "Auditorium",
        "days_from_now": 8,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Q3 Planning",
        "location": "Conference Room A",
        "days_from_now": 6,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Q3 Planning",
        "location": "Conference Room B",
        "days_from_now": 5,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Design Review \u2014 Q3 Planning",
    "Budget Planning \u2014 Q3 Planning"
]

KEEP_SUMMARIES = [
    "Lunch & Learn \u2014 Q3 Planning",
    "Customer Onboarding \u2014 Q3 Planning",
    "Product Demo \u2014 Q3 Planning"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
