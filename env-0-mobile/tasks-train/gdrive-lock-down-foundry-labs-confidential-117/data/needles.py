"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "109lxNPAhtDFHQz74UnodrjYUDNQLByR81ggB0r0fXeO",
    "19k4oYMkUF1TRR0MHr6bECR4ElS8k7hrtF8Bhy4CCOlF",
    "1xMTSkru5CMPcDgRBEEKHgkMQ3kph8uWAJzd6eKL4xOL",
    "1dJckIJO2sNIMQfcylgJJYwF4lwutXX65lGR5MhKTYeB",
    "1s3jEdvcA7K2tUyhBU2jx9q7NotrUC17VUoHPB8TZPII"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "1368f00793dbb971ed9d50eba25f8ba0",
    "b717ba6f5cf6a033a7b9ed0395827b16",
    "e1f9461244b43ef7b4585ae1fb2fcc3f",
    "aa2b4206674c0cf79998339b08a62548",
    "c95fc14c04cbbb0a83e11b55646596da"
]

LEGIT_PERM_IDS = [
    "91f18d500f153c6f1dee76b4c2925ef4",
    "d19a7dd7ab6821ad8c2a6702c60ef4d0",
    "35d68d12351d2b30db840b1f59435f89"
]

NEEDLES = [
    {
        "id": "109lxNPAhtDFHQz74UnodrjYUDNQLByR81ggB0r0fXeO",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "1368f00793dbb971ed9d50eba25f8ba0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "19k4oYMkUF1TRR0MHr6bECR4ElS8k7hrtF8Bhy4CCOlF",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "b717ba6f5cf6a033a7b9ed0395827b16",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1xMTSkru5CMPcDgRBEEKHgkMQ3kph8uWAJzd6eKL4xOL",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e1f9461244b43ef7b4585ae1fb2fcc3f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1dJckIJO2sNIMQfcylgJJYwF4lwutXX65lGR5MhKTYeB",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "aa2b4206674c0cf79998339b08a62548",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1s3jEdvcA7K2tUyhBU2jx9q7NotrUC17VUoHPB8TZPII",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "c95fc14c04cbbb0a83e11b55646596da",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1KmPNFWnubmR3ee75pOGGhYGOa6lXocBl6CplZP0EcUM",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "15hLQYDx98kuAcBUFqibM8FzbfYcebUMeWTKqe0fhHAo",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "91f18d500f153c6f1dee76b4c2925ef4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1j9uuMgOT2dK6DTCc1tMFzIeog2JTFdvFuqKRBkhp6Cv",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1uxargen1r0LUZs9MaHE6Oejl1w1nOSsbYWT2IZ5FLv6",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "19SxTlUvX8WKJhZ2H74euNPQ0FX7pZTGXN3Xtxe0nvCJ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d19a7dd7ab6821ad8c2a6702c60ef4d0",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1wdZVlL00N6L4YcWRlx54poF9rSiYT2s55HQ5yEgjCjb",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "35d68d12351d2b30db840b1f59435f89",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
