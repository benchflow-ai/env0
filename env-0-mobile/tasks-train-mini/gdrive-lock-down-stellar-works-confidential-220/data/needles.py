"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1JIc4VMRqRp6b0EoepR8f83QLBbWwSln5w8abeKaOk9G",
    "16MOUcyJhoxvDpXTL8oQjuOpkc2V9S2WyF4wYagkB35v",
    "164B88sMpxFMLMXwbMiyjWFVLmCRymXmb7Kyej53ys1a",
    "1DnKJeR7A7w2xDg9gYNPJtBRrhATZlS5E2DnhbShYkOb"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "0a335f1781ec3f911002dde67bbe772d",
    "0c69fdd3829722d54725fdeacb2e00d4",
    "1464e076530bc5389f4ed651128942e3",
    "e9185e0b4eb3705914dc1fbdc5973f9e"
]

LEGIT_PERM_IDS = [
    "c17d86d24d2df3e761352ff28ed5c517",
    "87141d67399f9bd3588eb7adfcb3cb94"
]

NEEDLES = [
    {
        "id": "1JIc4VMRqRp6b0EoepR8f83QLBbWwSln5w8abeKaOk9G",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "0a335f1781ec3f911002dde67bbe772d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "16MOUcyJhoxvDpXTL8oQjuOpkc2V9S2WyF4wYagkB35v",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "0c69fdd3829722d54725fdeacb2e00d4",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "164B88sMpxFMLMXwbMiyjWFVLmCRymXmb7Kyej53ys1a",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "1464e076530bc5389f4ed651128942e3",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1DnKJeR7A7w2xDg9gYNPJtBRrhATZlS5E2DnhbShYkOb",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "e9185e0b4eb3705914dc1fbdc5973f9e",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1HGNtL3JBHYYwrVLzVBlQuAIgm4jXytCXQRE6k3OZQ6a",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1dOx5g5KMxE6fyGJNNE7s4WfMUPmTmRBDnweQNCsN7pS",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c17d86d24d2df3e761352ff28ed5c517",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1NCiTeT5W9gIRtg0AFNFOR5mm5Gx3QGwcXN3N7XJC3mw",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "87141d67399f9bd3588eb7adfcb3cb94",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1gOfBYTEHGtSWFiaqAKo6shQeUaMBrC5LZOR4WlKOsha",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
