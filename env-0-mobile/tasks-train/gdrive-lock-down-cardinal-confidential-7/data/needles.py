"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1SLvy2wNXXWrkLNPfQn88fF3uP6tZCvnjrIpbT90gCTK",
    "1lOLmSGBbgYagXrBigx3YEcke6Ch2gRw8iIMTNxT7uqO",
    "1obbehrn00j7YDzsLffqyQDElJNMpzeslpjkEwIV1cP8",
    "1Lwt6sreeyGApo7fUxcTkcZpTg80evSHaFvsO9nLB67U",
    "175vso1fqW8unTXHUObICmu2I3wxZKwTClknh28ZiaIe"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "86e1f543bd3c54fdb63a7a60679e22d0",
    "551fe0d1cb77c45b844308f58461fdd6",
    "03f8d0367c087487dc4aa1a3c962d61f",
    "6352399dbba7ae58a7504f2047be8426",
    "ad007dfadeb6d249fb9450f7d68b0e2e"
]

LEGIT_PERM_IDS = [
    "4af1a681532abe3b6c0e214de80b1783",
    "88b30bb5894286cb3cae63521b8999fb"
]

NEEDLES = [
    {
        "id": "1SLvy2wNXXWrkLNPfQn88fF3uP6tZCvnjrIpbT90gCTK",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "86e1f543bd3c54fdb63a7a60679e22d0",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1lOLmSGBbgYagXrBigx3YEcke6Ch2gRw8iIMTNxT7uqO",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "551fe0d1cb77c45b844308f58461fdd6",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1obbehrn00j7YDzsLffqyQDElJNMpzeslpjkEwIV1cP8",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "03f8d0367c087487dc4aa1a3c962d61f",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Lwt6sreeyGApo7fUxcTkcZpTg80evSHaFvsO9nLB67U",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "6352399dbba7ae58a7504f2047be8426",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "175vso1fqW8unTXHUObICmu2I3wxZKwTClknh28ZiaIe",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "ad007dfadeb6d249fb9450f7d68b0e2e",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "16VT5a0s1vEUWKKpRxgk4OdlHAWsOUdkr2UMO9tM1ZRD",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "174MUoac02a1VNI5KefCBbjkJpj8Uj8eEcv7ivED1mlc",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1dmp9QbmpJV9gldJCANknCoAiN4lG8gfxQoMudd8nyCK",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "4af1a681532abe3b6c0e214de80b1783",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1w9ra8obOMimxeDxWDLB2jd425yICz60v8XDpkuX8nVO",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "88b30bb5894286cb3cae63521b8999fb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1F5dIr4djMPFOylFzUcOj3hiMD1G9i5V1JQUScBHXyh4",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
