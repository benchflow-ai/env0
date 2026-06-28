"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1j8kkXoeuP6TS7LZyNs72dPxsUk368kpG9NY6BFxiqRJ",
    "1GVBGDEDk7cvD8UQEimHmMl1HlQtRKIsw1sjFUmju2xD",
    "1rJOVWrnAOa9JACOGRpsVZmsSMY9MIc6W9DZsIcTBcik",
    "1JBKBt0tdoovkM68nfhVvA4KhvQgCVEOqPzbMoWRPzOG"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "ce662ebeec22bb597663e029a47b9be3",
    "42d5742669f69b3811f510fafbd2c236",
    "b56ac14251b976ae83569525279edb41",
    "e493994c339307a00f58c258a2000c1c"
]

LEGIT_PERM_IDS = [
    "aac0ea9d988b7ad903e34eb5b91a8ffe",
    "cf3cf1d1740cea50186f61a705d399ed"
]

NEEDLES = [
    {
        "id": "1j8kkXoeuP6TS7LZyNs72dPxsUk368kpG9NY6BFxiqRJ",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "ce662ebeec22bb597663e029a47b9be3",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1GVBGDEDk7cvD8UQEimHmMl1HlQtRKIsw1sjFUmju2xD",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "42d5742669f69b3811f510fafbd2c236",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1rJOVWrnAOa9JACOGRpsVZmsSMY9MIc6W9DZsIcTBcik",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "b56ac14251b976ae83569525279edb41",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1JBKBt0tdoovkM68nfhVvA4KhvQgCVEOqPzbMoWRPzOG",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "e493994c339307a00f58c258a2000c1c",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ZJi4aUtP7WzN3tG8SCpQEuluewyQALAKDnPbXcCvvRO",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "aac0ea9d988b7ad903e34eb5b91a8ffe",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "105NWyQqcSKS2Yys1bJrXxKu6gWcEIuG8G0xP4EtZcpn",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1RoZmBcZdN8apITXI7NQ47Xs8yMP2iQEBZ80gzHP2OAA",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1GYokSPMb3pAfZ89UItZxaCMdxKlefPDPKhMACtondPE",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1tOJZBwWaxFPYeRRJPY9JJ78b7iOAIZv9z8xAnXWrDOP",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "cf3cf1d1740cea50186f61a705d399ed",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
