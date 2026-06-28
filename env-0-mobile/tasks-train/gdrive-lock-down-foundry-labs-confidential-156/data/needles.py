"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "135n6M4JrFoOmJ5FLRzfx9XMPlnqX8A5j0hizFAzn1bI",
    "12TcKyLq8IkWRd7YLrOtls41kY2Z01WJ4nMDbFeCnDyx",
    "16LQ51fX1G4ykBrB1ITO6GdB9dTCileemyAU7CI5AZLv"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "8e8212d1606d4f9e6f95b21a54a26957",
    "3c72441da0059b71d3871a766f91f801",
    "c0771e2f4773bf5f90080b8f498f019c"
]

LEGIT_PERM_IDS = []

NEEDLES = [
    {
        "id": "135n6M4JrFoOmJ5FLRzfx9XMPlnqX8A5j0hizFAzn1bI",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "8e8212d1606d4f9e6f95b21a54a26957",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12TcKyLq8IkWRd7YLrOtls41kY2Z01WJ4nMDbFeCnDyx",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3c72441da0059b71d3871a766f91f801",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "16LQ51fX1G4ykBrB1ITO6GdB9dTCileemyAU7CI5AZLv",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "c0771e2f4773bf5f90080b8f498f019c",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1gGISB9DGbcFLXKIjv346sPhnVNWhhN9Ip0NTPjR0c8P",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1jkbTL11V0Kb9QqO8cOMwZJ1cMfjvnPtRTsoMzhPt6zY",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1ehzJL5vR7X32ABEAs0LRwJSQxbNSQzUKqpnzrqBkKMh",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1jgmv0HDgE4XMGrRNsxmsOlY8NDt2h0wr46SXrjecmj7",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
