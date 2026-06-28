"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1PWkvNxGl7q0jpfuUrSMahJ8KOLXqt9jbnLBi2PayNTq",
    "1xq6VefhvRchUTvq0g5TKEMY99fJT25nhPCDltjoE6EB",
    "19abXuGCtTOaFLM1Mw4U0NAfVuGj6oyIEWyHTvvNc9cR",
    "1L1CdTR7ubw3O9k2PSsnloJj8GiB23c2QRQtWNgBqYsa"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "24310198053b4c6dcf03a11623474172",
    "e18d92bf4352571243bd828a212c0baf",
    "f8b116b5b1b26927021d2187a71268b8",
    "73c902f2d440cdfd2f71ec7475e28a7a"
]

LEGIT_PERM_IDS = [
    "54c29f288f20d78490280a50da176943",
    "f932d9ab88aea6564320168a9e394335",
    "36cd6e4daac0aa2b51564b1af1590472"
]

NEEDLES = [
    {
        "id": "1PWkvNxGl7q0jpfuUrSMahJ8KOLXqt9jbnLBi2PayNTq",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "24310198053b4c6dcf03a11623474172",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1xq6VefhvRchUTvq0g5TKEMY99fJT25nhPCDltjoE6EB",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "e18d92bf4352571243bd828a212c0baf",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "19abXuGCtTOaFLM1Mw4U0NAfVuGj6oyIEWyHTvvNc9cR",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "f8b116b5b1b26927021d2187a71268b8",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1L1CdTR7ubw3O9k2PSsnloJj8GiB23c2QRQtWNgBqYsa",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "73c902f2d440cdfd2f71ec7475e28a7a",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YcCNYPneNkqEVjuQnT068EnZbXpSnccdJM6G1Jh1u12",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1qObQqg1KH7xaU6VKGgpX6SyJvRcUC2MSlaDpa14GTd6",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "54c29f288f20d78490280a50da176943",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1JlJjGPzWNVwVdpZWirrG6FoUqwCX3CXTN6zJYq6JUX5",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "f932d9ab88aea6564320168a9e394335",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1OFnAffbMG9hatLyxbPZVhY9YvG8fLN7RdPRZns3he3b",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1AqsGDZKUcz7x8T95bqvt4A8WwBCgmGUU3syiGFFgD6R",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "36cd6e4daac0aa2b51564b1af1590472",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1nqcmaDwuApsumwHON605I8EBfsWSZHmx0WKf27mOqY7",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
