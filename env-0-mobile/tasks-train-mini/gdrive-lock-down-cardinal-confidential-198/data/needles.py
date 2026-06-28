"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1tmpvSc5dKE06k7uPCcUFBi7kybQefiMhQ7W7icuDDqN",
    "1XBxRluWHiuqxNLEUgSWpexBtO5zA6hOajSHigPz32bB",
    "1zvmdVyuL6cda5mMAATobBxL3pkoDHhFKnARhPmttais"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "d7d48585813b61b6af7c51195cb91876",
    "06e59542ed66f8a941ab2b099367eb43",
    "cf9efe3f3af8b1766e940f353158f018"
]

LEGIT_PERM_IDS = [
    "5fd4acfa0f8537618d6282df4b4a6760",
    "c573e19f2db7269a528e0cffc8a5f1fe",
    "af28bd713427b962e5dd677c05c4545f"
]

NEEDLES = [
    {
        "id": "1tmpvSc5dKE06k7uPCcUFBi7kybQefiMhQ7W7icuDDqN",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "d7d48585813b61b6af7c51195cb91876",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1XBxRluWHiuqxNLEUgSWpexBtO5zA6hOajSHigPz32bB",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "06e59542ed66f8a941ab2b099367eb43",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1zvmdVyuL6cda5mMAATobBxL3pkoDHhFKnARhPmttais",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "cf9efe3f3af8b1766e940f353158f018",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1l7OKrnxO36eUs6efzQ9cfiRqPcqBS5EexF7jM8JzdEc",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "5fd4acfa0f8537618d6282df4b4a6760",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1K4PoCViJ3TNofNgHPWMlzqmZQRNVY6kq5xVqA5G6Bmr",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c573e19f2db7269a528e0cffc8a5f1fe",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1CkCeEshamSH7xRzIECg62GfcAwtLUMoliLsS77omA5b",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1xZKuD7gEcsyeXAE4vFI1ib7LJfYueeUfpl4m0Ii8DCv",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "af28bd713427b962e5dd677c05c4545f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1DHI1EIIXxAtYAotnw7WVN9so5sGXqYrIyJCOyJQJS2Y",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1moQtSbC97JJfJK9sBiVhizfmXV4Wb2zQPIrNgfxl7Li",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
