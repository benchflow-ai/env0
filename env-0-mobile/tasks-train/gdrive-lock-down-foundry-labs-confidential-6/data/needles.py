"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1F6wjf0JWw4MyfAbPvWGsB3qdsCm3yoEV8JFhiD3WNYg",
    "1ikRGb1Bal2KcIfwbIBgw3nF9FqF4zB5jLOMZOgz8Ik6",
    "1VKpT9fSRsNjJ4m0hQT87LIXldXnxVfMX7VMYAdtr6Gs",
    "13EqveCvXz0PBsibv4w9LJ80pZIZ9CAx2ogkkKMkTkrQ",
    "1ufXjbQvVYZ8dQEuELDfC7ixLGqsHUYcmkpy5xJhbYRG"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "8c1f75f5c630a8402f68b16a68ee8e26",
    "5aeef949272934edbae0388dcdd8c9c3",
    "d9885fd0c659ae224a44ca73e6512d0e",
    "09e13c1c9c301fc0d0df5d67d4da56ec",
    "c7ee252c86f89bfcf14243fbd1bbf97d"
]

LEGIT_PERM_IDS = [
    "72e6c46ea38a3bbc7e78131d10892d70",
    "937ed4fdaa4e87a7c380dcf790811aba",
    "a1332c96604a5ceeedff88a6154198e0"
]

NEEDLES = [
    {
        "id": "1F6wjf0JWw4MyfAbPvWGsB3qdsCm3yoEV8JFhiD3WNYg",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "8c1f75f5c630a8402f68b16a68ee8e26",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1ikRGb1Bal2KcIfwbIBgw3nF9FqF4zB5jLOMZOgz8Ik6",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "5aeef949272934edbae0388dcdd8c9c3",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1VKpT9fSRsNjJ4m0hQT87LIXldXnxVfMX7VMYAdtr6Gs",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "d9885fd0c659ae224a44ca73e6512d0e",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "13EqveCvXz0PBsibv4w9LJ80pZIZ9CAx2ogkkKMkTkrQ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "09e13c1c9c301fc0d0df5d67d4da56ec",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ufXjbQvVYZ8dQEuELDfC7ixLGqsHUYcmkpy5xJhbYRG",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "c7ee252c86f89bfcf14243fbd1bbf97d",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Op51fssA2O4VY5b99e6hnDG9ZkmPxRB1MnQ9NTLJst4",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1x8V6vcuXLA0QilxGJn7E6kJo4rMv6ATL3HItOaJRGTg",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "72e6c46ea38a3bbc7e78131d10892d70",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1zAZuPqrsB4MvLVFaj9IElL7YTfsl1a8sQgMYINPunzn",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1v8tqQNiG7MRzVQK1Iqvr1StWiZ0dIXJQxNzwVakFMip",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "937ed4fdaa4e87a7c380dcf790811aba",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1KvbM5J4ksefthNbRVb0QQrY0I2q86zbJ2kK99C2rkRn",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a1332c96604a5ceeedff88a6154198e0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
