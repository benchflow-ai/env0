"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1gAwaEbjdxUVrhpe7p7ppbG93WfqboaTdXIkqeyi9IhI",
    "1HaIE4EFBbZjvBIcgNgck01EI4Bqpf05hh5OfrbiZZfR",
    "1zC4T3cmgL68PUtUvZrWdtuCVVwHJGYPkQ1HOXEOshpF"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "85ae72c5be7ca6e242320625b158d0de",
    "b62a7c48e68845d5680d60b1db312730",
    "ec864d608456eddb69dc4fc1e193ac19"
]

LEGIT_PERM_IDS = [
    "24c7a38eb35e5af0cadfa0d826cdd480",
    "947f0e0d1b1583abc661a80b5c69b8c8",
    "94c365ddae5646272de9abc96c2a0977"
]

NEEDLES = [
    {
        "id": "1gAwaEbjdxUVrhpe7p7ppbG93WfqboaTdXIkqeyi9IhI",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "85ae72c5be7ca6e242320625b158d0de",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1HaIE4EFBbZjvBIcgNgck01EI4Bqpf05hh5OfrbiZZfR",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "b62a7c48e68845d5680d60b1db312730",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1zC4T3cmgL68PUtUvZrWdtuCVVwHJGYPkQ1HOXEOshpF",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ec864d608456eddb69dc4fc1e193ac19",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1dZgckiRMFXShZPdHfuUYgW7Ml517S7xhY8BXY8gXT1b",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "24c7a38eb35e5af0cadfa0d826cdd480",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1RMMOon9B9GpqnxoFJujZhE4JA7aTN4uXqpJTUj1KpDL",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1S32sJBr4YcLXCw9eBbU6yXT9DoJDcDt5aHEbvVCYWUq",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "947f0e0d1b1583abc661a80b5c69b8c8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1wlNOcgvwifdKiq3I7udJ7u7dvCmu5I3ZeUIuYgm3lwW",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "94c365ddae5646272de9abc96c2a0977",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1dqZAz44TQbe8vBQ7vTJpqesdNtnjhlMDXh1QTecclqw",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
