"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1rZ2PM3ZriIhHBXM4Vm3HufWSghgEcKyXGe1fOUqvNmt",
    "15eujJyIcIAyvbLnzXuzzPiE8I8vACMUkebzQplDHvFn",
    "1RZJoMA64qnQiAxcSXVioa9tx2Afx8iOBr8mjfIFmimg",
    "1N6V3P5uDHzcsKy1Bay01VWstAozAUuot2SHyZ9NVua3",
    "1YzsQ4fN8QJYeaYlsD8BAWMxcx9fRyhgyKhISZD9g9UP"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "2f5f25743ed8cb1f6f4645b4f084f3fd",
    "4438d4351d0f497ffa8c245628403320",
    "15f17f887a6c410f0d6e64b44bdf1df8",
    "577cd224cc11c53bfe1e2f22490ea128",
    "a06db200103e7bb2179f8078dca70aea"
]

LEGIT_PERM_IDS = [
    "1c9321b356b5b83c7cc7e604e604c917"
]

NEEDLES = [
    {
        "id": "1rZ2PM3ZriIhHBXM4Vm3HufWSghgEcKyXGe1fOUqvNmt",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "2f5f25743ed8cb1f6f4645b4f084f3fd",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15eujJyIcIAyvbLnzXuzzPiE8I8vACMUkebzQplDHvFn",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "4438d4351d0f497ffa8c245628403320",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1RZJoMA64qnQiAxcSXVioa9tx2Afx8iOBr8mjfIFmimg",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "15f17f887a6c410f0d6e64b44bdf1df8",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1N6V3P5uDHzcsKy1Bay01VWstAozAUuot2SHyZ9NVua3",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "577cd224cc11c53bfe1e2f22490ea128",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1YzsQ4fN8QJYeaYlsD8BAWMxcx9fRyhgyKhISZD9g9UP",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "a06db200103e7bb2179f8078dca70aea",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1lUA70dutp0MdIw7UBjJVaRH09obFFaWjOOueA68x6FP",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1XqbAuwPRiDtRR6xp27Qw7OJG58dhdbWZGuVpOKbqmVY",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1vPqJIXHAM4rygL5p9FvpxL3n0XYEYSNeEGKgJSZmIYo",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "1c9321b356b5b83c7cc7e604e604c917",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1UIGKPKQweBckRfraQrrnNH2YZrf0WZTSQuvLg13FH3t",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
