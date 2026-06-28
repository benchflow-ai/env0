"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1X00W0XkX6k3SUWWwcuLtSndPxmWI9AfPA5NztBRTnTD",
    "1xScZUmExHcJ4qn8agnZU9uKfztKPeluFSizYXySgLWd",
    "1xqVuSyzAzWDHPG4UVyhwP1KLgWqHGwp6atd7FxqWW1A",
    "1H4IK4zDGuIJ5pyXknNs0Kq7ivG78XejaHbJNguciWK5",
    "15WN72WErfdRAgGwkVEEPuyAzIFHSywHS1OW4TtHOtjl"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "f9309b72e3de429340be9821fcff1e89",
    "62b0d7cfb4240e4e8f551fea65687482",
    "df3f65cdb066d7500aa6df680a6ae9e2",
    "aef21e05d64187a8c6392f663b220e31",
    "e5691d7350c108e31c077d423cb2eedf"
]

LEGIT_PERM_IDS = [
    "d794d2e4742b9296be30f80cca929ebe",
    "24d00609320f5e94fb50d1eececd42ab",
    "a4ff335b113791e732922a271897871a"
]

NEEDLES = [
    {
        "id": "1X00W0XkX6k3SUWWwcuLtSndPxmWI9AfPA5NztBRTnTD",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "f9309b72e3de429340be9821fcff1e89",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xScZUmExHcJ4qn8agnZU9uKfztKPeluFSizYXySgLWd",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "62b0d7cfb4240e4e8f551fea65687482",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xqVuSyzAzWDHPG4UVyhwP1KLgWqHGwp6atd7FxqWW1A",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "df3f65cdb066d7500aa6df680a6ae9e2",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1H4IK4zDGuIJ5pyXknNs0Kq7ivG78XejaHbJNguciWK5",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "aef21e05d64187a8c6392f663b220e31",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15WN72WErfdRAgGwkVEEPuyAzIFHSywHS1OW4TtHOtjl",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "e5691d7350c108e31c077d423cb2eedf",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1EuxXkZdvYzbkOOdrvhMIonTfwatgzvZB36JqW3htLV8",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d794d2e4742b9296be30f80cca929ebe",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1wyMv2fl7MT8cEhNfP4lMgYkkhFz62qnYB3J3ttGpSx5",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "24d00609320f5e94fb50d1eececd42ab",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "187Bww2Yac7Xjg0fHgK3NG0r7P0GRZ9Zz39wJj8lzznW",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1nWquKsEahnb8WwAg6FhaxVa73qaVyq8fMlGbs8db4ty",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a4ff335b113791e732922a271897871a",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1AidsJET8NBXMAEIdOBdi7dswRSiS912n5IouXAEsbKn",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
