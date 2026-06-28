"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "19kZs8yjWwqppvahg8FilzKc2xP4Df0YqOBoELksdd8J",
    "1NmPPg0sQFmcRSjOUncR6pJpZvMP3zaD1m0Tt3DZlWCb",
    "1YaJCuLlx7luRPcw1PVw8rQs6I1oPAxMTWC4cCN6PJ25",
    "1oFuGIPPbOgNFOJim5VfkUZwowfuNeYNVp6cZ9WO1vfh",
    "1o5EgX6YFJPOmYfHkzS8OcB7JfpyWstbEdQuL4qRhiMZ"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "5969ea842f160452a7f66a6eddade208",
    "8e7078e157ce84c8e512bd9068e6f2ee",
    "630e171390561718b4ff02add4fe8490",
    "0ce92912139cdfba7be40b3721ea2160",
    "b8a89a33f49707533bcff1e9c92d565a"
]

LEGIT_PERM_IDS = [
    "3fa733889e5738f2b201e82775dee3b3",
    "55867c582de0b4f68378ddbd49bebe2a",
    "4ed2b60a55bf9ee8d6450204cab3990d"
]

NEEDLES = [
    {
        "id": "19kZs8yjWwqppvahg8FilzKc2xP4Df0YqOBoELksdd8J",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5969ea842f160452a7f66a6eddade208",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1NmPPg0sQFmcRSjOUncR6pJpZvMP3zaD1m0Tt3DZlWCb",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "8e7078e157ce84c8e512bd9068e6f2ee",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1YaJCuLlx7luRPcw1PVw8rQs6I1oPAxMTWC4cCN6PJ25",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "630e171390561718b4ff02add4fe8490",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1oFuGIPPbOgNFOJim5VfkUZwowfuNeYNVp6cZ9WO1vfh",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "0ce92912139cdfba7be40b3721ea2160",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1o5EgX6YFJPOmYfHkzS8OcB7JfpyWstbEdQuL4qRhiMZ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b8a89a33f49707533bcff1e9c92d565a",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "17RckNly6nc0WAhWnaVWFlI21Rp1EJ0hMpgBoqq0TImJ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "3fa733889e5738f2b201e82775dee3b3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1GuK2YGILh7iBGPoeGyPwJF1oavw82XrUYLoe09g7wDC",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1SfgFk4JuKe0KPlQ1DC6Imz0JWcAOXxpFTiqx4Dq2bcv",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1GK66hzxFLJbtbcwZdB8nmTlXvqldeJUVwAwLQnPNb3e",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "55867c582de0b4f68378ddbd49bebe2a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1yFzIy0h2UQQkiHZsUPl4q9HwvtIxtllD9usQ5XGhHsL",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "4ed2b60a55bf9ee8d6450204cab3990d",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1zu8nzPuNHDc6jLTgosFv8VcfktEtq2ba8dq5LPH4La5",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
