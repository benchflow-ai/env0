"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1bokkTf1otsO40JhEQg74srCAUYiD3KcyIBRQzLdkoYE",
    "10L9MEvNcpEQJsahMbTn1p7zOgDCrMy3LiXhHXzPs3mp",
    "1oAXyPx89tMyuPNmlIDF8enCcVeIh0bycr7d1mc25Pjr"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "8696947b71cbabe516f8ab93e9d4a231",
    "4cc08bd48867e3bd0153cf065a035f92",
    "1f8fa752bf72e0c1ddd8e6a9886a9b3b"
]

LEGIT_PERM_IDS = [
    "346e365f86e0bc9deb0a0ed061c63b0e"
]

NEEDLES = [
    {
        "id": "1bokkTf1otsO40JhEQg74srCAUYiD3KcyIBRQzLdkoYE",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "8696947b71cbabe516f8ab93e9d4a231",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "10L9MEvNcpEQJsahMbTn1p7zOgDCrMy3LiXhHXzPs3mp",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "4cc08bd48867e3bd0153cf065a035f92",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1oAXyPx89tMyuPNmlIDF8enCcVeIh0bycr7d1mc25Pjr",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "1f8fa752bf72e0c1ddd8e6a9886a9b3b",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1mLurZJ4lhnbEPe9ocWx2QjmRa1mFm1lk1HPgr6rjrMD",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1UpokHPQIcajjn8VcBvLTNsPewp0AJxrECXYN8fvq3Qf",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1ndl4XV1SE0qQBf5XQagvOyjiZ37X1MV2bjY95PZmlxZ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "346e365f86e0bc9deb0a0ed061c63b0e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "153LH4tZHLYjYva6eN1X2VFJxf9x7mIku2G8YcwSsdPn",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
