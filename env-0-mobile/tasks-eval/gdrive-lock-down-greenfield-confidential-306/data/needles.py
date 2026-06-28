"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1BUoJ3NXxoOgQ6PJbWDrbIWxek0PWvlRb2tgdoSAW3wq",
    "1GnOqBuaBoujzCGSVTY9roX85h0ZkBT4iDhui6jOzgo2",
    "1JZM2Q7EwQMyBKBNRgSi9z80tx7yTGn1yjKR2BUeVgPl",
    "1hrWbX6NKDR0LdwPOF9no6qdHfwCuZxBSqp8bLWUU3op"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "c0a740c0a365973cf7421dbdcabdd8ed",
    "9956fd1b3664cc3f93557147bc4ed2db",
    "6ec85a8944d1059f2854bdd772b8f885",
    "d6f752853deca298eb9e5f9f75b36cbe"
]

LEGIT_PERM_IDS = [
    "62a7eaa1acec41e84c19aa8f7aed6e3a"
]

NEEDLES = [
    {
        "id": "1BUoJ3NXxoOgQ6PJbWDrbIWxek0PWvlRb2tgdoSAW3wq",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "c0a740c0a365973cf7421dbdcabdd8ed",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1GnOqBuaBoujzCGSVTY9roX85h0ZkBT4iDhui6jOzgo2",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "9956fd1b3664cc3f93557147bc4ed2db",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1JZM2Q7EwQMyBKBNRgSi9z80tx7yTGn1yjKR2BUeVgPl",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "6ec85a8944d1059f2854bdd772b8f885",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1hrWbX6NKDR0LdwPOF9no6qdHfwCuZxBSqp8bLWUU3op",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "d6f752853deca298eb9e5f9f75b36cbe",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1EHZi3qcd6B3Jb3exmemzaOcbrTxogBFm2hhLxStWjLF",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1dFjFrbMYhAXVDMJXDTXBNmqZ9c5CQBnJI8R2CSXRHWE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1zVOBY4dPB3O9KwJ9nHscUHVynL0vqlGnCBhWqqsY7h7",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1HbOf5SOCkXBplrF9W9asMsDhT6cNSwUJ5lIYQkR376X",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "62a7eaa1acec41e84c19aa8f7aed6e3a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1aGrkDTaV7zysDQZDbwxYEkl9AOjKBzvKZkt11pahtZk",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
