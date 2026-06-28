"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "19TLLGvmGeRKisSvRla0Y4Oy5n8lSZ16MAYGkCseC99a",
    "1b6dhqDl5ygi84a4HGhyy6Cogs1pfPw405bFN9dHsqPr",
    "1DQhEwz68nt5kFAcgoGGJ6gzSZpIKEewvoimRyZdUZxP",
    "1cCwBK2oqH4eh2aY8cRQPrnNi2lnO4A2OPATw5JwxZhh",
    "1ahWUtjRXdiU5KBGDcimmdcRluFTFmeVV7ilJ2XeRYMm"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "3e273c043a7ec3b5c2ddda1b6e89c06b",
    "fdacf0b080d7480f0cdd728724dfc5ae",
    "96030dacce253af2c265a36eb7571d1d",
    "bf5c3967035afabd57b9eac445266dbc",
    "8644cab06f67c6b68f1e43d639b1f4b6"
]

LEGIT_PERM_IDS = [
    "9226ff3ead90f4f7e725bfdc5836e10b",
    "622460622933b8231632c5d63bb0234f",
    "3de4df0fb27316e5d0ecc633002baf6d"
]

NEEDLES = [
    {
        "id": "19TLLGvmGeRKisSvRla0Y4Oy5n8lSZ16MAYGkCseC99a",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "3e273c043a7ec3b5c2ddda1b6e89c06b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1b6dhqDl5ygi84a4HGhyy6Cogs1pfPw405bFN9dHsqPr",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "fdacf0b080d7480f0cdd728724dfc5ae",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1DQhEwz68nt5kFAcgoGGJ6gzSZpIKEewvoimRyZdUZxP",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "96030dacce253af2c265a36eb7571d1d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1cCwBK2oqH4eh2aY8cRQPrnNi2lnO4A2OPATw5JwxZhh",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "bf5c3967035afabd57b9eac445266dbc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ahWUtjRXdiU5KBGDcimmdcRluFTFmeVV7ilJ2XeRYMm",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "8644cab06f67c6b68f1e43d639b1f4b6",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1NYEGbhzaLzf9lR5Db6gg4VIm3QD6WldsJxD60hExTCQ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9226ff3ead90f4f7e725bfdc5836e10b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1lHs8w1BsdLnmiKHHyrhIxOeLl2o9zal8EsKHq2vARyF",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "10jymn6kt5KplwCccwccnXXaXyShYhM2NlB9eYcX7pK3",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "622460622933b8231632c5d63bb0234f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1vjYm8CfKIPp3WTb68vGGUd2UAH0FvPnBVS7dTYyFt8S",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1UdphVBzp8xxrbpptGMvpK6nX9NQ02a9jp7OQYgKLNvr",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "3de4df0fb27316e5d0ecc633002baf6d",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
