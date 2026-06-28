"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1hZYE6K198Nx9NW7ELoTn1GMhMHjO9w4MBwAKftPOZOa",
    "1Cw4rBKX5xWFu8gjlUjGSulhPtTzAQyRcQMeaEYC9YHT",
    "15sFiXOge5gVTbxPVxV5L2m6zJHfdSSVq3NPjgaM2ET3",
    "1WGSpcUf8KSuiIrJaw1kX39DSjRA0xgLjwF39a44mu0G",
    "1RuNMvb67tnLxq4bfsPGH8pis4CDFC3GNuRoqs1mAUcu"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "7b726ed7cd8a433b045db737d3463fb7",
    "dad76accbfaded725a50c6f96524f8c4",
    "b62453f2c2767aa60a353c3aa718b73b",
    "c7cc8829d7dd5768ee5f4a86ee96eed9",
    "d04bb3a048b7b77528ef7b8a852266cb"
]

LEGIT_PERM_IDS = [
    "7a11bd3154014d53a66c330fc6073fe1"
]

NEEDLES = [
    {
        "id": "1hZYE6K198Nx9NW7ELoTn1GMhMHjO9w4MBwAKftPOZOa",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "7b726ed7cd8a433b045db737d3463fb7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Cw4rBKX5xWFu8gjlUjGSulhPtTzAQyRcQMeaEYC9YHT",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "dad76accbfaded725a50c6f96524f8c4",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15sFiXOge5gVTbxPVxV5L2m6zJHfdSSVq3NPjgaM2ET3",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "b62453f2c2767aa60a353c3aa718b73b",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1WGSpcUf8KSuiIrJaw1kX39DSjRA0xgLjwF39a44mu0G",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "c7cc8829d7dd5768ee5f4a86ee96eed9",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1RuNMvb67tnLxq4bfsPGH8pis4CDFC3GNuRoqs1mAUcu",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "d04bb3a048b7b77528ef7b8a852266cb",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1PeIAlslCkKiTbKO2TvG8AF91Vllil76ZmeBLXJggaf3",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7a11bd3154014d53a66c330fc6073fe1",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1DAgQnCizTlZWokln3Zjt05TdyY5CAanzB4iksmkyOM8",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1vYwdHNrKlGbn6yOQZVKHellg6DhiTRy0tGFPT45lAXJ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "12VqvXKYLWplNg61jy2nypiyKMfTDVQCu1axXxNhU6Ik",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
