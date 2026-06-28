"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1XJczWsNh1trzT4jpkeYDbYQ8H2vlyJBBPMTDmICzPqc",
    "1Kji7cqAV14cMs0hxPI3lBuxvkrzmwKW7uwiwubpGFCA",
    "1wT2PdgkLwL9UJ11awBYVUMPxDSGk0GyRiB2uvO6Zym4",
    "1ElRTBcYbpi9MGU2NqTIarj8Zx8BRJxJwaxEdn40aA4T"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "7f218911d82b6ff1b121f7ec7aa97300",
    "7e15408a1d101017d0131d22e4475408",
    "5dae25622617ed08f9ff161b9b5a7d2d",
    "7cc63d49cf1b7ebb3c2b40776607642b"
]

LEGIT_PERM_IDS = [
    "fc5ae7746e75d0c47ada88a07eb01c4a",
    "fefaac051546d0e0d111b5bf7d502e47",
    "1555a512d74267e755e4db551a61c9f0"
]

NEEDLES = [
    {
        "id": "1XJczWsNh1trzT4jpkeYDbYQ8H2vlyJBBPMTDmICzPqc",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "7f218911d82b6ff1b121f7ec7aa97300",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Kji7cqAV14cMs0hxPI3lBuxvkrzmwKW7uwiwubpGFCA",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7e15408a1d101017d0131d22e4475408",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1wT2PdgkLwL9UJ11awBYVUMPxDSGk0GyRiB2uvO6Zym4",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "5dae25622617ed08f9ff161b9b5a7d2d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ElRTBcYbpi9MGU2NqTIarj8Zx8BRJxJwaxEdn40aA4T",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "7cc63d49cf1b7ebb3c2b40776607642b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1U8fdchRd8F59wiJaNVlWEK1GVUUQsCz8ysuFCF3xl1r",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "fc5ae7746e75d0c47ada88a07eb01c4a",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1XKqGwIfjR3xWKFkgul6PQJfbicFaBYGlvfmDfzBOehD",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1WSxI4zJtAzBp2NZV24IXd3H3RscZGothF69UJjZYodQ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "16cqf16Wo2eW5mRyHj7wSvJiOmfgCfOq7xyHMRNwailM",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1lZWSU5vLUHUGlUCzZo1CugF8gDaFnKRmB1JQBovYGpL",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "fefaac051546d0e0d111b5bf7d502e47",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1i9gqHYFIhHCFdq8Ms7QXBzL4KT9kTi3pfbl2QLMrmnz",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "1555a512d74267e755e4db551a61c9f0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
