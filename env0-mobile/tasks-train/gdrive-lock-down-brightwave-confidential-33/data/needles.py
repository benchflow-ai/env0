"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "149GFVgyU0Tchui3VgDiiPErZ1wQftFYZVSagGFcoQJt",
    "1xgnymvxyanRteRSrRRVShDyeGmdCZun5n4PZuQltgWm",
    "1ouG6MPcmBRM6RGvK33PxKSYmWwRJw0XzNnbON4CILlU",
    "1GV907U0j69UIJa59bI2qoe9Zv6DsGUg7G4vsxkpfU1q"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "8c60d5ec7f4a19ea474f956b9e64f097",
    "600b66a64209c90f51ad4685d456fa40",
    "b03c58c2fbd70e08a6b7ea7a78ee4895",
    "cfb53d71529a6842f4fe8c7ba7e88f0e"
]

LEGIT_PERM_IDS = [
    "7b8b7aa52d89d3324b6dbd7d811c7457"
]

NEEDLES = [
    {
        "id": "149GFVgyU0Tchui3VgDiiPErZ1wQftFYZVSagGFcoQJt",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "8c60d5ec7f4a19ea474f956b9e64f097",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1xgnymvxyanRteRSrRRVShDyeGmdCZun5n4PZuQltgWm",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "600b66a64209c90f51ad4685d456fa40",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ouG6MPcmBRM6RGvK33PxKSYmWwRJw0XzNnbON4CILlU",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "b03c58c2fbd70e08a6b7ea7a78ee4895",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1GV907U0j69UIJa59bI2qoe9Zv6DsGUg7G4vsxkpfU1q",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "cfb53d71529a6842f4fe8c7ba7e88f0e",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1IjKu0KAV6KuUQ19Bm5neBZTA8yAjNrNWtuyUgnDNdAM",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7b8b7aa52d89d3324b6dbd7d811c7457",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1PfgpJKfjSBTrEmyLi8X3xKnNW6xCv7g62aOKXD69AUz",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1tvdFciOTVSVD5K65FL99gk1846GpYY6YeRyk91YKS0p",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "16qOkhiK2n5FzGsvyZF0nhuAZMRWz5D8kKAGlOpesdav",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
