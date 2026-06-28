"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "11lQzJG29v6aaUhqy8BmBX8disp7YIvPicafAnPhN37M",
    "1awM1KBfD0xOFo6Bm2uGYiMnxpnwybUiyEKKL2QIAotS",
    "1v0itNrqsICkwzpAtDN9CqEs7A9MYThvZ4rd5grsNAmj",
    "120N4ZLqiLCw0ua6NSPcFrGWJro11uZZtCvYBfnaedEU",
    "1hRKjRLviWrZd4lDfolRlHWanaERQzinfxEc7OFFD2Fg"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "3f05736f83f9f4fd6609f5d59c292947",
    "d7bb11ada83241cc113af09f1767b3f6",
    "bd19c295b71d4ba2d1c3613b50552516",
    "36427e92f66a9ad8cdc257f9235bc7b0",
    "11d3286588596bbb3a5befbf1fb95f9c"
]

LEGIT_PERM_IDS = [
    "0424b43bf53643fe5b395c59f614e4f6",
    "f4ce522f89ca1b65961ee2e200058f99"
]

NEEDLES = [
    {
        "id": "11lQzJG29v6aaUhqy8BmBX8disp7YIvPicafAnPhN37M",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "3f05736f83f9f4fd6609f5d59c292947",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1awM1KBfD0xOFo6Bm2uGYiMnxpnwybUiyEKKL2QIAotS",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d7bb11ada83241cc113af09f1767b3f6",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1v0itNrqsICkwzpAtDN9CqEs7A9MYThvZ4rd5grsNAmj",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "bd19c295b71d4ba2d1c3613b50552516",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "120N4ZLqiLCw0ua6NSPcFrGWJro11uZZtCvYBfnaedEU",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "36427e92f66a9ad8cdc257f9235bc7b0",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1hRKjRLviWrZd4lDfolRlHWanaERQzinfxEc7OFFD2Fg",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "11d3286588596bbb3a5befbf1fb95f9c",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1DntR6IbCgYtDO5kxXmtuv9MG8TMkQWTmz2FsKTk8zxI",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1YTVvn1IKwTkfIkYjals2m0jIm52UutKMxCwz7XVle3R",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0424b43bf53643fe5b395c59f614e4f6",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1sMAMjfoAlwNH0fz0lzSwDeUtzHvLcwUjRQYh3Fo0zp9",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "18m3pCwKtcYND6eDnLDWqp43XDKLn46GiTW1wl36kl9c",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "f4ce522f89ca1b65961ee2e200058f99",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1BH4bZGGslrD8Ow99j1mR0RSKyiJkM7evAs4FyH5LKCZ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
