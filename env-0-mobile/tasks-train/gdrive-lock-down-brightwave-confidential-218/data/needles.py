"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "11UOOQUoabwBvZGbr4H3jFG6aIf7r0MiAN9aeiwOWtna",
    "1ifvCZVzvVuhaFzY0Bj1nwxoZsWYc42opA8QF2IIJWc0",
    "1qkJTKxKtr0hHEL4Wm4y7YSi6XlxnKRwPuAEAxtwhj1P",
    "1AemYmhYk4Frs8EbSWiRHZt8fUfB5HPNN5CzkDUapff5"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "316fb4637f837fa48c6dffb97a2906d8",
    "acb67ffce973e016eb23c2f61141afde",
    "6fb1f06dde0ce40d5af989102d74bb70",
    "1fff839726a1f589cddb709286e91bbd"
]

LEGIT_PERM_IDS = [
    "656781414d41a4228a7d01bb0405a98a",
    "746cc030ea0f387ca7207aaed2be50a9"
]

NEEDLES = [
    {
        "id": "11UOOQUoabwBvZGbr4H3jFG6aIf7r0MiAN9aeiwOWtna",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "316fb4637f837fa48c6dffb97a2906d8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ifvCZVzvVuhaFzY0Bj1nwxoZsWYc42opA8QF2IIJWc0",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "acb67ffce973e016eb23c2f61141afde",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1qkJTKxKtr0hHEL4Wm4y7YSi6XlxnKRwPuAEAxtwhj1P",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "6fb1f06dde0ce40d5af989102d74bb70",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1AemYmhYk4Frs8EbSWiRHZt8fUfB5HPNN5CzkDUapff5",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1fff839726a1f589cddb709286e91bbd",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Mhcip0un3UgFlgJM4u9fDVG79FThQfincLwKXitDrY0",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1v3y9DpmcwFaR6l3LNiD99FaUrMZTVex2afVY7tyqFzd",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "656781414d41a4228a7d01bb0405a98a",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1aDs0CG3S1S2YwG0K72WmRiPZDLT0uE8bmPL0mcvr464",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1O3rJnoaUbNDrCrkChOJTtRXD39I9FO9j3ANciL3Rut2",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "746cc030ea0f387ca7207aaed2be50a9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "14PseWzDwrsTLmOO6RhE2wAu7ZB4pGgUJZcNqiGOMM0G",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1F7Z6pVCHXfN5aGPzHPzUpeSeekt6ICsd2Clz1foIAlA",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
