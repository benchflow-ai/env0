"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "13QM1zqUnlN5n0IV4t0kcCCZnUZqaRrISXe8u7nNiCJV",
    "1nbHTb1H8RkYHNqZgcMf61w1YJmF610uPrdlxpGHqIUD",
    "1bVOrmcyVOQ4TJUnIvVLpPddxjx8bXLoOdHNssVpaWbj"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "bc4dafd50e2f558e41b8c13cc5bd93c0",
    "9b1d1147dcd9e541109a2556a5c39c62",
    "36d304fca20f1a1227e09629274a32c8"
]

LEGIT_PERM_IDS = [
    "8cc8e284afb8fa969b0214ca0e843035",
    "e193cf10bc6102490f5915edfe7418e4"
]

NEEDLES = [
    {
        "id": "13QM1zqUnlN5n0IV4t0kcCCZnUZqaRrISXe8u7nNiCJV",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "bc4dafd50e2f558e41b8c13cc5bd93c0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1nbHTb1H8RkYHNqZgcMf61w1YJmF610uPrdlxpGHqIUD",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "9b1d1147dcd9e541109a2556a5c39c62",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bVOrmcyVOQ4TJUnIvVLpPddxjx8bXLoOdHNssVpaWbj",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "36d304fca20f1a1227e09629274a32c8",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1fKZn4FVtgMk07OBjtrAX12qwb1J5WOynLQbAn7bW79i",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1qbMa6TAoI71GuqxtqBC56QG6ZL4e4G50XGSbWt4Hys3",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "8cc8e284afb8fa969b0214ca0e843035",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1pkH3LBC4e13vWMfgkcyevCIqslcJ0VLZ2zQZrqjNyK5",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1rGHReOuwYWQr2W4vm0jPLnENZmHPDXb6Us3JmgQHrE3",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1whmAurNgAfBnE6bfTBsLz400Q2W6kYPISaXzPi73Nxj",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "e193cf10bc6102490f5915edfe7418e4",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1vJE6seZRpQfZ1CHmuw0yxqrbFz7xvfthg9JAsck8dnv",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
