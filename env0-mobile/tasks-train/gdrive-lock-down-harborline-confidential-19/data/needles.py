"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1D5qEMxCMhkkBQEnVPy6Wp6UwwIyVruA0guieBAx4hb0",
    "1Kzgo5KIgaJFvJ2m7P7DJAicZ9OeQttDpTlalEgSFeg9",
    "1cpgAl0bkwQDG4hSDDczuPVAVpI6YXhO2dKCQZb4tO0R"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "4e2b89690a24294a2e0868a0cc4bcc78",
    "ff6275b03f95790b0a44c7e8ae4a4d01",
    "615a6b8274649c58d1db4e2df3f08e97"
]

LEGIT_PERM_IDS = [
    "fbc53e9da1b6179076a550412d7d01fa",
    "b1418de29fbbd4d4123ffd189385bd7d"
]

NEEDLES = [
    {
        "id": "1D5qEMxCMhkkBQEnVPy6Wp6UwwIyVruA0guieBAx4hb0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "4e2b89690a24294a2e0868a0cc4bcc78",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Kzgo5KIgaJFvJ2m7P7DJAicZ9OeQttDpTlalEgSFeg9",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "ff6275b03f95790b0a44c7e8ae4a4d01",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1cpgAl0bkwQDG4hSDDczuPVAVpI6YXhO2dKCQZb4tO0R",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "615a6b8274649c58d1db4e2df3f08e97",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1k5QrbXlGZJIeMRk3gY4Jfe1iOQM55q0SwhXf0xbLUnX",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "19MnsAgU7VsmcgWkmENxbCQd2AwcKoPH6Ty76NR8G6cO",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1WYLFs62W2gnWqW3CumHBnMvvrZ55pTkBL3tbyCEVTdz",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "fbc53e9da1b6179076a550412d7d01fa",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1AvsIh7IPbf0BOy0oePcAxxoVbRDRytASkAdestaKDr9",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1MUguszyGpUV4YueyjBiE3ZxsXLYLMQ7xfXz9fD67W7O",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b1418de29fbbd4d4123ffd189385bd7d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
