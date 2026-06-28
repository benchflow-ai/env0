"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1A3pR6vEy1NeGjtT6RVh2vkdM8q9jRJlVmCKDUKVMnfL",
    "1Je58u7hVlgoj0hyiU7udthXYK8gRAPSVC1A6hJhclQz",
    "1gq0Moujag2xLKcW8kfUmGvdBwyGsFdMF2AqQRUVrqN0",
    "1oDDXHXBuCHluKLHJmtjXQyD1WebclrrkTLTyekqbEuL",
    "1hAS90PCR60b8w7PNKWrZmUHop9LIEnpt021DTxgZ0Ei"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "3d4823dfaafde4002683cea597a0a3f8",
    "03701ed06688118b710cb0ade94aea84",
    "ecdba04061ac5b93a1bfec5a1acd0217",
    "81f8cb5f5195e7ed363c0442a5c90529",
    "5a065d3f19795b1a3507af1411deef9a"
]

LEGIT_PERM_IDS = [
    "694e1608c47e6833fadc93e5043ba171"
]

NEEDLES = [
    {
        "id": "1A3pR6vEy1NeGjtT6RVh2vkdM8q9jRJlVmCKDUKVMnfL",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "3d4823dfaafde4002683cea597a0a3f8",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Je58u7hVlgoj0hyiU7udthXYK8gRAPSVC1A6hJhclQz",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "03701ed06688118b710cb0ade94aea84",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gq0Moujag2xLKcW8kfUmGvdBwyGsFdMF2AqQRUVrqN0",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "ecdba04061ac5b93a1bfec5a1acd0217",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1oDDXHXBuCHluKLHJmtjXQyD1WebclrrkTLTyekqbEuL",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "81f8cb5f5195e7ed363c0442a5c90529",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1hAS90PCR60b8w7PNKWrZmUHop9LIEnpt021DTxgZ0Ei",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "5a065d3f19795b1a3507af1411deef9a",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1huj4jpewMZZFBw70gsE0VfUk88NrcKpnfEGpipvD5p5",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1qlfGOWtITLAXwXOBG8pTLrGNcbDa4GWF7BZNNTEanK8",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1K9Smz6PEWbaNS5IEbm14Knx3sHsudcLodMxg1YOK6tG",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "694e1608c47e6833fadc93e5043ba171",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1OM64rHtQvP4DLiG4R73VFua8CCsnO1GIfir2f9jIabk",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
