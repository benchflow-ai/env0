"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1fW2qLtg1NRYpZPiyEYu07ktMLHr0lUT012bNZ621vev",
    "1VscxIlTHK7Vfl3DKJ7ijuXdpXze5o4yQ14gob4XTxez",
    "1mhIrvGZglSfC6OONKISG4RX6fYHlxkfaBDYfTGFtp2I",
    "1vuucK96NBD2FpDJ3fEV6mSpl97kzwvh6OieM4COogfa",
    "1tzGVqqKP2PfZw7766dmbZAMRZCzRZyHgL3oay5flY9K"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "3e549384a4e4cc0a10e4602c72bde319",
    "00cc0d3f1fc74d4d0d72616cc50b1ee9",
    "e055baa6056a5bc6f00f032c4ff2749f",
    "f69128bca811832f9886c66f4a8d2084",
    "9e5c5770fb3e90db9f96b490797757ba"
]

LEGIT_PERM_IDS = [
    "6b4c15f3313b16335dd572275fe597f6",
    "52122b2180fc81e588f5f97cdffd4e0b"
]

NEEDLES = [
    {
        "id": "1fW2qLtg1NRYpZPiyEYu07ktMLHr0lUT012bNZ621vev",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "3e549384a4e4cc0a10e4602c72bde319",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1VscxIlTHK7Vfl3DKJ7ijuXdpXze5o4yQ14gob4XTxez",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "00cc0d3f1fc74d4d0d72616cc50b1ee9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1mhIrvGZglSfC6OONKISG4RX6fYHlxkfaBDYfTGFtp2I",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "e055baa6056a5bc6f00f032c4ff2749f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vuucK96NBD2FpDJ3fEV6mSpl97kzwvh6OieM4COogfa",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "f69128bca811832f9886c66f4a8d2084",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1tzGVqqKP2PfZw7766dmbZAMRZCzRZyHgL3oay5flY9K",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "9e5c5770fb3e90db9f96b490797757ba",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1kP42CqRYUViwUHApdxgZnOlRhgOpvJXIvdXAtC0Hlum",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6b4c15f3313b16335dd572275fe597f6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1p4IRY5lTEZAM1yNPH3756CRvJJx0VmPul4SMPdJmWac",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1Vo5sOHm7jTYsew98RHP9VSQNrdRrXaHL8Cs5pmGzh4e",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "52122b2180fc81e588f5f97cdffd4e0b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1himQ4mrDn0qMWGsnu8TKb1cX0t3OXi6kcuPk5pyTxOD",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1cMfWCsH2efMqlfzllzCf55koW39YjN2KJaPbAS4dVVV",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
