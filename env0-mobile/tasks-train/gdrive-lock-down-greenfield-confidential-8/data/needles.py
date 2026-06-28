"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "15Uxbs43ER0LHSEMmxdWSTwNI4LRuBLw4Rv0ig3Dhv5u",
    "1NWVUDw69KAblrQkOoiRjYeKBHrt1WpwqbJR8KlwkIIn",
    "1sRGfQfDIO7BxMpLIScXpOH2iwujhcdZ7HAsJ1QE9Oka",
    "1Fr0ZVfHTo82FxB0m4YSItNLY4oNKeEWsCfQY5KzwQfJ"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "926c743bde1a5d5281866f666ef5e88f",
    "9bad0ca92be2522b311e09d251390d7c",
    "4dc01b5b6a21d87aa092a87e68f33199",
    "b4b1cbd59c371ac97c88c04ff432c089"
]

LEGIT_PERM_IDS = [
    "a6c4ae12375982012f6dac757a5f31db",
    "5c8ee6309bf84f9ea86f6601a72c15dc",
    "bef9283700facae966c95eb53db6fb6f"
]

NEEDLES = [
    {
        "id": "15Uxbs43ER0LHSEMmxdWSTwNI4LRuBLw4Rv0ig3Dhv5u",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "926c743bde1a5d5281866f666ef5e88f",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1NWVUDw69KAblrQkOoiRjYeKBHrt1WpwqbJR8KlwkIIn",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "9bad0ca92be2522b311e09d251390d7c",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1sRGfQfDIO7BxMpLIScXpOH2iwujhcdZ7HAsJ1QE9Oka",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "4dc01b5b6a21d87aa092a87e68f33199",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Fr0ZVfHTo82FxB0m4YSItNLY4oNKeEWsCfQY5KzwQfJ",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "b4b1cbd59c371ac97c88c04ff432c089",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1yJsTVsMERiI9qPkJ7cz0FLljBz2DhhdsIrsQrL3BAfi",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1j7Sj4oCrO71F3hOnGqO4PAwmZP0AnKqdl98XBRGdINw",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1BmBBhKbwabIS7jVnMUFy7ZEgYYXMn5X57BWVJZ2CUX8",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a6c4ae12375982012f6dac757a5f31db",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1GNOkKEF1yM0oNOrPEJW50vyWsudWeGkdbPP5U6qQGm2",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "5c8ee6309bf84f9ea86f6601a72c15dc",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1bMf1pY9pyHxEdr70FdvXImWmzkJzpvorn1pWaQE9zqR",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "bef9283700facae966c95eb53db6fb6f",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1eUynWtWXrpgcTLR3WZkip1bElQPeKpgBTypVmN4Uubq",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
