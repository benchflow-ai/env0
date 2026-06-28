"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1Pv13bpldcbGKEc4KwnbkRBgW8OuWNviu10PZc5uyJFq",
    "1QJLuLKzcwY6EHPJqkCC0eYyymmuPaeVlvXfhhqiL6eW",
    "14Je1nwOcvuSEQcmtQuTzOWXrWqb37nRkyXBtcjV1RQ7",
    "1EgdjP5pQPp6oFMihky40stkMAsveT99zdBiqBbtEfbF",
    "13UM8FJQcsxseXoMaDYDfoNFkOornYuuMwV5LilxrfKA"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "4335ebaca413e6a9a9a8bff82243440e",
    "209e56c71a3b5b796b82de06acbb1f4d",
    "e4a6a768683eb14a307dd9e7cdde81d6",
    "665efff6dc5eab141dcbd7b01b890bed",
    "d84ec60535090d0a43dc8a0cdfb7f25a"
]

LEGIT_PERM_IDS = [
    "f449deb707f23deb43f65ec746c66e60",
    "c8092724a56c0a11221b6689265613f2",
    "0c8bacd7cddd1777b8ed9bd9620a268f"
]

NEEDLES = [
    {
        "id": "1Pv13bpldcbGKEc4KwnbkRBgW8OuWNviu10PZc5uyJFq",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "4335ebaca413e6a9a9a8bff82243440e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QJLuLKzcwY6EHPJqkCC0eYyymmuPaeVlvXfhhqiL6eW",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "209e56c71a3b5b796b82de06acbb1f4d",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "14Je1nwOcvuSEQcmtQuTzOWXrWqb37nRkyXBtcjV1RQ7",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "e4a6a768683eb14a307dd9e7cdde81d6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1EgdjP5pQPp6oFMihky40stkMAsveT99zdBiqBbtEfbF",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "665efff6dc5eab141dcbd7b01b890bed",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13UM8FJQcsxseXoMaDYDfoNFkOornYuuMwV5LilxrfKA",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "d84ec60535090d0a43dc8a0cdfb7f25a",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "10JPoOhU2ZfGeZQEL5X2ohfnlE7btBJX0zPDBiS11WOU",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f449deb707f23deb43f65ec746c66e60",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1F6CZ4lCgvcNnmfJSOrcRBMAuSl2UFqyqlUPtq4GZUej",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "16t0LoYHyVESPPobxQ9DtdHF20tYuSQXbPbmCzRYXGJd",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c8092724a56c0a11221b6689265613f2",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "10iMZc2LLynAqYs44U7tNCWnPCeAY5nWTbGUULTKwXHA",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1cOUzMFweteCawFbflgdtKzaqKoB14Uo9qnKDBJlCALe",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0c8bacd7cddd1777b8ed9bd9620a268f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1R4FkFdwHwRHZzbRyq01MHUioazC3qOHuyV3DfSZMs66",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
