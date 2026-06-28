"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1jgEObeZFclOKDB6rERlJWckOnCpOq9CUuCSmYQ5TYBw",
    "1q5OuVcnyrqQvneXqUbm19XPdHUtZVnLrWRGnniouLZB",
    "1P3gXmDcDCORQaBRaxc4snMEkGK7mukyxDoNRgdDjirs",
    "1D8z6CUzpkYFCbudZHSf5sFo1Kfs6pbCKrfbDiGna8M6"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "19e781e87ce4465de80b6315fbc6c1fe",
    "bb7e5e3d85201c776b6bb52833a3d22a",
    "ac6ae5c097c0d8169ca6b6cefa4e8fbb",
    "d00083fb57d9ce5adbd694ca01d3c444"
]

LEGIT_PERM_IDS = [
    "f448b951befc40ec87624ae63342bd06"
]

NEEDLES = [
    {
        "id": "1jgEObeZFclOKDB6rERlJWckOnCpOq9CUuCSmYQ5TYBw",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "19e781e87ce4465de80b6315fbc6c1fe",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1q5OuVcnyrqQvneXqUbm19XPdHUtZVnLrWRGnniouLZB",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "bb7e5e3d85201c776b6bb52833a3d22a",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1P3gXmDcDCORQaBRaxc4snMEkGK7mukyxDoNRgdDjirs",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ac6ae5c097c0d8169ca6b6cefa4e8fbb",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1D8z6CUzpkYFCbudZHSf5sFo1Kfs6pbCKrfbDiGna8M6",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "d00083fb57d9ce5adbd694ca01d3c444",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1qoo09sBWh7P3piOWd7zwwbGTCeeGoVJvmOkxezPfhLE",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "15DkkKzQWyl5sQcrPMJFQeBa1vXdxs1sxDuzMhAUCgGy",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f448b951befc40ec87624ae63342bd06",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1M3iYFXlgvKMtbAA40aEXktM5a2NJyAASiFcf4jMhsdi",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1thR1yKkqP9KYAtar7GBKdfpFVCH3G5L2Cbv93PfSfE5",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
