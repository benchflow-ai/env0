"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "19qM72psqbvLyC47JAEoE5BYSXGrcIrFCJ7VzJK4Gguk",
    "15xmvcBJ0SvWoQXlBYhsvdiFZF75BzLJettLZi0YQ6wU",
    "1MsdZsQa3LZkXW7HdyrgQS4ekd3mScMwzYITcwtGN4Z3",
    "1rAI5qCOHi9b9aIpPiI4F7vhPOxRjJE2LqdVMkpTNJua"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "62f2f6ce4410a9f45aee39aeada53ec7",
    "e3e300f74bbc33b04661e81627bbb752",
    "d052898cb359d24736aef53c2db0da80",
    "39c14e0b5691dbeb4a3c4123b6831a34"
]

LEGIT_PERM_IDS = [
    "02564d3689f5ec7e1c8fb65528452e99",
    "e3fb1c4f9185659a86f496a5ecbf9e9b"
]

NEEDLES = [
    {
        "id": "19qM72psqbvLyC47JAEoE5BYSXGrcIrFCJ7VzJK4Gguk",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "62f2f6ce4410a9f45aee39aeada53ec7",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "15xmvcBJ0SvWoQXlBYhsvdiFZF75BzLJettLZi0YQ6wU",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "e3e300f74bbc33b04661e81627bbb752",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1MsdZsQa3LZkXW7HdyrgQS4ekd3mScMwzYITcwtGN4Z3",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d052898cb359d24736aef53c2db0da80",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1rAI5qCOHi9b9aIpPiI4F7vhPOxRjJE2LqdVMkpTNJua",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "39c14e0b5691dbeb4a3c4123b6831a34",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1MunOxEKbPPocWl5Vuu2oLdPruQ5I1YkfRSKPg0O9bcC",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1uRqVS20kG3Vuzg5Y9EJ32hwFTvcaOcDwy1HG30gYH9L",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1dCFAj0lJApKGjOd1IUZnIH3CsH8OIQK9RlR9NwhND5K",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "02564d3689f5ec7e1c8fb65528452e99",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "15LUXFxyDoVbQsP9lMCTecS4t3C3QZWvpcB7Ykxw7xNz",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "120wUlX9dNj3PJGx47VbhcPz64Md3j69ERsiOM9LU3pa",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "12xm8oPLtgznUeVby4kxaHr6CmfhLJEXZ6VESORT4t13",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e3fb1c4f9185659a86f496a5ecbf9e9b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
