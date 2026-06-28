"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Partner Call \u2014 Atlas",
        "location": "Conference Room A",
        "days_from_now": 12,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Design Review \u2014 Atlas",
        "location": "Conference Room B",
        "days_from_now": 13,
        "start_hour": 11,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Team Standup \u2014 Atlas",
        "location": "Conference Room C",
        "days_from_now": 3,
        "start_hour": 16,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Atlas",
        "location": "Conference Room B",
        "days_from_now": 4,
        "start_hour": 9,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Security Review \u2014 Atlas",
        "location": "Zoom",
        "days_from_now": 9,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Partner Call \u2014 Atlas",
    "Design Review \u2014 Atlas"
]

KEEP_SUMMARIES = [
    "Team Standup \u2014 Atlas",
    "All-Hands \u2014 Atlas",
    "Security Review \u2014 Atlas"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
