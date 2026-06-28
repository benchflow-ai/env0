"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Vendor Check-in \u2014 Falcon",
        "location": "Zoom",
        "days_from_now": 4,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Budget Planning \u2014 Falcon",
        "location": "Zoom",
        "days_from_now": 7,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Falcon",
        "location": "Zoom",
        "days_from_now": 10,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Falcon",
        "location": "Google Meet",
        "days_from_now": 12,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Falcon",
        "location": "Phone",
        "days_from_now": 8,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Falcon",
        "location": "Conference Room A",
        "days_from_now": 2,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Vendor Check-in \u2014 Falcon",
    "Budget Planning \u2014 Falcon",
    "Roadmap Sync \u2014 Falcon"
]

KEEP_SUMMARIES = [
    "Team Standup \u2014 Falcon",
    "Product Demo \u2014 Falcon",
    "Customer Onboarding \u2014 Falcon"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
