"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1Syuw4FlfboRF6wKFFixatE6aehY6OrFJ7yDDBUxV8Zp",
    "1wFW5yHT6OLIFc7hhqq00hHGNb77W5QTVZr0Y73ROIDe",
    "1IKUgoIcvpIBbB162EprDO766VaANuJEWhn3pOB0Qj4x",
    "1W0lp7dUS1JmI1i9ltFDvVeobQ2APRYCvuJakI7rHyR7",
    "1JhpGYln6hEvlbxvkhHZxk75e34YL5aVkQw1u9USteyX"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "cd316dd9c538a35d8e5e3cb1d09b1afc",
    "7183874a389c0bb027ce58c6fffb1bb7",
    "de1767bc44471c0d74a0a32dacb371d7",
    "e087197a64202bca1ad71af77078d8c1",
    "ee95eb18391320e97c491d279b0b761b"
]

LEGIT_PERM_IDS = [
    "101e8b99933ffafb22ae9b31212d3328",
    "006b82644400e3838ca9a2d2676739a4"
]

NEEDLES = [
    {
        "id": "1Syuw4FlfboRF6wKFFixatE6aehY6OrFJ7yDDBUxV8Zp",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "cd316dd9c538a35d8e5e3cb1d09b1afc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1wFW5yHT6OLIFc7hhqq00hHGNb77W5QTVZr0Y73ROIDe",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "7183874a389c0bb027ce58c6fffb1bb7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1IKUgoIcvpIBbB162EprDO766VaANuJEWhn3pOB0Qj4x",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "de1767bc44471c0d74a0a32dacb371d7",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1W0lp7dUS1JmI1i9ltFDvVeobQ2APRYCvuJakI7rHyR7",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e087197a64202bca1ad71af77078d8c1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1JhpGYln6hEvlbxvkhHZxk75e34YL5aVkQw1u9USteyX",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "ee95eb18391320e97c491d279b0b761b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1eMFctrdbQ0HJDf4WKNhzO1JUwRJ4Xj8HRBmrukb9Acy",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1J3GUyGcFqOVSxR8pzLdNCY1QScUljLSv4VDS6iQfrc2",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1HGFPACn6lvwrDVCFsIPLCEqYuboGFZSvibyUOOO27Vc",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1vO55lJGt1ETJBrwiov7tKBi2p89Q4s5MGGOJ3EgN3MJ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1xRhy6fIuOCR4OXarWYhLNF8J0iqwrVi4VbjuwsEFeRv",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "101e8b99933ffafb22ae9b31212d3328",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1r8LYA6NBaF4zMmaixlF8EyxlROVK607hEDvMLvKEa6p",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "006b82644400e3838ca9a2d2676739a4",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
