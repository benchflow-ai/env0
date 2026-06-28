"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1T4DIyAN4gIscqdmPf62SsT0Y1VYRcjj2kxtEc88rRNy",
    "1HePg259h3Lk1kJb2wmXXui0858fgCqGnD8eP9HHZbAr",
    "1uuWZLoU17Y8UyfjW8kfHsLRMYlKuNogu7pELDZBEJEx",
    "18Lzy7oovmE747jSdbdKWtWQZBf858Z4BNwccSjsYLbW"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "9ef7f748b46ffb921022ac599a5a569d",
    "2e364ab29a2288892634d048013ca4a9",
    "595f222b6fe8df4cbd50d0a76399bc4a",
    "b6e23794ac89f1e41453c26378e4a1bb"
]

LEGIT_PERM_IDS = [
    "aaba6a976987b244db39e1eeb05b5c4d",
    "0cf49b6d8944874cabecd2823c59b303",
    "c63202432ee304e305dc5b7b571ce1e6"
]

NEEDLES = [
    {
        "id": "1T4DIyAN4gIscqdmPf62SsT0Y1VYRcjj2kxtEc88rRNy",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "9ef7f748b46ffb921022ac599a5a569d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1HePg259h3Lk1kJb2wmXXui0858fgCqGnD8eP9HHZbAr",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "2e364ab29a2288892634d048013ca4a9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1uuWZLoU17Y8UyfjW8kfHsLRMYlKuNogu7pELDZBEJEx",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "595f222b6fe8df4cbd50d0a76399bc4a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "18Lzy7oovmE747jSdbdKWtWQZBf858Z4BNwccSjsYLbW",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "b6e23794ac89f1e41453c26378e4a1bb",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1B0W49oihhufvC8LJWa6KyxuAcnLXohFquZ3YSIWC7DY",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1FX4lgtM3GOAHTWtZi9OW0u87Qh8CKOOUUv8AAOoU4aY",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1Cq6sc7PhzW0ZFfJQsA1eiwzvNfkn5hEQKgJ7jT5Dnnl",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "aaba6a976987b244db39e1eeb05b5c4d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1jIjE9y5WpFOqzzhqoDzv4r7oikIhSbmYOZCdEfnU6ox",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0cf49b6d8944874cabecd2823c59b303",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1hkW0VnrZOPfHCQKtyveryin1V2LUNNP4UuTHOOxcnKV",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c63202432ee304e305dc5b7b571ce1e6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
