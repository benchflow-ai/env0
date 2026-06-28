"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1fpmSasQhzRd6lBWIHYw6k0aQDaI3kiUxYjXFZaUOKyE",
    "1KZVYvlQ6oLdCAyKiCn52tllfCogMsNdGwLKBtkmvY65",
    "1iVAwkuE3SnNgnTooWPw4b6YTSrRDI82TDJF9cXbmn3u"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "2300a4c7b3d2cd7cc89e94c1da111223",
    "bb2b29fb54c03255fa3cdb532db57689",
    "ab73814ee2cf62a90fcd8c064c6b70b3"
]

LEGIT_PERM_IDS = [
    "c3450694ba60f75135656dce8be3f688"
]

NEEDLES = [
    {
        "id": "1fpmSasQhzRd6lBWIHYw6k0aQDaI3kiUxYjXFZaUOKyE",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "2300a4c7b3d2cd7cc89e94c1da111223",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1KZVYvlQ6oLdCAyKiCn52tllfCogMsNdGwLKBtkmvY65",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "bb2b29fb54c03255fa3cdb532db57689",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1iVAwkuE3SnNgnTooWPw4b6YTSrRDI82TDJF9cXbmn3u",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ab73814ee2cf62a90fcd8c064c6b70b3",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1jxa1PJEH4OvGGvgXU8SZhKPx2tUISNH7fVSJzjenA1A",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1ztAlNES136WY4YTirA7Bep7PxTSKxBZlX0SMAG4B4Jl",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "c3450694ba60f75135656dce8be3f688",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1J0isqOmyVa4LcnM3wnq3ls7jHrZADaEDeWDOzfFx0kq",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1tQXlO7jzHiY2JE9azlZUDICZwoTEdLjuyhmetnUahIS",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
