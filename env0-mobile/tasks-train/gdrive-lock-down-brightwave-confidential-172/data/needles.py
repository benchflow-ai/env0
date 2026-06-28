"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1nMIzJ1JBJ1rhrOjLfbYNdDwMh6UxcwUsEbwMNXFqNC6",
    "1dnpvprWB8Pmz14DdkDJhj073nji8iaRiJ6jtcY1U3WO",
    "1Q43gEYRWdVX31LVVgyOFiwWyySDdVhj4t62Nzj9k1H4",
    "1S8IU12JKwF94KjFuNO7maGDSahGIILGwLYZ6rgB9wJG",
    "1ujmuUvvX4oR2RRHwWSGjWjVIgu5fC9FLjIHVsa7dDXS"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "3b42503be0865d4e4bde5aad2cf77d9e",
    "38265a738701c1c9b28355d4a8740056",
    "38c8ff55c184c420f6f4655f4196dbe9",
    "dd2bf598e9fb468dfb00869ea7a45565",
    "e6e321136afa521324c3e1a760dd487c"
]

LEGIT_PERM_IDS = [
    "b2d36d83212a1a26a74b66638aba8eba",
    "d8908da20f722a37693a95db65b29993"
]

NEEDLES = [
    {
        "id": "1nMIzJ1JBJ1rhrOjLfbYNdDwMh6UxcwUsEbwMNXFqNC6",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "3b42503be0865d4e4bde5aad2cf77d9e",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1dnpvprWB8Pmz14DdkDJhj073nji8iaRiJ6jtcY1U3WO",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "38265a738701c1c9b28355d4a8740056",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Q43gEYRWdVX31LVVgyOFiwWyySDdVhj4t62Nzj9k1H4",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "38c8ff55c184c420f6f4655f4196dbe9",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1S8IU12JKwF94KjFuNO7maGDSahGIILGwLYZ6rgB9wJG",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "dd2bf598e9fb468dfb00869ea7a45565",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ujmuUvvX4oR2RRHwWSGjWjVIgu5fC9FLjIHVsa7dDXS",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e6e321136afa521324c3e1a760dd487c",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1XvU9TbK1hYpS8r33Iidcc0a74BIBIahYrlKPnGaijWB",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1n1uTm5AavgGuCa0H0H5KvVGG4ZFCOMewMStESYz2Qee",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1g0O52ao2LHyUtH42m9W7xIrXfJvUpe0oHpzAU3sgI9a",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b2d36d83212a1a26a74b66638aba8eba",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "11W98cP2eNzfOoG0ZMGWEIrkGthNkyu2IMWSzrzU10fC",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1cfKRnNSl7sHyBanIICceKbBnCEkVxsGtzDj1GnqPA6Z",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d8908da20f722a37693a95db65b29993",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
