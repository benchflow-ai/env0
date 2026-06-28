"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Budget Planning \u2014 Project Nova",
        "location": "Conference Room C",
        "days_from_now": 8,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Project Nova",
        "location": "Zoom",
        "days_from_now": 2,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Project Nova",
        "location": "Zoom",
        "days_from_now": 9,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Project Nova",
        "location": "Phone",
        "days_from_now": 11,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Project Nova",
        "location": "Conference Room B",
        "days_from_now": 6,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Budget Planning \u2014 Project Nova",
    "Roadmap Sync \u2014 Project Nova"
]

KEEP_SUMMARIES = [
    "Customer Onboarding \u2014 Project Nova",
    "Lunch & Learn \u2014 Project Nova",
    "Eng Office Hours \u2014 Project Nova"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
