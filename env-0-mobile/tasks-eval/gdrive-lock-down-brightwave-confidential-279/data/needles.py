"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1k4jUO2XvOQ8f38sHRSSpOmy2joj1i6gQVL1PchMpp2c",
    "1oMDtF4UJUskq0lYDpaf5mFZBAOXfAUPNRLqSIryWqs2",
    "1eakAkZnufJZdRMyTzTvkqvSnfNhSm3KKhAm7Zz0I3Ns",
    "1HvpP7H4FkU6tYPZBBDQebqLfe9Mz5bj6HQ8IACTODhi",
    "1FzWnnlshr2odZsLuZbJsEYNujS5e7G0n4y1NBEoJy6U"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "866fb23bf7cf569f3b5eeae5c40774b9",
    "cf0705a90dcb59f9ef3c7aafeb6a6736",
    "4c6a0198bb3d122c45763c224a146091",
    "ffd5e6e65783cbc523e0d24ecd093375",
    "c23736edecac7adc02ec9ac4b33abf9b"
]

LEGIT_PERM_IDS = [
    "2ef10d4ca9e8fdc012f990a344170057",
    "d69902d9e5da48e52f305d3f1a37b515",
    "e84ce1a6b1281d30a33df7320d426e52"
]

NEEDLES = [
    {
        "id": "1k4jUO2XvOQ8f38sHRSSpOmy2joj1i6gQVL1PchMpp2c",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "866fb23bf7cf569f3b5eeae5c40774b9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1oMDtF4UJUskq0lYDpaf5mFZBAOXfAUPNRLqSIryWqs2",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "cf0705a90dcb59f9ef3c7aafeb6a6736",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1eakAkZnufJZdRMyTzTvkqvSnfNhSm3KKhAm7Zz0I3Ns",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "4c6a0198bb3d122c45763c224a146091",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1HvpP7H4FkU6tYPZBBDQebqLfe9Mz5bj6HQ8IACTODhi",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "ffd5e6e65783cbc523e0d24ecd093375",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FzWnnlshr2odZsLuZbJsEYNujS5e7G0n4y1NBEoJy6U",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c23736edecac7adc02ec9ac4b33abf9b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1IvVedLK3pmljBqlDwHpGq8bas7gIpueBlPkFl3g7kI2",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "14qRJPdFxq3Nkd8NzDIdzEIMUvC64H6reN1mEukEshov",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1ZrSPD1msAAFYgQhv23IAW6To4znawSXCxcKhootpPhE",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "2ef10d4ca9e8fdc012f990a344170057",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1d87x3wg2dNLgIEE5z6kLSfsz1e7X2FsB7Yo1LiNeNgT",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d69902d9e5da48e52f305d3f1a37b515",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1g4vyFFyXUOfXvv403jKxVHNEy1airbGeNpglWYfCtTI",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e84ce1a6b1281d30a33df7320d426e52",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1mNBqMgbX8JLGUXgWCznL2zM90O5tve754pGzO4n5sC3",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
