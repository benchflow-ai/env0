"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1nn00OQsIQhn7vJNdWLlTLWLP6OS5ot2AhMgM9Qm83E0",
    "1Rlu1nmce55N0LBR9cBOfol5yTECfhWt5xBTKmqZcBxd",
    "1LrX8sfBN7nNXyKHPpsHWJATz0yVIbIxrqz5r5OHuKLx"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "a7c8216781a0ed40ac07886a3c03e54a",
    "6d8e0fc652a5911d198f61fe0a3af455",
    "8851a8549d619890bf9302b6de6eead4"
]

LEGIT_PERM_IDS = [
    "619ff132b5758e67fd8614bbe4d34b2d",
    "0e4b70c1b9ca79ef0eee81ae0b889d51"
]

NEEDLES = [
    {
        "id": "1nn00OQsIQhn7vJNdWLlTLWLP6OS5ot2AhMgM9Qm83E0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "a7c8216781a0ed40ac07886a3c03e54a",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Rlu1nmce55N0LBR9cBOfol5yTECfhWt5xBTKmqZcBxd",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "6d8e0fc652a5911d198f61fe0a3af455",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LrX8sfBN7nNXyKHPpsHWJATz0yVIbIxrqz5r5OHuKLx",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "8851a8549d619890bf9302b6de6eead4",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1CIf3MXlKPjSTpNqUFPfUmKFzx6iz4nxDBogLBu0hEuc",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "619ff132b5758e67fd8614bbe4d34b2d",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1nwsVtMimOTlqGaAfjwngLzNVYAWA47WkRVRVDmx901H",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1V0WnOGibMpCTK90d2KQub7DIb5eJC7fZBNJtjV5Zkes",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1jm8wVKm87d1CMXMVZDMdVY3W1FCEk8m32wym6Jn3XmT",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1oR5jadC8me0SDFulW7kw31qZlypDuKUlKehyNiHxwhx",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0e4b70c1b9ca79ef0eee81ae0b889d51",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
