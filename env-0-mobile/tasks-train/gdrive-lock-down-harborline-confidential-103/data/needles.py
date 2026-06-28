"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1k4j14EIUBOV2PBrt4i3L5ilDKg3sETb5Z2DSB21pFve",
    "1RvhUFbDJfcKnL6VLBC9JwQiFDx5kDEytSPlow8qZkGL",
    "1yz5kadGSGkRdDouMdgYWwjttagGeBlXmesZsXwGP59x",
    "1eA3QEhs7tzbIDP8bRrh5FskqCDqaNUKDdHdNVGUtJEK"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "6cb46b71189d6be4f092dc79347c348e",
    "531d5279eb4a82fe73144c83ccafe08d",
    "08c6ec19a6354fea3e676adbdc76f610",
    "def5348be4344786e3b00fe61705883b"
]

LEGIT_PERM_IDS = [
    "529baf99b98cc6516a416a0820d56bb2",
    "2b84003460c57d4fd21c972f15cfdf54"
]

NEEDLES = [
    {
        "id": "1k4j14EIUBOV2PBrt4i3L5ilDKg3sETb5Z2DSB21pFve",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "6cb46b71189d6be4f092dc79347c348e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1RvhUFbDJfcKnL6VLBC9JwQiFDx5kDEytSPlow8qZkGL",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "531d5279eb4a82fe73144c83ccafe08d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1yz5kadGSGkRdDouMdgYWwjttagGeBlXmesZsXwGP59x",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "08c6ec19a6354fea3e676adbdc76f610",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1eA3QEhs7tzbIDP8bRrh5FskqCDqaNUKDdHdNVGUtJEK",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "def5348be4344786e3b00fe61705883b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1XMqePVO0g4OYYUGGkryOQ6wFYm7lzp3EjuxNicAEn92",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1oDNaGcb561I4Y3YCofMKg9zU0omo46NG7YsQngHN1fq",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1a07MsnoyfRfWyZ53o6wBRpz91fZ36qtOwWXRgEEYNBX",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "529baf99b98cc6516a416a0820d56bb2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ZZlpG8ri4cn2iBFWASp3tnVzEEauNBPYeZjzy3cHWwi",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "2b84003460c57d4fd21c972f15cfdf54",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1lOOzHZxLFvvhv8eh2g3R5BwSUZeSh6pLd1OevEf2WUe",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "144OzpwelTWTVkhhnUUe3NDsGBpNQcZ0jBh7PZpM86IM",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
