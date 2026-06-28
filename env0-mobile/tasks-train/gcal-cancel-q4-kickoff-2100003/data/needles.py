"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Vendor Check-in \u2014 Q4 Kickoff",
        "location": "Conference Room A",
        "days_from_now": 12,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Q4 Kickoff",
        "location": "Conference Room B",
        "days_from_now": 11,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Partner Call \u2014 Q4 Kickoff",
        "location": "Conference Room C",
        "days_from_now": 4,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Product Demo \u2014 Q4 Kickoff",
        "location": "Google Meet",
        "days_from_now": 3,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Q4 Kickoff",
        "location": "Google Meet",
        "days_from_now": 6,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Vendor Check-in \u2014 Q4 Kickoff",
    "Design Review \u2014 Q4 Kickoff",
    "Partner Call \u2014 Q4 Kickoff"
]

KEEP_SUMMARIES = [
    "Product Demo \u2014 Q4 Kickoff",
    "1:1 with Manager \u2014 Q4 Kickoff"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
