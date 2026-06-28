"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1JQPls0lnB9tjkjjfJNVPdAEyMq2We7ErqoNfjGPdmGC",
    "1MgX16z3JCnt4Sz1sNM65WUfTM3lSb1u3keQM2i7TGt5",
    "1doqRhz8c2TRqKpib5xXXd91TdkUo5QJFuCJ9DKfgFqf",
    "127cvmzOrgGTPB1qf0m5pqFAEM1NjcpgIQywUz2OtEfc"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "ece76bcc391c30520c5470a163b47383",
    "a7aa869aad41239fecd50777fb4500db",
    "24bd9ac6071c56e4eb1eca59285e0121",
    "af4b3547ea09adadab0a971ad95ea928"
]

LEGIT_PERM_IDS = [
    "0802de2ba76fa81f8ebaaa81751796ce",
    "89c48706931bfa99430eac813fc7a4a6"
]

NEEDLES = [
    {
        "id": "1JQPls0lnB9tjkjjfJNVPdAEyMq2We7ErqoNfjGPdmGC",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ece76bcc391c30520c5470a163b47383",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1MgX16z3JCnt4Sz1sNM65WUfTM3lSb1u3keQM2i7TGt5",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "a7aa869aad41239fecd50777fb4500db",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1doqRhz8c2TRqKpib5xXXd91TdkUo5QJFuCJ9DKfgFqf",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "24bd9ac6071c56e4eb1eca59285e0121",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "127cvmzOrgGTPB1qf0m5pqFAEM1NjcpgIQywUz2OtEfc",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "af4b3547ea09adadab0a971ad95ea928",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1kdJovNTCmqTAmtjpAAmwmP8kxhpRJfibOipEFeL9vtt",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1lH2FRo5KjBKakwYhD5NKxkjOLexwXOQ1KMYqcWAVodL",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "0802de2ba76fa81f8ebaaa81751796ce",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "17lSdgvqtMIWSCr3vuDyi5sBD1HX6LrXzELWgG8RM5Uj",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "89c48706931bfa99430eac813fc7a4a6",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1lxKjzDsLhmn7ly30sAb4Ov5NxQGt3qhuvCljzXMPQbB",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
