# Source Provenance

All user-visible titles, dates, times, and locations in this task come from
official Federal Register notices.
The seeded calendar `description` fields store the exact Federal Register notice
URL for each event, avoiding synthesized calendar metadata.
No synthetic filler events are seeded for this task; every task-specific event
comes from those official notices.

The seeded calendar stores timestamps in UTC. The Federal Register notices use
local source timezones (Eastern and Pacific Standard Time), so the UTC values
below are exact conversions used by the task harness.

## Primary sources

- Fort Hancock original notice:
  `https://www.federalregister.gov/documents/2024/10/03/2024-22761/gateway-national-recreation-area-fort-hancock-21st-century-advisory-committee-notice-of-public`
- Fort Hancock rescheduling notice:
  `https://www.federalregister.gov/documents/2025/01/14/2025-00614/notice-of-cancellation-and-rescheduling-of-the-public-meeting-of-the-gateway-national-recreation`
- National Park System Advisory Board original notice:
  `https://www.federalregister.gov/documents/2023/12/28/2023-28710/notice-of-public-meeting-for-the-national-park-system-advisory-board`
- National Park System Advisory Board rescheduling notice:
  `https://www.federalregister.gov/documents/2024/02/23/2024-03755/notice-of-cancellation-and-rescheduling-of-the-public-meeting-for-the-national-park-system-advisory`

## Seeded / expected events

| Action | Summary | Original official time | Updated official time | Seeded / expected UTC | Location |
| --- | --- | --- | --- | --- | --- |
| update | `Gateway National Recreation Area Fort Hancock 21st Century Advisory Committee Notice of Public Meetings` | 2025-01-15 09:00-14:00 Eastern | 2025-02-06 09:00-12:00 Eastern | 2025-01-15 14:00-19:00 Z -> 2025-02-06 14:00-17:00 Z | `Online Conference` |
| update | `Notice of Public Meeting for the National Park System Advisory Board` | 2024-03-07 09:00-17:00 PST | 2024-05-01 09:00-17:00 Eastern | 2024-03-07 17:00 Z -> 2024-03-08 01:00 Z -> 2024-05-01 13:00-21:00 Z | `Joshua Tree` -> `Stuart Lee Udall Department of the Interior Building, 1849 C Street NW, Washington, DC 20240` |
| update | `Notice of Public Meeting for the National Park System Advisory Board` | 2024-03-08 09:00-17:00 PST | 2024-05-02 09:00-17:00 Eastern | 2024-03-08 17:00 Z -> 2024-03-09 01:00 Z -> 2024-05-02 13:00-21:00 Z | `Joshua Tree` -> `Stuart Lee Udall Department of the Interior Building, 1849 C Street NW, Washington, DC 20240` |
| keep | `Gateway National Recreation Area Fort Hancock 21st Century Advisory Committee Notice of Public Meetings` | 2025-05-08 09:00-14:00 Eastern | unchanged | 2025-05-08 13:00-18:00 Z | `Virtual` |
| keep | `Gateway National Recreation Area Fort Hancock 21st Century Advisory Committee Notice of Public Meetings` | 2025-10-10 09:00-14:00 Eastern | unchanged | 2025-10-10 13:00-18:00 Z | `Virtual` |

## Evaluator checks

- The January 15 Fort Hancock meeting must be rescheduled to February 6 with
  the shorter duration preserved in UTC.
- Both March National Park System Advisory Board meetings must move to May and
  take the amended Washington, DC location.
- The May and October Fort Hancock meetings must remain present and unchanged.
