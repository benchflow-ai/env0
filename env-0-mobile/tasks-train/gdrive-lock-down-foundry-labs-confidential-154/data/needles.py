"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "13ZdI1ppZi2cqfY7EaYD29Rdz9OvZRjxpa9tgITk2bJ8",
    "1XE78tUNu2k5gsf4Lc6pCvqr0d5HjjJ6X4nq2yHYjbVU",
    "1upX290FwbMEX4qxUbZZSFyVHI9NwJIr6IODwP7JQMTB"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "c4673e29712020dbbc42d2d4938109ec",
    "2917f3f365087cedd50e93f1d1003199",
    "8321da12697e31736280baf719b6d83b"
]

LEGIT_PERM_IDS = [
    "bd37dce25e0a1170a5b36760bd692058",
    "eedd87c7f7477198117dbcd8b56a1adb"
]

NEEDLES = [
    {
        "id": "13ZdI1ppZi2cqfY7EaYD29Rdz9OvZRjxpa9tgITk2bJ8",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c4673e29712020dbbc42d2d4938109ec",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1XE78tUNu2k5gsf4Lc6pCvqr0d5HjjJ6X4nq2yHYjbVU",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "2917f3f365087cedd50e93f1d1003199",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1upX290FwbMEX4qxUbZZSFyVHI9NwJIr6IODwP7JQMTB",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "8321da12697e31736280baf719b6d83b",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1vHdaAJuFhXv1KmJtOni7DtH92dYrge32oN6fJdA7mT2",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "bd37dce25e0a1170a5b36760bd692058",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1oZphXZd3rzkDoiY3NzTTVxIIkMpXhfjQ2xG3QyLeoDz",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1le4d91oW72Rxuei6nc9tB6mebTWClMxAY269eQkQfWB",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1eJ4PNXx3VmNKlKj4m8mkvbH5wsa0OcLWLTiRI4oOLWN",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1sQwmunwZbuL4aJKOohEKr9Dz09KmqN49UT6uRTJaBOv",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "eedd87c7f7477198117dbcd8b56a1adb",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
