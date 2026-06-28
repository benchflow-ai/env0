"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Orbit",
        "location": "Conference Room B",
        "days_from_now": 7,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Orbit",
        "location": "Google Meet",
        "days_from_now": 13,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Orbit",
        "location": "Conference Room A",
        "days_from_now": 10,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Orbit",
        "location": "Conference Room A",
        "days_from_now": 8,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Orbit",
    "Design Review \u2014 Orbit"
]

KEEP_SUMMARIES = [
    "Lunch & Learn \u2014 Orbit",
    "Customer Onboarding \u2014 Orbit"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
