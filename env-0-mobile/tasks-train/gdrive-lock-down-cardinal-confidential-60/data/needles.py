"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1w1eETbQsMQC65Kqtj8bTiW3iQSteM7sOpFHcGSORgKE",
    "1MoBosPAmZluB5VxBZnVeC5qLUsBkCqYkyKxBpoA8Kaq",
    "1MChjVFxP0DGeEwNAaKudnV4ocbI7PfmOlKDsE0RPl95",
    "1xhhu3iIzjMYOHTgOYbzhmWUX8luOedbijEJT769UGPe",
    "1rUDoP2tEq8nrVIeoLidlrvrAet2i5QTvTWHaSphtAjI"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "02673894898bca713de297a70eeff4bb",
    "5ab2d2025abe4f6dafb31e3dd30d2faf",
    "7885641fec674ffb99399f65266648e1",
    "2d4f1efad1d266564ae45860da46a92f",
    "3d00afc2f7f24e5beb3ab88035ccb2c1"
]

LEGIT_PERM_IDS = [
    "a80586a49b84e8750de7822960239a7e",
    "448fe45d105e1825380219b3fb4b981b"
]

NEEDLES = [
    {
        "id": "1w1eETbQsMQC65Kqtj8bTiW3iQSteM7sOpFHcGSORgKE",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "02673894898bca713de297a70eeff4bb",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1MoBosPAmZluB5VxBZnVeC5qLUsBkCqYkyKxBpoA8Kaq",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "5ab2d2025abe4f6dafb31e3dd30d2faf",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1MChjVFxP0DGeEwNAaKudnV4ocbI7PfmOlKDsE0RPl95",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "7885641fec674ffb99399f65266648e1",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xhhu3iIzjMYOHTgOYbzhmWUX8luOedbijEJT769UGPe",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "2d4f1efad1d266564ae45860da46a92f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1rUDoP2tEq8nrVIeoLidlrvrAet2i5QTvTWHaSphtAjI",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "3d00afc2f7f24e5beb3ab88035ccb2c1",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1u7MtGj6K68ygZeNVxvNgcXMofWO4qxMNuxG3ddndOnK",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1Q9DKamWT66QGNawKnGS1zJ0nyqeEodEMT0GEtUYCBsn",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1ominTY8Ysxcy11HBpC63MbiF363ydGo9RMGOXTLC9gf",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a80586a49b84e8750de7822960239a7e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1FkT25ErY0DQebgFwgvFhSB0dFzs9qFXOIF4qRIP6PHu",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "448fe45d105e1825380219b3fb4b981b",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
