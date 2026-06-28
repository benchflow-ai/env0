"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1kefYhzknKEiFfEyIKzqSAqQf4HeOzuRY3dVSCx1IWZ8",
    "1nBlL3P5CV7X8mSi4TTtkNRkV67jyGicsMhC3Iuuo7VT",
    "1LkSgLcUArPvCKxWpVhuLQg4M9ywvr7JpQL7YpLGPGkn"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "267c7c9ad5685d20102eb5f3e188fffc",
    "02275dba5d364b5c06344fc691f47bde",
    "f260d2fe4d8696d4c3929e7054cc8a5e"
]

LEGIT_PERM_IDS = [
    "b0f797c599120525f5d20ba943be473e",
    "8ea44095a8abf50553f82ad90a533574"
]

NEEDLES = [
    {
        "id": "1kefYhzknKEiFfEyIKzqSAqQf4HeOzuRY3dVSCx1IWZ8",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "267c7c9ad5685d20102eb5f3e188fffc",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1nBlL3P5CV7X8mSi4TTtkNRkV67jyGicsMhC3Iuuo7VT",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "02275dba5d364b5c06344fc691f47bde",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LkSgLcUArPvCKxWpVhuLQg4M9ywvr7JpQL7YpLGPGkn",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "f260d2fe4d8696d4c3929e7054cc8a5e",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1yrM0LRZ59WLFRNor1zQGxOohWJ5n4YrIZIiZEuPL41Q",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1816SY0MUcRzbOl9KrovoiJjPRivD1frwVhxIvdezi6A",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1MD6zSTZvTNLyEuLpapwL00yhnPYkafwBXDAfO5PPU6W",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b0f797c599120525f5d20ba943be473e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1mUutwFdsvND2oJjtvmGpasmz4wXPBiw5KtXoknYMmHt",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "8ea44095a8abf50553f82ad90a533574",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
