"""Auto-generated env-0 tasks-lite needle data (gcal cancel meetings).
Dependency-free. Dates are relative (days_from_now) -> near-future at seed time."""

NEEDLE_EVENTS = [
    {
        "summary": "Sprint Retro \u2014 Q4 Kickoff",
        "location": "Zoom",
        "days_from_now": 1,
        "start_hour": 15,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Roadmap Sync \u2014 Q4 Kickoff",
        "location": "Conference Room B",
        "days_from_now": 4,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "1:1 with Manager \u2014 Q4 Kickoff",
        "location": "Zoom",
        "days_from_now": 2,
        "start_hour": 13,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "Eng Office Hours \u2014 Q4 Kickoff",
        "location": "Phone",
        "days_from_now": 11,
        "start_hour": 14,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    },
    {
        "summary": "All-Hands \u2014 Q4 Kickoff",
        "location": "Conference Room B",
        "days_from_now": 9,
        "start_hour": 10,
        "duration_hours": 1,
        "status": "confirmed",
        "attendees": []
    }
]

CANCEL_SUMMARIES = [
    "Sprint Retro \u2014 Q4 Kickoff",
    "Roadmap Sync \u2014 Q4 Kickoff"
]

KEEP_SUMMARIES = [
    "1:1 with Manager \u2014 Q4 Kickoff",
    "Eng Office Hours \u2014 Q4 Kickoff",
    "All-Hands \u2014 Q4 Kickoff"
]

GCAL_FILL_CONFIG = {'target_count': 'fixed_only', 'include_needles': True}
