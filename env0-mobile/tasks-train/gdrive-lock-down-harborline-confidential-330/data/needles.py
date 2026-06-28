"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1QlS7XOiasGlUaKXa48Uz8usxR0xTwApYGT8JyxIk4Fc",
    "1u9Y4CuKczpvjhpKbvkOLYoKxECbY9eLAG5vFI7XlVxP",
    "10pEaT6qCb74Qfr0YC3MA53K6bfbKz3AlvxmiOeHhLOk"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "a35dce576d74128592dd0fcdf80910c0",
    "3af9f31495fbe605e95a3a5d04cc357f",
    "45c5c605b9913a602ec74e85c26ad3b6"
]

LEGIT_PERM_IDS = [
    "7740b43214cdb9ac0632fcbedd8b1205"
]

NEEDLES = [
    {
        "id": "1QlS7XOiasGlUaKXa48Uz8usxR0xTwApYGT8JyxIk4Fc",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "a35dce576d74128592dd0fcdf80910c0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1u9Y4CuKczpvjhpKbvkOLYoKxECbY9eLAG5vFI7XlVxP",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "3af9f31495fbe605e95a3a5d04cc357f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "10pEaT6qCb74Qfr0YC3MA53K6bfbKz3AlvxmiOeHhLOk",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "45c5c605b9913a602ec74e85c26ad3b6",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "10LJDSrSGvoYbPk5iKzL9g15Oz5G9cG5h7qD4lG4rRNN",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1YGWNhBZrQf2jIomgfAgP3sWkmKKY9Whd9E5e22VnIbO",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1gVBbvWCq44Kkx2VFPjq9wRKeQw11sQtbNI9cjKaOqVs",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7740b43214cdb9ac0632fcbedd8b1205",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1fMHjOp2Z7Tho0bLmezYuj1XqnnqPrSQE9NWNmRDDJ8L",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
