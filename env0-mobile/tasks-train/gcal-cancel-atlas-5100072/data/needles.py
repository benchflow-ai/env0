"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Atlas",
        "location": "Conference Room A",
        "days_from_now": 12,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Atlas",
        "location": "Conference Room B",
        "days_from_now": 5,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Atlas",
        "location": "Phone",
        "days_from_now": 11,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Atlas",
        "location": "Auditorium",
        "days_from_now": 10,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Atlas",
        "location": "Google Meet",
        "days_from_now": 7,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Atlas",
    "Roadmap Sync \u2014 Atlas",
    "Partner Call \u2014 Atlas"
]

KEEP_SUMMARIES = [
    "Eng Office Hours \u2014 Atlas",
    "Customer Onboarding \u2014 Atlas"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
