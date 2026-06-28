"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1xVD0afVmCfZVyZdN6IoYwWdbroZb4lqI6vhxhSlWSSY",
    "1Z07ZTlsCpTrJUx9kIvGNMyXQkIPZPQbY0rzYMqCLiFq",
    "1yVW2D3DNj6K9UK9jqgOIBL9RBEdjrAAyHlPFwxK7SYc",
    "1QWwRJe91LtdJOlkOMIfDRUppeKsv3T8wbhTkaXdKpbV"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "a0e75b718cdd57da8b2b261c77094778",
    "570c185aaba8ddb72658d2dc76dca174",
    "f4665b2d6812b6eed1b5c63cfc434d6b",
    "cc827b9d65cc5d4069098dd0e3614ade"
]

LEGIT_PERM_IDS = [
    "f0a32df0cbb3ea2eb247551db7d77227",
    "45c7fbba3407879865bfc6b9215c602b"
]

NEEDLES = [
    {
        "id": "1xVD0afVmCfZVyZdN6IoYwWdbroZb4lqI6vhxhSlWSSY",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "a0e75b718cdd57da8b2b261c77094778",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Z07ZTlsCpTrJUx9kIvGNMyXQkIPZPQbY0rzYMqCLiFq",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "570c185aaba8ddb72658d2dc76dca174",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1yVW2D3DNj6K9UK9jqgOIBL9RBEdjrAAyHlPFwxK7SYc",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "f4665b2d6812b6eed1b5c63cfc434d6b",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1QWwRJe91LtdJOlkOMIfDRUppeKsv3T8wbhTkaXdKpbV",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "cc827b9d65cc5d4069098dd0e3614ade",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "114gWNu8wNMYeUgs1Q8pDipfTOgC7m6q67G34wxsbpw6",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "f0a32df0cbb3ea2eb247551db7d77227",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1fU5JPDYBHFrMqg2eupn8F7TVwdW1K9Y5NhaSFyLnKhW",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "45c7fbba3407879865bfc6b9215c602b",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "14BcSigrCjlVzBN5e54J7lgWlXn2YTouTghKxWRiBguL",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1VWCPKTKhTwlughZpckycb2Uo2J7B6qWsS8qsWyTiWgC",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1OQDKBxFgcBLv1QBNwpxECGnKovNl435EncrWKOZl1sq",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "18MMZbdrpfYN90OIpbKcu5hnV1D41ulLixEhHJ7vO8oV",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
