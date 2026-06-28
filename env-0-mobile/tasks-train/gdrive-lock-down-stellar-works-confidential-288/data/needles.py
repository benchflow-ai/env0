"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1GzHQ3advOp7dPsW8ZW2GAbA0MCLk9h9RvZjdMvWbaDz",
    "1qGVMVd0yyxzLfqBtJ74NneRnje4dYslbXnOEc7BqAE7",
    "1KCpjVpT1ekyvHkGx5PYQvQpkkj2kV9jDXowReVBNX3V",
    "1f3VogSEluss6LFzL2EspOVKqmUeLWTXFuBUYmaLmfew"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "07994ffec058d02edfe7a5026acd539d",
    "1ba055cbae1fdc7972247b138d0a7e7a",
    "4c87dc2c15e7665bc49f9209c065d426",
    "47766e2dca4a6f36957c8d3a091969f6"
]

LEGIT_PERM_IDS = [
    "71ee8d68556d57a7e3858f1cfbd3a26f",
    "274ae5eceb09b1422004f20b9218be1d"
]

NEEDLES = [
    {
        "id": "1GzHQ3advOp7dPsW8ZW2GAbA0MCLk9h9RvZjdMvWbaDz",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "07994ffec058d02edfe7a5026acd539d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1qGVMVd0yyxzLfqBtJ74NneRnje4dYslbXnOEc7BqAE7",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "1ba055cbae1fdc7972247b138d0a7e7a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1KCpjVpT1ekyvHkGx5PYQvQpkkj2kV9jDXowReVBNX3V",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "4c87dc2c15e7665bc49f9209c065d426",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1f3VogSEluss6LFzL2EspOVKqmUeLWTXFuBUYmaLmfew",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "47766e2dca4a6f36957c8d3a091969f6",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1VGzIHzNQGzvcXTtRG71lT108gtAMs2L5xoe5cehIOZP",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "71ee8d68556d57a7e3858f1cfbd3a26f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "17F8z9K56GGSivW6dktAJfzLtnEtttg9CX2655s2BAux",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "19UX0TtIZA9d53Jxe3W7bCdOPwmn4ToVx3gY0JFz6hjQ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "274ae5eceb09b1422004f20b9218be1d",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "15NIcxfT72GnCLfx6EGwEQgYhUtAH4wQSynX9pbg93YF",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
