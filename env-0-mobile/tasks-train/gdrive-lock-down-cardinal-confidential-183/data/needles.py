"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1rw2U4V4cXds8FtrGP8OJL71YE3jvtwbPdSoJegnm9vh",
    "1nOatUSRwKVDqFjmTKDTOalEkzl4HJ6TP2LgszHsEGJ5",
    "1NIQEO1tjHJJt064KQgZYhpk5kOXzJrGMr3kjegITDkh",
    "1BDcY7IkiPkL5yxoJJjo82694wxrzBLutUUcnTYm3SUE"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "0cb86ef9125ffb869472580921daad59",
    "ddf898c6602f113e2422244bac25a4df",
    "a4f9eba9321288f5da28af00a4f98068",
    "1fdb78d8bc7fd7b418da7a9db7fb9de7"
]

LEGIT_PERM_IDS = [
    "fc720511b0652a20f8ead6aa98c2c6d8",
    "c2d9d23d9af55d105fa4ab6993148593",
    "d84672e54a12c553910f522b01a14f57"
]

NEEDLES = [
    {
        "id": "1rw2U4V4cXds8FtrGP8OJL71YE3jvtwbPdSoJegnm9vh",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "0cb86ef9125ffb869472580921daad59",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1nOatUSRwKVDqFjmTKDTOalEkzl4HJ6TP2LgszHsEGJ5",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ddf898c6602f113e2422244bac25a4df",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1NIQEO1tjHJJt064KQgZYhpk5kOXzJrGMr3kjegITDkh",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "a4f9eba9321288f5da28af00a4f98068",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1BDcY7IkiPkL5yxoJJjo82694wxrzBLutUUcnTYm3SUE",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "1fdb78d8bc7fd7b418da7a9db7fb9de7",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "165OLWmKN4xzNS91kg6I7vFTt0amakqlPd3ptF2V4imy",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1UT1AWQBIvR4fHOsgsw5F8P5uF7Cf6LJJRVvnLlGhlAB",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "fc720511b0652a20f8ead6aa98c2c6d8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1zef3zlluxMUyCmhlLLwFvIDEvbLVPPzeJUjMIUl6xqi",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c2d9d23d9af55d105fa4ab6993148593",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1VBgov4qgZM9Amke1n3p1mzSi2DWNPgV1v4uBQqYQgGZ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d84672e54a12c553910f522b01a14f57",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1xfdQSxRujn6FLuk9rC1wrqOzucECLlkg2d2RW5teeBb",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
