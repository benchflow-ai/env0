"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1uaHWP35BpEjKzSt3QP2983jSqTmaDVBcKxdrZ30dyk3",
    "1Jmsq0bploWR2QIQBjz9KssJ1D9PDVXDyJmNYoFeropQ",
    "1ywEMUy2lXJyunmTJ9iMCUbwiXOnjjrTOcZZEffDfPoY"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "aef229651af84da0345447dab7e044d3",
    "f94a6353c2bb2fd034f8b52f8fd100e1",
    "e92da542874cd2399406b9ef87550832"
]

LEGIT_PERM_IDS = [
    "63ccb31358a8c54fddc642a67e710a73",
    "86f62acd3907c0b638a32bbb0d7f4590",
    "0f46cb273d3bf75d536fa7608b314762"
]

NEEDLES = [
    {
        "id": "1uaHWP35BpEjKzSt3QP2983jSqTmaDVBcKxdrZ30dyk3",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "aef229651af84da0345447dab7e044d3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Jmsq0bploWR2QIQBjz9KssJ1D9PDVXDyJmNYoFeropQ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "f94a6353c2bb2fd034f8b52f8fd100e1",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1ywEMUy2lXJyunmTJ9iMCUbwiXOnjjrTOcZZEffDfPoY",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "e92da542874cd2399406b9ef87550832",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1jXWz9OeaGM1EbUKO01foC714eYfvp8fB4ORsxrDQ84D",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "16kvFRymJXtqtRlBHLzEkkyMZaaAnhDhPKq5pNt1O4Fc",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "63ccb31358a8c54fddc642a67e710a73",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Re1Xvy6yy0jrQIWZlZdHsLopcMRu0RQYYNXPAGPsQAa",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "86f62acd3907c0b638a32bbb0d7f4590",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1iUgFUrcp8YcmF5Q9H66SoerAhJHBkHQw2yUN2YqbLtg",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "0f46cb273d3bf75d536fa7608b314762",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1GsN8FalZ2eo7mmRHD1Mys451ZpAfcauZXDjgcurAgiA",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
