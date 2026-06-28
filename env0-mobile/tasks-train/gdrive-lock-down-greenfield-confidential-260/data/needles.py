"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1yU5Y1YN5M3wMKtjtnJsWCSIwCSsljKrNrUHV96o6Yoq",
    "1ul5vSSLlmabaaWNj9UYXQM0tw4bbBVWaREunEwuOl76",
    "1cXubPzXKoy64UtSUMBMhZ9vAkkE8Jbmqz0usubduBUq",
    "1c4U0WNeiOi6SMKtq1lqNq6D75bEd3fkR2QO6Unvmm93"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "9913fce26d81d1cc249018bb72642fe3",
    "9eb22155ab5fc67f74fa0d3e093fdf8e",
    "68cba08b0c047737541021bfb1f56e66",
    "a155d8f8e929c90a2b0ee04dfb2f89c3"
]

LEGIT_PERM_IDS = [
    "c4ce8e3ee8414cfd5a9cd518dbbc54f1",
    "b3cfec48a016994ef8397e6c7ee774ae"
]

NEEDLES = [
    {
        "id": "1yU5Y1YN5M3wMKtjtnJsWCSIwCSsljKrNrUHV96o6Yoq",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "9913fce26d81d1cc249018bb72642fe3",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1ul5vSSLlmabaaWNj9UYXQM0tw4bbBVWaREunEwuOl76",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "9eb22155ab5fc67f74fa0d3e093fdf8e",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1cXubPzXKoy64UtSUMBMhZ9vAkkE8Jbmqz0usubduBUq",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "68cba08b0c047737541021bfb1f56e66",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1c4U0WNeiOi6SMKtq1lqNq6D75bEd3fkR2QO6Unvmm93",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "a155d8f8e929c90a2b0ee04dfb2f89c3",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1WjB2hvZVyz6gR6B7xv9ZIZ0YdmWxAoFRFZAJSg2blC4",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c4ce8e3ee8414cfd5a9cd518dbbc54f1",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1B3BvrE1xWR092UCiUIK2F4GQ9VMmBi8JzImemKh8pWK",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1AIuBhiIRl8ENjFx4UhAEWtcRxa2ATEmGDnl7jykf8vC",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1ocB3uhSDFsqIaOGCJkJRx4hET3OOaIlu5jJo05vJyE1",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1gmWUszDri6kRH4ou5BjVPPC0LezF7tRZHo79H17tDBk",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b3cfec48a016994ef8397e6c7ee774ae",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
