"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1V0IFllDrchplytljLhHQFhiKlstEFsBEHqyMuckgolZ",
    "1CU4VAR9CfHYbQwK0MqCd8aSe8UQ5n8WBHhpbEeq80tm",
    "16Vllgrb0ioUKbANjmkoOTnNiP1NBPQvQvRe5pXP7gBh",
    "1lCVzZENOFE8zLB1uL1aAZX0BYPEpbNPhX2SSLivlVUq"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "c47ceeee9acd95d74a9ee183f786de14",
    "bde99713ec694dc32db95c4be2b3f90b",
    "ba3e88348743d06c35d7466b6ee31248",
    "9bcdc677817cb4f6134479ba0a02bd2a"
]

LEGIT_PERM_IDS = [
    "e0a8a776512160514655037ce46d5b8f",
    "e10495aa8f0ec449ae2339ecc1eb8f10"
]

NEEDLES = [
    {
        "id": "1V0IFllDrchplytljLhHQFhiKlstEFsBEHqyMuckgolZ",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c47ceeee9acd95d74a9ee183f786de14",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1CU4VAR9CfHYbQwK0MqCd8aSe8UQ5n8WBHhpbEeq80tm",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "bde99713ec694dc32db95c4be2b3f90b",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "16Vllgrb0ioUKbANjmkoOTnNiP1NBPQvQvRe5pXP7gBh",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ba3e88348743d06c35d7466b6ee31248",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1lCVzZENOFE8zLB1uL1aAZX0BYPEpbNPhX2SSLivlVUq",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "9bcdc677817cb4f6134479ba0a02bd2a",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1MsgPxxprkVH4D8G6RQ3Qa8oM2PKndgLI9Ipg0puqCEq",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1bIfCir3QkP2fWN0vlwBxsszgXmqdeb9bSUo3waG89zc",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e0a8a776512160514655037ce46d5b8f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1xnCtPlJPkGy1JwypDn4WIBAjeXD5mLWaOrFWPee7c2g",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e10495aa8f0ec449ae2339ecc1eb8f10",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "13FC7hSARWr3TYYDO7B3ixXiRw5GUsLOfX1qqZ2ROf29",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1pjSMoikCJOBw3EwWA7bPInDLuECHfafAn0QBnNIhRU6",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "177PRdBQydlbUfTX7k1OTHVnbjCe07BphneBsow3gJ0Q",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
