"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Northstar",
        "location": "Conference Room C",
        "days_from_now": 2,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Northstar",
        "location": "Google Meet",
        "days_from_now": 5,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Northstar",
        "location": "Conference Room B",
        "days_from_now": 1,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Northstar",
        "location": "Conference Room A",
        "days_from_now": 12,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Northstar",
    "Roadmap Sync \u2014 Northstar"
]

KEEP_SUMMARIES = [
    "Customer Onboarding \u2014 Northstar",
    "Product Demo \u2014 Northstar"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
