"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "19j3OsIAd1QPGqMiBffymeU96cz29BkmjKAp10VrbBIG",
    "1jqdedmgOYZoykD6hGVVKM1GSU0RLt2m4v24YQisyayG",
    "1YKjXurKfUv1IEjBaO0EyZxQuxJIRt2Hg8W10WIc6O6q",
    "1Ov4rHiQdlyH5Esc8qR7bEaA9xIVFA3d3sJLsgOyJkAQ",
    "1hSd2DdRIO0n0x5oKHCLAjyqRBcEhBmojUKYfofzWVQc"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "66b982887b62f0adb5ed723c19f40aa4",
    "f9fa0880c81461fdf0f8c70005f13e48",
    "dc8292d211496364a806e98d23cab20d",
    "2398ca0b0a066beb927260b9e2c93a0b",
    "0cd9900c64e55378a2fb6116dd1e0a27"
]

LEGIT_PERM_IDS = [
    "3c146558a007d9e24ea15b10d2103f71",
    "9b6c467e9ec120b383a34c778a76fe08",
    "acec4cedf2ef886ca3f7676a8ee6c249"
]

NEEDLES = [
    {
        "id": "19j3OsIAd1QPGqMiBffymeU96cz29BkmjKAp10VrbBIG",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "66b982887b62f0adb5ed723c19f40aa4",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1jqdedmgOYZoykD6hGVVKM1GSU0RLt2m4v24YQisyayG",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "f9fa0880c81461fdf0f8c70005f13e48",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1YKjXurKfUv1IEjBaO0EyZxQuxJIRt2Hg8W10WIc6O6q",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "dc8292d211496364a806e98d23cab20d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Ov4rHiQdlyH5Esc8qR7bEaA9xIVFA3d3sJLsgOyJkAQ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "2398ca0b0a066beb927260b9e2c93a0b",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1hSd2DdRIO0n0x5oKHCLAjyqRBcEhBmojUKYfofzWVQc",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "0cd9900c64e55378a2fb6116dd1e0a27",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1VdufszNayY68mzP3zqJ7dPc8PiHhdDlt4zxxwnLhvZ3",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1BW008rGRZOXM0MnthyUKeYNBkI7yUUkhDHGeQal38io",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "3c146558a007d9e24ea15b10d2103f71",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1XZ9kWPixvOyIigh5qLoZYDsU19UAmbvfa9jckuuyXHU",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1hklmOuxtdusmbMmIcgDFFnwucwbDvv7OFOYLsGasb2O",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9b6c467e9ec120b383a34c778a76fe08",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "12ep9COFY4djCGY7s68Dj2CQcKycQvfkEekrxjeQM6YY",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "acec4cedf2ef886ca3f7676a8ee6c249",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
