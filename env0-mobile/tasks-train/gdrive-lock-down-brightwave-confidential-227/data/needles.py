"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1PQPdEsUEfpJ94uumpq1ZJ9i8k49cJoMlVuJmZN86VaZ",
    "1lH9B6YdoaPYkVfzA1RRBqzcyvT4Pcxaw9Kj7vOMW4b8",
    "1jYS7zFNwyvlOLxMkNNyKiiR2rxGVIqbltRCMQk9ZlvA",
    "1d3oRJ9Nw0AS90gDwMZeVrK0TGLMqlv4wGB0CYoZNd9i",
    "1A7kRm2wchQCDEr63OPXvBAMdC9Emdeg8j46bPneHpkI"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "d05754f3d117e9c6017c7f17afa7952d",
    "cd74a9e9126166646a6315e1b3957c11",
    "0b55973bc9d2792fce2e5eba3f4b484d",
    "826f621b4827edd3fb0743b31e305e7a",
    "ed080181bb64dbe1dcca5aace13205e8"
]

LEGIT_PERM_IDS = [
    "e29ac2715501ad3ef730de318563b77d",
    "4882e75a1210aecd39658521f9a753ef",
    "9e677d504cfdb82f24313f177c319a0d"
]

NEEDLES = [
    {
        "id": "1PQPdEsUEfpJ94uumpq1ZJ9i8k49cJoMlVuJmZN86VaZ",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "d05754f3d117e9c6017c7f17afa7952d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1lH9B6YdoaPYkVfzA1RRBqzcyvT4Pcxaw9Kj7vOMW4b8",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "cd74a9e9126166646a6315e1b3957c11",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1jYS7zFNwyvlOLxMkNNyKiiR2rxGVIqbltRCMQk9ZlvA",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0b55973bc9d2792fce2e5eba3f4b484d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1d3oRJ9Nw0AS90gDwMZeVrK0TGLMqlv4wGB0CYoZNd9i",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "826f621b4827edd3fb0743b31e305e7a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1A7kRm2wchQCDEr63OPXvBAMdC9Emdeg8j46bPneHpkI",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "ed080181bb64dbe1dcca5aace13205e8",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Ev5w0xLgi6gMf6FC9HyxlQHaZ8pyoY5XcJSsxfRKSau",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e29ac2715501ad3ef730de318563b77d",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1ZHlPr7g3vgsFqBXnEk2rRXquTG0i1Es0Opt99zqEH3s",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1fQVON4yZlB7vt9i92kyjXlPQREtbWgnNp2zguTrWTVM",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "4882e75a1210aecd39658521f9a753ef",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1sSuqeVY2yd06CuhgtJ3Zjba7iVqYnVxu32pAtfnFndK",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "14U1P7WCYYOTGN4UK7f8yLGnBL3YpltS4ifItqdWsTIp",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9e677d504cfdb82f24313f177c319a0d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
