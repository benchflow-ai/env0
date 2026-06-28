"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1SEr6N8SqrffqDKX6dX8BfiZoae1Uuk1CkCwPvyXeT1f",
    "1Mi8HGavcko4Zzd3Ie8QfZPva7Ylm3UW1it538s4yVrw",
    "1giavJLCAlgMWe4QFLG1ddbfuJR7kUUdqN2CayppCDAM",
    "1vYkuTQvCYA3aXR7yGj1Z7FEoN8bA7b5dlSMlIC8BTgq"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "5eadfb08954750e2d7ce2f9d3b92ccd4",
    "901c913a0e9512bc562d449b4a184b28",
    "12358b5438f4b10534308b8b3ab1e057",
    "5e47f946dfd539de2644012c06653e83"
]

LEGIT_PERM_IDS = [
    "992477eaaedd3e7b658738c981d08bff",
    "d4a45bbe55cc881455064f2f3d95cb61"
]

NEEDLES = [
    {
        "id": "1SEr6N8SqrffqDKX6dX8BfiZoae1Uuk1CkCwPvyXeT1f",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "5eadfb08954750e2d7ce2f9d3b92ccd4",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Mi8HGavcko4Zzd3Ie8QfZPva7Ylm3UW1it538s4yVrw",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "901c913a0e9512bc562d449b4a184b28",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1giavJLCAlgMWe4QFLG1ddbfuJR7kUUdqN2CayppCDAM",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "12358b5438f4b10534308b8b3ab1e057",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vYkuTQvCYA3aXR7yGj1Z7FEoN8bA7b5dlSMlIC8BTgq",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "5e47f946dfd539de2644012c06653e83",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1BL9fyxHhgCQBFKdZTtimM9oijqtEmzIFvxH4AKmorgt",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "992477eaaedd3e7b658738c981d08bff",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "149hrF9H20Mu76sShd82NUjjwibvECH6BvB5zBJh9Cco",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "12O8WvaIWmUp1xUZQOuZcaSesHfQyjkxG6xqixtBpQ23",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "d4a45bbe55cc881455064f2f3d95cb61",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ROk2rHcBPybc3Olr3NcTt8rYZnFSxjiJfxLTRhfPgeg",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1DK2W40ZbN2Kil66wZfkHfAGpvOQutB86fUqoteWkxXR",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
