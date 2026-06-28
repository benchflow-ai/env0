"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Design Review \u2014 EMEA",
        "location": "Zoom",
        "days_from_now": 6,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 EMEA",
        "location": "Auditorium",
        "days_from_now": 1,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 EMEA",
        "location": "Conference Room C",
        "days_from_now": 4,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 EMEA",
        "location": "Conference Room A",
        "days_from_now": 10,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Customer Onboarding \u2014 EMEA",
        "location": "Auditorium",
        "days_from_now": 12,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Design Review \u2014 EMEA",
    "Vendor Check-in \u2014 EMEA"
]

KEEP_SUMMARIES = [
    "Lunch & Learn \u2014 EMEA",
    "Product Demo \u2014 EMEA",
    "Customer Onboarding \u2014 EMEA"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
