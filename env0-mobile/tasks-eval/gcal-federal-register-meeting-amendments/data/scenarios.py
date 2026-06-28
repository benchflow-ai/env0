"""Real-world task data for amended Federal Register meeting notices."""

from __future__ import annotations


TASK_NAME = "gcal-federal-register-meeting-amendments"

SOURCES = {
    "fort_hancock_original": (
        "https://www.federalregister.gov/documents/2024/10/03/2024-22761/"
        "gateway-national-recreation-area-fort-hancock-21st-century-advisory-committee-notice-of-public"
    ),
    "fort_hancock_amendment": (
        "https://www.federalregister.gov/documents/2025/01/14/2025-00614/"
        "notice-of-cancellation-and-rescheduling-of-the-public-meeting-of-the-gateway-national-recreation"
    ),
    "nps_board_original": (
        "https://www.federalregister.gov/documents/2023/12/28/2023-28710/"
        "notice-of-public-meeting-for-the-national-park-system-advisory-board"
    ),
    "nps_board_amendment": (
        "https://www.federalregister.gov/documents/2024/02/23/2024-03755/"
        "notice-of-cancellation-and-rescheduling-of-the-public-meeting-for-the-national-park-system-advisory"
    ),
}


FORT_HANCOCK_SUMMARY = (
    "Gateway National Recreation Area Fort Hancock 21st Century Advisory Committee "
    "Notice of Public Meetings"
)
NPS_BOARD_SUMMARY = "Notice of Public Meeting for the National Park System Advisory Board"


SCENARIOS = [
    {
        "id": "update_fort_hancock_january",
        "action": "update",
        "seed_event": {
            "summary": FORT_HANCOCK_SUMMARY,
            "start_iso": "2025-01-15T14:00:00Z",
            "end_iso": "2025-01-15T19:00:00Z",
            "location": "Virtual",
            "description": SOURCES["fort_hancock_original"],
            "calendar": "primary",
        },
        "target_event": {
            "summary": FORT_HANCOCK_SUMMARY,
            "start_iso": "2025-02-06T14:00:00Z",
            "end_iso": "2025-02-06T17:00:00Z",
            "location": "Online Conference",
            "description": SOURCES["fort_hancock_amendment"],
            "calendar": "primary",
        },
        "source_urls": [SOURCES["fort_hancock_original"], SOURCES["fort_hancock_amendment"]],
    },
    {
        "id": "update_nps_board_day_one",
        "action": "update",
        "seed_event": {
            "summary": NPS_BOARD_SUMMARY,
            "start_iso": "2024-03-07T17:00:00Z",
            "end_iso": "2024-03-08T01:00:00Z",
            "location": "At or near Joshua Tree National Park, California",
            "description": SOURCES["nps_board_original"],
            "calendar": "primary",
        },
        "target_event": {
            "summary": NPS_BOARD_SUMMARY,
            "start_iso": "2024-05-01T13:00:00Z",
            "end_iso": "2024-05-01T21:00:00Z",
            "location": "Stuart Lee Udall Department of the Interior Building, 1849 C Street NW, Washington, DC 20240",
            "description": SOURCES["nps_board_amendment"],
            "calendar": "primary",
        },
        "source_urls": [SOURCES["nps_board_original"], SOURCES["nps_board_amendment"]],
    },
    {
        "id": "update_nps_board_day_two",
        "action": "update",
        "seed_event": {
            "summary": NPS_BOARD_SUMMARY,
            "start_iso": "2024-03-08T17:00:00Z",
            "end_iso": "2024-03-09T01:00:00Z",
            "location": "At or near Joshua Tree National Park, California",
            "description": SOURCES["nps_board_original"],
            "calendar": "primary",
        },
        "target_event": {
            "summary": NPS_BOARD_SUMMARY,
            "start_iso": "2024-05-02T13:00:00Z",
            "end_iso": "2024-05-02T21:00:00Z",
            "location": "Stuart Lee Udall Department of the Interior Building, 1849 C Street NW, Washington, DC 20240",
            "description": SOURCES["nps_board_amendment"],
            "calendar": "primary",
        },
        "source_urls": [SOURCES["nps_board_original"], SOURCES["nps_board_amendment"]],
    },
    {
        "id": "trap_fort_hancock_may",
        "action": "trap",
        "seed_event": {
            "summary": FORT_HANCOCK_SUMMARY,
            "start_iso": "2025-05-08T13:00:00Z",
            "end_iso": "2025-05-08T18:00:00Z",
            "location": "Virtual",
            "description": SOURCES["fort_hancock_original"],
            "calendar": "primary",
        },
        "source_urls": [SOURCES["fort_hancock_original"]],
    },
    {
        "id": "trap_fort_hancock_october",
        "action": "trap",
        "seed_event": {
            "summary": FORT_HANCOCK_SUMMARY,
            "start_iso": "2025-10-10T13:00:00Z",
            "end_iso": "2025-10-10T18:00:00Z",
            "location": "Virtual",
            "description": SOURCES["fort_hancock_original"],
            "calendar": "primary",
        },
        "source_urls": [SOURCES["fort_hancock_original"]],
    },
]
