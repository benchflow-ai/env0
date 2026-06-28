"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Helix",
        "location": "Conference Room C",
        "days_from_now": 12,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Helix",
        "location": "Conference Room B",
        "days_from_now": 7,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Helix",
        "location": "Conference Room A",
        "days_from_now": 2,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Helix",
        "location": "Conference Room A",
        "days_from_now": 11,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Helix",
        "location": "Phone",
        "days_from_now": 4,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Helix",
    "Design Review \u2014 Helix",
    "Partner Call \u2014 Helix"
]

KEEP_SUMMARIES = [
    "Customer Onboarding \u2014 Helix",
    "1:1 with Manager \u2014 Helix"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
