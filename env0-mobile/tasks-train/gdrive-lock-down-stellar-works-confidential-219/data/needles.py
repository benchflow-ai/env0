"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "14GmPz8H49yVIpJ74EwZSn7H4oD0nHr9GF4kckigylK4",
    "1gctPRgzdPcWhOX9G5ybaoAXOnkputBCHDwqXFnizu5V",
    "1Pv08JtcdOXi5YOUsARMB2vQzYKgMm8tZK9U6L0caIFn"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "bed9fecd618226434eef8f40c6a9fa3f",
    "f49de7a98575d6f569919a7e7db80049",
    "993fc267280a13ad21780d635e7d652a"
]

LEGIT_PERM_IDS = [
    "aa1d0153444bb2074da2546674547750",
    "52325335e9e66f3e28653a933ccff594"
]

NEEDLES = [
    {
        "id": "14GmPz8H49yVIpJ74EwZSn7H4oD0nHr9GF4kckigylK4",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "bed9fecd618226434eef8f40c6a9fa3f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1gctPRgzdPcWhOX9G5ybaoAXOnkputBCHDwqXFnizu5V",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "f49de7a98575d6f569919a7e7db80049",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Pv08JtcdOXi5YOUsARMB2vQzYKgMm8tZK9U6L0caIFn",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "993fc267280a13ad21780d635e7d652a",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "13Ha8CFl6J9S6bkHFeSkMLjjsx3ionbrMJI9rO84B0wu",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1dXsmTbd9qgrMw86K28IuZv6PH2KSxSniIfnlRvoahlz",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "aa1d0153444bb2074da2546674547750",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1yT7MYBdmwaXcL40fqgmzMhB2HMhXh5V8Nl9eWvv5xiA",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "52325335e9e66f3e28653a933ccff594",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Q5bvu4qVCh7xUDpzc8qsSTdWCeVwQhJkIol0DO3Kree",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1uns0pss7eNl0n52ovfPJLchVWVp40Mo0BK7wJ4bAPAp",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
