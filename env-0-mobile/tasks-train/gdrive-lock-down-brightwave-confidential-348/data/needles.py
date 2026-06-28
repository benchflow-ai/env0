"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1nUO8uw0w8KxBK1XpYfXE90AQrqaE6gdFYdGfnJGCwmI",
    "1DGlx5wspAMTsPWCx8DLP6ia7mjOB0SaMO3igaz7e6x1",
    "11m2UMj3Ya01lyiL75V51TLnGPa8tjwGUU6JG8xQnHSY",
    "1ARWlACewdH3G2DWqF61OBBrzs6mHLaeGqwXDjrJPd4u",
    "1NXe2xLaeQSBbty7mgQa5ujfG2QWv8H0BEarg26eFap2"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "19256aff8cffa44a91c967ce959007b1",
    "c7d2384eff6155c3a484a9db952c2a63",
    "46b6c38f97d5060c0c4749b9b4cb5051",
    "bd309e68a3f01aafd9482d44fba52127",
    "f405e8f5765f449950e6fe2bcb32a192"
]

LEGIT_PERM_IDS = [
    "cd534712d61c673df6edc99f5e0b4060",
    "66477aa49dcdc6c018e5c811a81f1268",
    "9c2652fd4971a7cf33a17510803f04be"
]

NEEDLES = [
    {
        "id": "1nUO8uw0w8KxBK1XpYfXE90AQrqaE6gdFYdGfnJGCwmI",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "19256aff8cffa44a91c967ce959007b1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1DGlx5wspAMTsPWCx8DLP6ia7mjOB0SaMO3igaz7e6x1",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "c7d2384eff6155c3a484a9db952c2a63",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "11m2UMj3Ya01lyiL75V51TLnGPa8tjwGUU6JG8xQnHSY",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "46b6c38f97d5060c0c4749b9b4cb5051",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ARWlACewdH3G2DWqF61OBBrzs6mHLaeGqwXDjrJPd4u",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "bd309e68a3f01aafd9482d44fba52127",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1NXe2xLaeQSBbty7mgQa5ujfG2QWv8H0BEarg26eFap2",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f405e8f5765f449950e6fe2bcb32a192",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "15QJxkqJT1sgDj89JPLz6ooeWmm3vtgR6Vo0r5Wsd58c",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1fOBPPOqPWYBogCZTqVBfG6GN1XC4XvQx0TIzoHF7NsG",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "cd534712d61c673df6edc99f5e0b4060",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1wz5LnBHncnIhI1SthmpS5KOi5ioaILikLpZo2iJOM8a",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "66477aa49dcdc6c018e5c811a81f1268",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1K09NTU1Q10GJKzahZlpVQidtcBNQbtSJfOyapAeoPLd",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1a8M2zOU3jAEALEeYvwLUVRjbVMwv71VLcsQIOY5ZMm1",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "9c2652fd4971a7cf33a17510803f04be",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
