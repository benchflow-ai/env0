"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "10Upf4C2QFB0QbmieUdCtwWl10eVUE3lD4SfDMStudpX",
    "1M6w8dJnasD9uiB2bH80giy2B3arWJDERVT1uU6HnoYZ",
    "18HALqLQymBQjdHXj2N5Gzu5rtlrjAjlz8H2nbRdgqF1",
    "1lMo5H0ZfM79e8iaVoTtn34mp8jakA8mu0Fi1cMBfavp",
    "1RmLEqfajvmxOePQz7AJ8nvwUgXxKQhm1DlaBtqXV5dZ"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "dc0cdad6e8c638bc06d12b8a1dbd358b",
    "5b2ddb99f5ab46ca1fab8399938e12e3",
    "f134084297bba89d4cac64e73c7a3285",
    "fa965d820ff461c249e338d46564b7b3",
    "b53cd5be197ee9b2b676f96a9d4da25f"
]

LEGIT_PERM_IDS = [
    "21c82816d9f5b3206d1b933c674c56ce",
    "096732b1ff53132de4ddd9a6b6d21a9e"
]

NEEDLES = [
    {
        "id": "10Upf4C2QFB0QbmieUdCtwWl10eVUE3lD4SfDMStudpX",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "dc0cdad6e8c638bc06d12b8a1dbd358b",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1M6w8dJnasD9uiB2bH80giy2B3arWJDERVT1uU6HnoYZ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "5b2ddb99f5ab46ca1fab8399938e12e3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "18HALqLQymBQjdHXj2N5Gzu5rtlrjAjlz8H2nbRdgqF1",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "f134084297bba89d4cac64e73c7a3285",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1lMo5H0ZfM79e8iaVoTtn34mp8jakA8mu0Fi1cMBfavp",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "fa965d820ff461c249e338d46564b7b3",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1RmLEqfajvmxOePQz7AJ8nvwUgXxKQhm1DlaBtqXV5dZ",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "b53cd5be197ee9b2b676f96a9d4da25f",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Y8uey0RdhbSUuUnixRxFPbSTInuEcrgeWwMCJrg4yxc",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1zxLdJkMcbb1Nt3uDIicv7aPz7IdLl7ULROBnOZBaJQo",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1R1vhLNqcaoLMRCQ4ugoZA63aXgzGHhDyAVjMTCX3YAY",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1kT7LhqzaImYfzpCu0qlCCYPLbKZtbO5JdroLJM3h9n9",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1ahhZT6JB4dNgbvTGzA76GMHZmmtYcvPFHlI7H9F8AR7",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "21c82816d9f5b3206d1b933c674c56ce",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1MPyLtVzGnAewzvR9OFJ64k0Pbhe8FeabSXYZko961fc",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "096732b1ff53132de4ddd9a6b6d21a9e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
