"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Analytics Review \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 8,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Hiring Debrief \u2014 Phoenix",
        "location": "Conference Room C",
        "days_from_now": 4,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Phoenix",
        "location": "Zoom",
        "days_from_now": 12,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Phoenix",
        "location": "Phone",
        "days_from_now": 10,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Analytics Review \u2014 Phoenix",
    "Hiring Debrief \u2014 Phoenix"
]

KEEP_SUMMARIES = [
    "Lunch & Learn \u2014 Phoenix",
    "Customer Onboarding \u2014 Phoenix"
]

GCAL_FILL_CONFIG = {'target_count': 18, 'include_needles': True}
