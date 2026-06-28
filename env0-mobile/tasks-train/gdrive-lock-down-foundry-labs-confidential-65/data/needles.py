"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1jKNMlawcDioOsaXJk21S5KvAWYGi6nXqdZmwRjW8698",
    "1ZZSafd5KAFTkwltkpeYzMJeZBIAucE6fDTYMnQxdZck",
    "1foCUJLuvWp0IO3G5zvr44j8Fi3l8caDo7rdpLQnMjVx",
    "1bzzfGMB7HJ01HMG237vqnpeeLXdHW10XTL4IfcLLnkl"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "1ad443c2c2cd0cb1583af0d6dc2d9a3e",
    "defda1598f62e4057e04868256e4caba",
    "c5c8fe9afe456089da7f94db680b9b32",
    "533e8572c17a6c83c328904ea03ed450"
]

LEGIT_PERM_IDS = [
    "69cf2191c4b1cf2fc8c9a82980d029c6",
    "09b6fc1abe31b6b5155bfcbecbcfc3b2"
]

NEEDLES = [
    {
        "id": "1jKNMlawcDioOsaXJk21S5KvAWYGi6nXqdZmwRjW8698",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1ad443c2c2cd0cb1583af0d6dc2d9a3e",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1ZZSafd5KAFTkwltkpeYzMJeZBIAucE6fDTYMnQxdZck",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "defda1598f62e4057e04868256e4caba",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1foCUJLuvWp0IO3G5zvr44j8Fi3l8caDo7rdpLQnMjVx",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c5c8fe9afe456089da7f94db680b9b32",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bzzfGMB7HJ01HMG237vqnpeeLXdHW10XTL4IfcLLnkl",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "533e8572c17a6c83c328904ea03ed450",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ANJF4Qkm0r6Ye0A2EInvmMXZNSRSgbJm1UGvtF3aSB7",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1E3NgWAevWkdOQyfgsFNe3Xac3ZYrK4BFIfs0ydpd7SA",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1pQyjxJzp9ySgAS5k6LA4mqg3piWzGf6bwbdBN1PUmEM",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "69cf2191c4b1cf2fc8c9a82980d029c6",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "10G20FCqVOwypatmy60OlkfcuvuwvwTecIuohW9kFiof",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "09b6fc1abe31b6b5155bfcbecbcfc3b2",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
