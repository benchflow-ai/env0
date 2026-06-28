"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1oLGOXK8c7UPdhACu8ebhcTIHjkoEpSmclRa5vWFahRt",
    "1BUkwoEAENhUn5qzIJjyYpG83GpKqNppV0qqPCoR66bi",
    "1Ip1pFOIMcgQG3M1cP5WsWDaS2PlcJMeiqlUZMH7NwD8",
    "1P0BJNVOHPBmqo7MX2BBjwBOKKfEEm1CaaPZ327HqW8L",
    "1s2sXG0YgpnId916McAWLWzOkkjHWmEBZlcRH43Tqaw2"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "6c703bb23015e922047fb4c8140d32bf",
    "ba50f91aac169a081662a3928ef7bd08",
    "1697a1a0d06372db7e2d8a961f9beb89",
    "a58f801f53d3fc08ad240b6444cbb3b5",
    "af948ca7601182d7a175276bf06a00f6"
]

LEGIT_PERM_IDS = [
    "9e3a7051a429835e1fa72ea2e8b8e7d7"
]

NEEDLES = [
    {
        "id": "1oLGOXK8c7UPdhACu8ebhcTIHjkoEpSmclRa5vWFahRt",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "6c703bb23015e922047fb4c8140d32bf",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1BUkwoEAENhUn5qzIJjyYpG83GpKqNppV0qqPCoR66bi",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ba50f91aac169a081662a3928ef7bd08",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Ip1pFOIMcgQG3M1cP5WsWDaS2PlcJMeiqlUZMH7NwD8",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "1697a1a0d06372db7e2d8a961f9beb89",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1P0BJNVOHPBmqo7MX2BBjwBOKKfEEm1CaaPZ327HqW8L",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a58f801f53d3fc08ad240b6444cbb3b5",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1s2sXG0YgpnId916McAWLWzOkkjHWmEBZlcRH43Tqaw2",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "af948ca7601182d7a175276bf06a00f6",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1pjlhvRQn3lSgD0QP0OFC1tpxN9UzAZd9Qz1uIMNwfwB",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1NCOXDdwagVRePIbM6Q6tKBAiLXOuzZLjSFitQyMl6pA",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1d96pKpJjSdO7jhoapUV3mYGE2fUTcryIMxGSs2MGFD7",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9e3a7051a429835e1fa72ea2e8b8e7d7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1kh2eygi8ZqeSvnYo18cnZee0hh6gKDZJDNJ7C8EKNYq",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
