"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Hiring Debrief \u2014 EMEA",
        "location": "Conference Room A",
        "days_from_now": 5,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Budget Planning \u2014 EMEA",
        "location": "Conference Room B",
        "days_from_now": 13,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 EMEA",
        "location": "Phone",
        "days_from_now": 1,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 EMEA",
        "location": "Conference Room B",
        "days_from_now": 8,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Hiring Debrief \u2014 EMEA",
    "Budget Planning \u2014 EMEA"
]

KEEP_SUMMARIES = [
    "Eng Office Hours \u2014 EMEA",
    "Customer Onboarding \u2014 EMEA"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
