"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1qkAC5lm7XPPfKzLmoRd2gJAYqTfERqs4Ve8WmQU6FMg",
    "14dYYvOQz2echtXq2luyWyBjf2euEFrHV36xxWKwpJjL",
    "1Cy82nMDA2WO7srvW9TJ0BCqOq5LyEyhjev7UQuHf1wx"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "7c0f40855e2d6681c70e1ccf114400e9",
    "8fc8955f567cf4b3fe652f4ac2218d83",
    "d6cb490e136476502ee56886d423fb43"
]

LEGIT_PERM_IDS = [
    "bc36d2264e409f7e6f781c4517861d2e",
    "f8e7ae7c030e1eab5d4865eed6d5d896"
]

NEEDLES = [
    {
        "id": "1qkAC5lm7XPPfKzLmoRd2gJAYqTfERqs4Ve8WmQU6FMg",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "7c0f40855e2d6681c70e1ccf114400e9",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "14dYYvOQz2echtXq2luyWyBjf2euEFrHV36xxWKwpJjL",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "8fc8955f567cf4b3fe652f4ac2218d83",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Cy82nMDA2WO7srvW9TJ0BCqOq5LyEyhjev7UQuHf1wx",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "d6cb490e136476502ee56886d423fb43",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1sPqzLuO6AKThkfsmvKEdOCYZ9f6CykQTOxFlfk31Zly",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "bc36d2264e409f7e6f781c4517861d2e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "18wtfDy1wG0mBkaLCkrz70vhbzpopDmvs8agghK3oamD",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1h05B3EKloZXqgcQZqYo6cp4CNHb1T4LTvP29NlEhuCc",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1HT8spG16hNfBmzftUTK02h92zxWzxnFUORs330cfGyV",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1imZNSi7c5sabQQNXzTUZzuylVPT8sjnmCADmOkCzAIC",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "16eVE6C6Q1g3Tmu1yXaqya3gUz9TzOl13mJdKFl2sVvB",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f8e7ae7c030e1eab5d4865eed6d5d896",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
