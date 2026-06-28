"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1FXap6uEnW4B4CBPP0j6n76AdBc6tKrmT34go3AQR6aj",
    "10kfGgfXnFqdbPZFGrBF1us6LWqtBYe0dRdgZZPDFvus",
    "19JW1jb0by2gEvI5KTfvfDyhAUjnEaH15hjj53phNTgx",
    "1UVHZocTFOhmiNso7vx91UQUhP5cDEfne8uk4eIysKKF"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "a579849aefda38fac3732fb9b3de81e7",
    "9280f1bf1da04429ee234567c177019f",
    "5d1f67de5c035b2a51a59fb115924cf6",
    "9a20d0e92ed7af094e82f15d14ef0bcd"
]

LEGIT_PERM_IDS = [
    "376721581f6a3a972baa333fe581964f"
]

NEEDLES = [
    {
        "id": "1FXap6uEnW4B4CBPP0j6n76AdBc6tKrmT34go3AQR6aj",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "a579849aefda38fac3732fb9b3de81e7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "10kfGgfXnFqdbPZFGrBF1us6LWqtBYe0dRdgZZPDFvus",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "9280f1bf1da04429ee234567c177019f",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "19JW1jb0by2gEvI5KTfvfDyhAUjnEaH15hjj53phNTgx",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5d1f67de5c035b2a51a59fb115924cf6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1UVHZocTFOhmiNso7vx91UQUhP5cDEfne8uk4eIysKKF",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "9a20d0e92ed7af094e82f15d14ef0bcd",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ebo72Je2aaaN6CwzxaiW2Zy2PDIuqR9wSeOhbvnxVED",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1kJsH9eG9oYOU5sBz4wZQV06QV5X34QYix7VbkbIXcDE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1dBI8dOoPZInZRthOG3Lsy8AGt7PT2cysaEvhxwKMcSF",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1RLTBH6bgArStTQlVi5Xbe5ans6CSPK1pHVCaYlUwWfc",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "376721581f6a3a972baa333fe581964f",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
