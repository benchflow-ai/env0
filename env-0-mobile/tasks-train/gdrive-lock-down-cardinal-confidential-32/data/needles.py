"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1bjNVVe4aNfv1pDlUtj3D9rnlBgl4IhqcMGmGdeUII4g",
    "1ItJKbRM5oXUXiSeBcMIt3vapKdD1GhlDJvpQWBL7wJT",
    "1jZ9PPqg5pXsuUaYFNBrpXfRn0rXzj3YjIvaRFKj9wKZ",
    "1PBZmdkGYcm96S5iwoGvDbKZ1hyAhbLiHMlLxp7QqL52"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "14995a4ad31b77aba0c5a5eea41ccc8f",
    "ce89f39ee98fcbf6ac6f29ca5664005e",
    "f57f7096c6392ebad049bb09c0c8fbd6",
    "ca5c4412b68504edb78e393afdf27e9f"
]

LEGIT_PERM_IDS = [
    "ea144d47619d712dc4e2f10de6a4fa40",
    "55981f6461c0d797c392d0bf15462a01"
]

NEEDLES = [
    {
        "id": "1bjNVVe4aNfv1pDlUtj3D9rnlBgl4IhqcMGmGdeUII4g",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "14995a4ad31b77aba0c5a5eea41ccc8f",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1ItJKbRM5oXUXiSeBcMIt3vapKdD1GhlDJvpQWBL7wJT",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "ce89f39ee98fcbf6ac6f29ca5664005e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1jZ9PPqg5pXsuUaYFNBrpXfRn0rXzj3YjIvaRFKj9wKZ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "f57f7096c6392ebad049bb09c0c8fbd6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1PBZmdkGYcm96S5iwoGvDbKZ1hyAhbLiHMlLxp7QqL52",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "ca5c4412b68504edb78e393afdf27e9f",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YhobkSpPdzn9lxCVyHPIWzS2KrxxM1749bORJjU0D4Q",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1quCoLtpW0qHVaw8KOErWI5iQ1HKizMpnMKhSTOBWXkt",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1JMs3u94lH5f2mmx2RxjoM8DpZaHhCAtXdZc7cYmDyWd",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "ea144d47619d712dc4e2f10de6a4fa40",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1fPF80a6xLUgdxOQJwJWEexS7wlvtEzXGa52Y1enqSoV",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "55981f6461c0d797c392d0bf15462a01",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
