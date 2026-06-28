"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1AvecIVtpKyt0m0fdXYTgoNqWrPBTagOk6GVjSMT4Zs9",
    "1IedEzHprIrUvY8kUGmgrscab39mG9dvV9EskI2SyXP5",
    "1x0bGumJ8ZGl608T1JtUTr1AkJ2S9zTh0e8rNYIo3Pp5",
    "1w5KxYRXeU9ThAm08H38wg1wFamkLMak27I7TAMpQMNn",
    "1WA2RqmAJwt3ix9ErFVG12XnAUwCKqEDUzDM68eJLNhS"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "d82035434c1b817cd5cf5242ef35463d",
    "42511cf94a1742de96733b76c05e49ed",
    "c81142dabe38e49131addb1d4b684848",
    "3d9a3eef5a67d7289d2b01f5ec812900",
    "91187497bbbe2b324697ebd48050b708"
]

LEGIT_PERM_IDS = [
    "2ad87c3be27b221161c2080ff87a28ef",
    "d674611f1a92d696e72c9de69de127a9"
]

NEEDLES = [
    {
        "id": "1AvecIVtpKyt0m0fdXYTgoNqWrPBTagOk6GVjSMT4Zs9",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "d82035434c1b817cd5cf5242ef35463d",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1IedEzHprIrUvY8kUGmgrscab39mG9dvV9EskI2SyXP5",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "42511cf94a1742de96733b76c05e49ed",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1x0bGumJ8ZGl608T1JtUTr1AkJ2S9zTh0e8rNYIo3Pp5",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "c81142dabe38e49131addb1d4b684848",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1w5KxYRXeU9ThAm08H38wg1wFamkLMak27I7TAMpQMNn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "3d9a3eef5a67d7289d2b01f5ec812900",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1WA2RqmAJwt3ix9ErFVG12XnAUwCKqEDUzDM68eJLNhS",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "91187497bbbe2b324697ebd48050b708",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1spxCJWK17SHbNrySLdJQ34YRppORcjs9R7R1Kr82lLo",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1o2khu5eekQbbfVBBLv0xEZ5ENxUJHNKmV0bLKjG7O27",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "2ad87c3be27b221161c2080ff87a28ef",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "19nWmAayJh4NZmV9Nw2T6KItyyEfu12hzi54NyI2ndJA",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1iq7jPHeI4hbmhtDLde11dw4qzHJhHOgOKfWTImPxKdK",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1lvslaaVFkeqUuVmYHVAujWGDsGgp5CdtmmParoZDS6Y",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d674611f1a92d696e72c9de69de127a9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
