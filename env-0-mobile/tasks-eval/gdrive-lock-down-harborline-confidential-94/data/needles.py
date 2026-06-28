"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "12aMh9HmkzxfGbvcpy09qbVSUgPMmXB7n58maxgYUp0m",
    "1Mjpt6yULDVI9l6sV0Zsyf2lV3sk4VDURPYnQi2IImQp",
    "1Rfy2wgDjantUhAlNvpuWVXfumev004WCmMzdu26LiUv",
    "17ViBTTU47uFZNpVKwmfG1GpAQq97269Q8Uuq0hVhJq2"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "35036f1b5d5aacb2d72b994c4833122c",
    "a2a0399723cf067a983f5ccaf1b8b090",
    "2db94a23334f4a41c4037ded9e861d6f",
    "11d8df5a08f8c4a83b436b5d2c4a744a"
]

LEGIT_PERM_IDS = [
    "952a7551f1842666606f2cf70ddd39d1",
    "04a185842c68fe49bc22e0b3ddcab96b"
]

NEEDLES = [
    {
        "id": "12aMh9HmkzxfGbvcpy09qbVSUgPMmXB7n58maxgYUp0m",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "35036f1b5d5aacb2d72b994c4833122c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Mjpt6yULDVI9l6sV0Zsyf2lV3sk4VDURPYnQi2IImQp",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a2a0399723cf067a983f5ccaf1b8b090",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Rfy2wgDjantUhAlNvpuWVXfumev004WCmMzdu26LiUv",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "2db94a23334f4a41c4037ded9e861d6f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "17ViBTTU47uFZNpVKwmfG1GpAQq97269Q8Uuq0hVhJq2",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "11d8df5a08f8c4a83b436b5d2c4a744a",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1F07eMWrYVlhTF17b3WjjkEYzXmaIyXX5A3XES0MnJwL",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "185UuaGrD6simaN32avKopYKBsHgRcUAwHRQ4NutOrXy",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "952a7551f1842666606f2cf70ddd39d1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1mxvzyVncrvsqrFwWTmge3WoyMErZPkyojEpLzyboaFK",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1YfHF0gyweOH1ku8gIoizlxvdc7RfZMRf2EK7NHYf1m7",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "04a185842c68fe49bc22e0b3ddcab96b",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1EnPaXDnFzRnhc3DVxqYcZZsVGxwBKcZSZKjHWnK5ZxI",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
