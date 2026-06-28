"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1EwqsdT8HPDFQ8JB9C0zKeiaR1QShdZrsNnDEZ9dzm2s",
    "1qFJI6vjj3156uQ0pOk7U78JbPL1TU6D91hs81FnwL1Y",
    "1tixs7fDQwnOpCLl12RcECv1cNVu7T6FF24Ayl2NzfuD",
    "1sKoZSMLl2IvnGsHUveZAyp2xyVcHY0jGEJQRD6gYr2P",
    "1EsvpoSwFqu2TIIczuhG49hH1ZDYsCbGUZa6ACna63FU"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "2949010c96233dcfc8a7d9507cde35e6",
    "24470be46d6d5a4af432d1ca26db2274",
    "c70e3fb5adb0fdf374e3364b09d87eff",
    "d2363e41da803ff866b3bb9bab394a2c",
    "a39a0c981da476417a3dd4883b7dcbec"
]

LEGIT_PERM_IDS = [
    "b4a19d2c2de2b84b3c97f77bbc5dd618",
    "e887df9a7588b5fd4a83bdbf1745bb09",
    "02c963f811aa7e3f04df331d5f3f4534"
]

NEEDLES = [
    {
        "id": "1EwqsdT8HPDFQ8JB9C0zKeiaR1QShdZrsNnDEZ9dzm2s",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "2949010c96233dcfc8a7d9507cde35e6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1qFJI6vjj3156uQ0pOk7U78JbPL1TU6D91hs81FnwL1Y",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "24470be46d6d5a4af432d1ca26db2274",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1tixs7fDQwnOpCLl12RcECv1cNVu7T6FF24Ayl2NzfuD",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "c70e3fb5adb0fdf374e3364b09d87eff",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1sKoZSMLl2IvnGsHUveZAyp2xyVcHY0jGEJQRD6gYr2P",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "d2363e41da803ff866b3bb9bab394a2c",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1EsvpoSwFqu2TIIczuhG49hH1ZDYsCbGUZa6ACna63FU",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a39a0c981da476417a3dd4883b7dcbec",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1B6Fi6LTZGe7f21cxiCkReyAIfyuJPDt8e7aowcggis7",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1QfpV5ffDfM6yHPIpFQJvIyPzoOYANOgC953tFPzMdLE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1TSpzByzNVQPAEUiXof3mdcQiSzz52nsYtxKD2txvK3P",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1XakVvZmqaPuqr4zTGXCcfIDusEmM8gy82BBj5yvmykS",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "b4a19d2c2de2b84b3c97f77bbc5dd618",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1FoGpyJml1MiKkRL9U75BBvn5FSE5BGVmEUEsCcUr9k9",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "e887df9a7588b5fd4a83bdbf1745bb09",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1SP2sv686AYZzk6ImCo3EXAhZmVwGGYoOtPJSNm0Rxrb",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "02c963f811aa7e3f04df331d5f3f4534",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
