"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "10ykpLdQEkV9haqvF61FfbApnhItl3Kswb2b81mFMKJP",
    "1fediKaVyWlGyNblzrXwYDvT9qgW5Mm9yWCIBDDOgurH",
    "172lt30WXs7PKckl5oKkwPwWHFCc0KuefSiQVRsOEgK9",
    "1Lc7BxOcPULdITVvZi11RwVGKXBGRmrhcxVOyohhnmgU"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "3e41d4b080e98f48d0987f122ca96e7b",
    "888e2d36d22f8b19a1c2a0b311bf5120",
    "0da00d3a7f43748d410831d1ba5c2ebb",
    "8e7a1a68a927b35ba74f8b74babed55f"
]

LEGIT_PERM_IDS = [
    "19d9c8a85e4efd67e25553f6ac726435",
    "be36bf4ae39658781443845c398a8908"
]

NEEDLES = [
    {
        "id": "10ykpLdQEkV9haqvF61FfbApnhItl3Kswb2b81mFMKJP",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "3e41d4b080e98f48d0987f122ca96e7b",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1fediKaVyWlGyNblzrXwYDvT9qgW5Mm9yWCIBDDOgurH",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "888e2d36d22f8b19a1c2a0b311bf5120",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "172lt30WXs7PKckl5oKkwPwWHFCc0KuefSiQVRsOEgK9",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "0da00d3a7f43748d410831d1ba5c2ebb",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Lc7BxOcPULdITVvZi11RwVGKXBGRmrhcxVOyohhnmgU",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "8e7a1a68a927b35ba74f8b74babed55f",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1rDleHbW4I9Kobo9GFnnkP7TcnprDw851o7qFS3hULeE",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "19d9c8a85e4efd67e25553f6ac726435",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "16frv7AWorT7nnmlyoj63EVmA9YjuQoSaRboKzWdLIBG",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1Authzg2CmSs08HIEZg1A002kibnYrhfkrQTaL9QFUb0",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1xXAQizuNfKTHjheyjptBMRKTP2mm5awRnIVQmlg18du",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "be36bf4ae39658781443845c398a8908",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1OEmCYn4tPveelSBPgHJcBaqZxxHU498SU1aRO26xlP9",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
