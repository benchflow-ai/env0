"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1PrpF1uBvG9OKwn0gjuAlxrrcDhLxQF3NpgjSUnO5MOQ",
    "13y5KzaJkr2YOQYnqp3RgJlbGXkXQFijhN5htLjYCPxL",
    "1I6U1izTfChU7BfJGshMHkoDgQRZK8aCdkuCQQwdeCse",
    "1K0ggpeG8kh9fnYqvlD4UzYJQDeKOohbND6x1CBuv6Vm"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "dc4454371b7787562acd223497511b06",
    "67bf99a51c030bdd181d7b4b28fc27de",
    "817144b659750748755ddbee14413e80",
    "2a1a613738aa8fa743418c7931fab984"
]

LEGIT_PERM_IDS = [
    "3d2d53dc5c91e2bdc160784c5d2ae1bd",
    "e1b91469c6adda711929d18d197bd87f"
]

NEEDLES = [
    {
        "id": "1PrpF1uBvG9OKwn0gjuAlxrrcDhLxQF3NpgjSUnO5MOQ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "dc4454371b7787562acd223497511b06",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "13y5KzaJkr2YOQYnqp3RgJlbGXkXQFijhN5htLjYCPxL",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "67bf99a51c030bdd181d7b4b28fc27de",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1I6U1izTfChU7BfJGshMHkoDgQRZK8aCdkuCQQwdeCse",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "817144b659750748755ddbee14413e80",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1K0ggpeG8kh9fnYqvlD4UzYJQDeKOohbND6x1CBuv6Vm",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "2a1a613738aa8fa743418c7931fab984",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1BcVElszdD3OEj8F0Ex2VfUgH3w5r55FklimdVbWhYKp",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "3d2d53dc5c91e2bdc160784c5d2ae1bd",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1RVZcjbrHtyKfm7PpXWT47PE9oGKv5aUi6LodMCFCmNU",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1l7mCNbef7fzSsGIo2n8VBF52p2ZZGZi2SrUviaX4d15",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "13T6NDN1hynXFf8s7O9HqMsG07dGDgWVz53PQMGH24To",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "e1b91469c6adda711929d18d197bd87f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
