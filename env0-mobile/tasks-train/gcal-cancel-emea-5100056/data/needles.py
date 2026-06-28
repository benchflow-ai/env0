"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Roadmap Sync \u2014 EMEA",
        "location": "Auditorium",
        "days_from_now": 1,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Analytics Review \u2014 EMEA",
        "location": "Conference Room A",
        "days_from_now": 4,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Hiring Debrief \u2014 EMEA",
        "location": "Phone",
        "days_from_now": 10,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 EMEA",
        "location": "Zoom",
        "days_from_now": 7,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 EMEA",
        "location": "Conference Room C",
        "days_from_now": 3,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Roadmap Sync \u2014 EMEA",
    "Analytics Review \u2014 EMEA",
    "Hiring Debrief \u2014 EMEA"
]

KEEP_SUMMARIES = [
    "Eng Office Hours \u2014 EMEA",
    "Customer Onboarding \u2014 EMEA"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
