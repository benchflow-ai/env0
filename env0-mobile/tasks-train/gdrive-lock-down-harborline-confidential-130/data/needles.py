"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1tbM3kf3pxMZ4cgFfThJgj64QBxWABVlcuaK4bUbuZOY",
    "1CajyZ2dXZEkuUz3BpEYq1SrubigKUqWFqxFzxvNkTQX",
    "1CpW3FBAUXaKiZFRDiIbNwsgLi4RLjmfZ0lOJFV18Xbu",
    "1DWof1UNXZlqH4s59pm9qyqWL0voWkBSUx2QbrtTUtNX",
    "1I1dJG05XzJcGWheI0DdYQYAAywJzQHKgECBVRneo4Xb"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "c12199269212d83d9bdfafea4ffe6ee1",
    "2e8cca764e91742a42be44dc9c13eea1",
    "49f3e54cf8ff891f17c20bcd703300c1",
    "75106b2994e60a2fd11d4467850be2e1",
    "65ebc3dda3c980bf9e944cc96f058b19"
]

LEGIT_PERM_IDS = [
    "97b1e582564b54f444626e96d6b599d0"
]

NEEDLES = [
    {
        "id": "1tbM3kf3pxMZ4cgFfThJgj64QBxWABVlcuaK4bUbuZOY",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "c12199269212d83d9bdfafea4ffe6ee1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1CajyZ2dXZEkuUz3BpEYq1SrubigKUqWFqxFzxvNkTQX",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "2e8cca764e91742a42be44dc9c13eea1",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1CpW3FBAUXaKiZFRDiIbNwsgLi4RLjmfZ0lOJFV18Xbu",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "49f3e54cf8ff891f17c20bcd703300c1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1DWof1UNXZlqH4s59pm9qyqWL0voWkBSUx2QbrtTUtNX",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "75106b2994e60a2fd11d4467850be2e1",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1I1dJG05XzJcGWheI0DdYQYAAywJzQHKgECBVRneo4Xb",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "65ebc3dda3c980bf9e944cc96f058b19",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1m5KrVDqQ8WcgCzEXHJ3WzQL3X9gEt31dczB3ZEG2siE",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1hrrwq1XVbTKNpRN1bLPgPdhdIL10cHILuO4OCzgfzk0",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "97b1e582564b54f444626e96d6b599d0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1VwhbF07X34uqnJH9Y95wKm7yf6e4P44ec4Krx1kLO2p",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1vndrz3581bhLoKWKZ1MGSY3pZUS5vTPMP7tefz74tjG",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
