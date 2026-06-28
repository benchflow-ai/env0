"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "15rT2Kr0itmwFaG1RpsCelrMUfrWY2xNtlA92bgrJdIU",
    "1Y3SwP5tvOBEyyQsy5h98YqCVQ0K7Cm3UWNBrLPKOeoX",
    "1G3bN0y8pmpoZN58anY1YTv6DkoNqVR0c2Udy1FNaq1w"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "74bce9e17ddb7f675eaf7a6f5d1a32ce",
    "9377310de59c5a2138bdba1434379cfb",
    "05b12eac001468804ca96d9d22231750"
]

LEGIT_PERM_IDS = [
    "a1c10177be5420087b8d0133f6b9131e",
    "7e0a823c3118c779d08c4bcffa1cfe48"
]

NEEDLES = [
    {
        "id": "15rT2Kr0itmwFaG1RpsCelrMUfrWY2xNtlA92bgrJdIU",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "74bce9e17ddb7f675eaf7a6f5d1a32ce",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Y3SwP5tvOBEyyQsy5h98YqCVQ0K7Cm3UWNBrLPKOeoX",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "9377310de59c5a2138bdba1434379cfb",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1G3bN0y8pmpoZN58anY1YTv6DkoNqVR0c2Udy1FNaq1w",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "05b12eac001468804ca96d9d22231750",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1LDd1NKpK13LCaG1Qgv4wVrWCS2XUdvdDpNR14cbOoDQ",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1tpJCnwrY7XKfbfZVpFtBKOm9FpWK5qktETK7YwSnLmV",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a1c10177be5420087b8d0133f6b9131e",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Xi1yVi1jvohc7Lr531wT9oME6BXnxAiryB59dDVMnDc",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "7e0a823c3118c779d08c4bcffa1cfe48",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1TxkxlbzFzC1PNiZ8juyBx0Ww4bf2c4iRVd7Gx9RVUUu",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1BrgT7GB0b58TU1ubPSbfrAOTc9vzGtr0YLgMeYFU65e",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
