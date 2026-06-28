"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1qmnCn4iYV3WUbyavj6QNHH8RAQr8gZGFn5i8GoLzF4M",
    "1WqFxHFdj8n2yxy8qIJn6dZNmPAgiOPMmTeM5XzXPdFH",
    "1SufFDHqkj9ECNyDe2lxGWYqhuI9E22tLfLhmSpnHt6z",
    "1Oy6xX93hzDQVaBsDiGy4bUWMv7Xbr00v5mee2FLAWPU"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "0eeda4e15f57fd286c59646a77b8240d",
    "0703f5f5dec194ea96fc56fc48e448ad",
    "73b0b10b29aebebfe5cdf58e9a5ae25a",
    "8160523dd8c92299927519b271c0d076"
]

LEGIT_PERM_IDS = [
    "ad4093e01261cdb7f1bf5c9a0f29a7fb",
    "84c6ff96d3ae50c86c25823744359178",
    "6dce95a9c50fc526d6f875ff4db3223e"
]

NEEDLES = [
    {
        "id": "1qmnCn4iYV3WUbyavj6QNHH8RAQr8gZGFn5i8GoLzF4M",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "0eeda4e15f57fd286c59646a77b8240d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1WqFxHFdj8n2yxy8qIJn6dZNmPAgiOPMmTeM5XzXPdFH",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "0703f5f5dec194ea96fc56fc48e448ad",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1SufFDHqkj9ECNyDe2lxGWYqhuI9E22tLfLhmSpnHt6z",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "73b0b10b29aebebfe5cdf58e9a5ae25a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Oy6xX93hzDQVaBsDiGy4bUWMv7Xbr00v5mee2FLAWPU",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "8160523dd8c92299927519b271c0d076",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "18jufh49pQnoDTJdb0XuN4Jljn6fNNWE2XVvUeSRUu5Q",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1XfyGvVsHABjzZmu3KNW4XmFVzw5JcO3TIzFDlLKXtEL",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1V7s73j5VOBYY2lwD985BGFXuFLH5tXLPE268sKkFvGo",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "ad4093e01261cdb7f1bf5c9a0f29a7fb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1OTrKsxNbCb8bonyc0ka9GFoagbkAKZZA0coI3fkqNXy",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "84c6ff96d3ae50c86c25823744359178",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "11aRVBTEzKmX64DtszhXGGFNf4wwdaVLZKJM1AAaoUl2",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1zBsH1mmOR5csMFunihUUDlYClXoojfH9JwdnMmjpUr4",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6dce95a9c50fc526d6f875ff4db3223e",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
