"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1vx4AWQO2WMfNwWek9TY8OSLGxfTqlMlkXjAFeylAj6v",
    "1uzXzp77fqlYnRnhAtjzC1gOrT5SpBKLXLc9DxLrBfW5",
    "1ON1CEgXYtYmi1VDfDc28OfWX7j6YkVQNzg9F6nJ5OCy",
    "1jBTNkqFHuXSThuuJaM00NxZVneV8LQcH3MvP1BWlMYo",
    "18afaO6JVRO3BEVDYIqt7EeC6FOzPRHFM0qg9CNfTElP"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "494bb8e08b0b1d43d95b51ebe736e4b4",
    "749305ca6ae6170b153c6f2a5d10e83c",
    "6904503954e9633652a7957618e2342f",
    "b17332b7f9e04b5efbd5d862b54cd0e6",
    "404114be8eaac679a7cb938d3c6a589b"
]

LEGIT_PERM_IDS = [
    "9f122522a99340f72c23505b7a47c729"
]

NEEDLES = [
    {
        "id": "1vx4AWQO2WMfNwWek9TY8OSLGxfTqlMlkXjAFeylAj6v",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "494bb8e08b0b1d43d95b51ebe736e4b4",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1uzXzp77fqlYnRnhAtjzC1gOrT5SpBKLXLc9DxLrBfW5",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "749305ca6ae6170b153c6f2a5d10e83c",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1ON1CEgXYtYmi1VDfDc28OfWX7j6YkVQNzg9F6nJ5OCy",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "6904503954e9633652a7957618e2342f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1jBTNkqFHuXSThuuJaM00NxZVneV8LQcH3MvP1BWlMYo",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "b17332b7f9e04b5efbd5d862b54cd0e6",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "18afaO6JVRO3BEVDYIqt7EeC6FOzPRHFM0qg9CNfTElP",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "404114be8eaac679a7cb938d3c6a589b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1COffo9X46EO7hNEUcYtDRM5nNEGZNFWLJQXInQmRiwA",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1MIBakkMaWf6sBrgU9YZTRvhHHl2AFkpDe3MENNHNvBH",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1nlYLZAiTm4fq2HDf2EX7Lo4ncnJXUBnYd1mGFpgT7Qq",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1tvYcGltJbXMH8BHSQejS59hd3kLdszHOOD8aGpAA2rc",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9f122522a99340f72c23505b7a47c729",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1xgdPS4arSUAxBUJPPK1Fq3M10mywnRJ3jh23Q2O5akP",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
