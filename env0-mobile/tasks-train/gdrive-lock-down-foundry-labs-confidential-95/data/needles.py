"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1jzWj9By8RNyUHkuUYQedeio6iAkZRSnNBbJIPGlxuUQ",
    "1xg015gzRbpsXaRv564L43RAuieKxteRHIeNvlkx858g",
    "1shg6eyyAv04FNDoE0gXCHHrsFVnPYujn9bwnz9YKFeK",
    "1pO7TUjvDYdyqmxLHKsOpfBVQslM5l1k7shiKWf6wwvi"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "1a2f96a8956e64707062ed0edb3dc3f6",
    "ec2aeaa14b81c917fc4e18c74263cfc8",
    "112b053d5318fa8a4fe7b790b788e1b9",
    "8590796a241454049e34334049608a37"
]

LEGIT_PERM_IDS = [
    "b5d78302f58531ce0bc3b697a813ba94",
    "e066f580b7ea38809932d791baa12c79",
    "26bbb72a6c111ab4deebdecdd200a5e7"
]

NEEDLES = [
    {
        "id": "1jzWj9By8RNyUHkuUYQedeio6iAkZRSnNBbJIPGlxuUQ",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "1a2f96a8956e64707062ed0edb3dc3f6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xg015gzRbpsXaRv564L43RAuieKxteRHIeNvlkx858g",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "ec2aeaa14b81c917fc4e18c74263cfc8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1shg6eyyAv04FNDoE0gXCHHrsFVnPYujn9bwnz9YKFeK",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "112b053d5318fa8a4fe7b790b788e1b9",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1pO7TUjvDYdyqmxLHKsOpfBVQslM5l1k7shiKWf6wwvi",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "8590796a241454049e34334049608a37",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1rJ6JzZJUCfOdogn5ameTKnZd2P10VqTRrcYxWJH8Bgj",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1cI5qVD6dPbbL3MpsvdBouBwT7WOEF0sMamZCrvOBYsS",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1e0x0605NUDv2EoxFrZW4ypm7gsh2lsVSa4IPPhNe7zT",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "b5d78302f58531ce0bc3b697a813ba94",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1um419ZYoxL70BDP1OvsgIPTeZsJP97E2sbMLpguB9pF",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e066f580b7ea38809932d791baa12c79",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1q1sulhHDBWQ83prqxhhK6NiCdyi2q33YLWIqUlfxQFe",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "26bbb72a6c111ab4deebdecdd200a5e7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "12uN3koXfVcUQhMUpJcxELEOdhV6uxEKpT4hShKgA9ya",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
