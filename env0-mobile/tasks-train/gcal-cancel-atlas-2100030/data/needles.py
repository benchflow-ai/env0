"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Vendor Check-in \u2014 Atlas",
        "location": "Conference Room A",
        "days_from_now": 13,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Budget Planning \u2014 Atlas",
        "location": "Conference Room C",
        "days_from_now": 2,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Atlas",
        "location": "Conference Room B",
        "days_from_now": 8,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Atlas",
        "location": "Phone",
        "days_from_now": 9,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 Atlas",
        "location": "Conference Room A",
        "days_from_now": 5,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Vendor Check-in \u2014 Atlas",
    "Budget Planning \u2014 Atlas",
    "Design Review \u2014 Atlas"
]

KEEP_SUMMARIES = [
    "Team Standup \u2014 Atlas",
    "Customer Onboarding \u2014 Atlas"
]

GCAL_FILL_CONFIG = {'target_count': 18, 'include_needles': True}
