"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1Bz2fWqpgVvTDog8U3m8C1DXOz2Ehvb0ot7pEDcCXpNf",
    "1O6NVFqNrxeD9ZzJdC8c7zN5Nin3vdmxIZ8qyqNH174g",
    "1GMvv0fxGbbKPvKb7WQmNo5BzUXpFEsUsV7hOga8cc1i"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "06be23fabcd0ac8cde9f72f4bea1b9c2",
    "b309d0de38ae1d2aaca22e1d2f93aa7b",
    "44a8d761be05dac8375241a4dd85e59a"
]

LEGIT_PERM_IDS = [
    "61ca8503e50246bdb634d64aaa0328de",
    "b22435525587593fe46d8e7959809d63"
]

NEEDLES = [
    {
        "id": "1Bz2fWqpgVvTDog8U3m8C1DXOz2Ehvb0ot7pEDcCXpNf",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "06be23fabcd0ac8cde9f72f4bea1b9c2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1O6NVFqNrxeD9ZzJdC8c7zN5Nin3vdmxIZ8qyqNH174g",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "b309d0de38ae1d2aaca22e1d2f93aa7b",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1GMvv0fxGbbKPvKb7WQmNo5BzUXpFEsUsV7hOga8cc1i",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "44a8d761be05dac8375241a4dd85e59a",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1w25NpbXnVyu8qmxphmDnAhwYlwjod83HzUNcYB8s9f7",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "61ca8503e50246bdb634d64aaa0328de",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1fEGM7J15A2ufkK36kSlGTXlPxui8RlG70aAenSsf7fP",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1CsRAdc4LVj6qmfJtmBMVeLOMRWwdCGfVkKsE5smkTWg",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1xXQrKi08cF5vJNMJ7Q6Go6DPk3Ly42WoLlqWx7AsH15",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1XtmJuf1Ag3p79QI0f2MEb4ZoIl3QeHhmH8RGn60u9Ao",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b22435525587593fe46d8e7959809d63",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1lTY3KgrX0jxc5BlMQSNLaHqZqBtrBsqmUcts6Zlf0cx",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
