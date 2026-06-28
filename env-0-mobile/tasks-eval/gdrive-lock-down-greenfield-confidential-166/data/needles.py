"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1ZNDGnQRxjsXVVe8QoDNv2drCl5QAFBmEA5ETzFeXmZt",
    "1ddrUQW6BBscoUVJO6YQsSLK2tZePSJGzTqm0oWWqacr",
    "1xxuv8NHy4rkmWQzPs3pqKYnltPKzg57hD4vZlh2B2yR"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "53efc22b257a271c93cd8658633075e8",
    "65d5ba3b0eaaf768eab637fe57d18e0e",
    "b7be0ca4b9723ccb1d0c7501807b8ec0"
]

LEGIT_PERM_IDS = [
    "a2c85919ba73deb06acb5569e65f9e3a",
    "132e02c60bc43c84c5ca7a99edd60408"
]

NEEDLES = [
    {
        "id": "1ZNDGnQRxjsXVVe8QoDNv2drCl5QAFBmEA5ETzFeXmZt",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "53efc22b257a271c93cd8658633075e8",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1ddrUQW6BBscoUVJO6YQsSLK2tZePSJGzTqm0oWWqacr",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "65d5ba3b0eaaf768eab637fe57d18e0e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xxuv8NHy4rkmWQzPs3pqKYnltPKzg57hD4vZlh2B2yR",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "b7be0ca4b9723ccb1d0c7501807b8ec0",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1biDY4wpkhjmnyUdujI09qwSF3biDJbMZynzrtHMppOQ",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1ud5mxzWqlBIEGcO9wqotwlQz9L7DraCScTCJu69jRxU",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a2c85919ba73deb06acb5569e65f9e3a",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1J7KTyflB2xEhudb5fyRtd4KVYN6Vx2chpImWKbHEvaR",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1r643Nvqq90wZgXOpx8SAFnNh0Ou11xP3eLDB9xRlMrO",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "132e02c60bc43c84c5ca7a99edd60408",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
