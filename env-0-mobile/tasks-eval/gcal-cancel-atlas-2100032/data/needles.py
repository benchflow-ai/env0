"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Atlas",
        "location": "Phone",
        "days_from_now": 3,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Vendor Check-in \u2014 Atlas",
        "location": "Auditorium",
        "days_from_now": 2,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Atlas",
        "location": "Conference Room B",
        "days_from_now": 4,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Atlas",
        "location": "Auditorium",
        "days_from_now": 9,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Lunch & Learn \u2014 Atlas",
        "location": "Google Meet",
        "days_from_now": 11,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Atlas",
    "Vendor Check-in \u2014 Atlas",
    "Partner Call \u2014 Atlas"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Atlas",
    "Lunch & Learn \u2014 Atlas"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
