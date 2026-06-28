"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1PoQKUt8CWj0MvOUN5LVPaz2CMoQpoyypdYu1k2kWrD7",
    "1wlga0jtl9CB3p6EpOqxq7RwxQmXm4vSa7tgzgBcPiAC",
    "1jZwjwSwZJaRYNcmQwkpfH5UJAZ0ps2OGQgU9fXATAdW",
    "1Yrh0ckBhSb6T77xPI5pc112Zv1e8wI5n1zCUkU4YqJT",
    "1kPkTyh4yMSv3TTBkzEHNwYrO2cqe51DRQ2rpwUFr50v"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "021595dbb5cf09f8c226cc856470ae84",
    "820f1a64b234b84698e72ff05ca4016a",
    "0b24cc9d785fc3fcb3b74ddedae4ca1f",
    "0d8b67b06c3941a1d17da71993aece59",
    "d997dd2b9f5a46914c4d8e533cef00c6"
]

LEGIT_PERM_IDS = [
    "08f7e0f7d5b811aad2e07e1bf0fd3d8c",
    "9aca90eb848feeda70be80f654c8a375"
]

NEEDLES = [
    {
        "id": "1PoQKUt8CWj0MvOUN5LVPaz2CMoQpoyypdYu1k2kWrD7",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "021595dbb5cf09f8c226cc856470ae84",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1wlga0jtl9CB3p6EpOqxq7RwxQmXm4vSa7tgzgBcPiAC",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "820f1a64b234b84698e72ff05ca4016a",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1jZwjwSwZJaRYNcmQwkpfH5UJAZ0ps2OGQgU9fXATAdW",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "0b24cc9d785fc3fcb3b74ddedae4ca1f",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1Yrh0ckBhSb6T77xPI5pc112Zv1e8wI5n1zCUkU4YqJT",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "0d8b67b06c3941a1d17da71993aece59",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1kPkTyh4yMSv3TTBkzEHNwYrO2cqe51DRQ2rpwUFr50v",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d997dd2b9f5a46914c4d8e533cef00c6",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1SmSdG9CMtKwWJmPEVNRp2Lfd3Er6CzHFr4wDNIDYksX",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "08f7e0f7d5b811aad2e07e1bf0fd3d8c",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1GvnqgpvOzYtXJwccIEI1EiPema0ZhYgosXRbxvbGza2",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1oRjGrgbZ8j8whZCiCZrtWuFQWTXw4l9yJnwhHtKtc6e",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1zM3ioqwC2V2tZOykMvDub4hnqXaW4kqqOZajA7P6bnD",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "9aca90eb848feeda70be80f654c8a375",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
