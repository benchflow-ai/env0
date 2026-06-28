"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1FQWfW6XxdxzfmXoSCWo6qmGa1wrO925SQN8mx875pKx",
    "1jICZeGcCMYYdy0zB4eaXhtuNoT1GKK2gcT0VyFRPX1H",
    "1vyCUdpFsaUJGJiEUkP8JUwAAFMahb0wMzVe3IPnVklE",
    "1Ht9KTUdx9GwXNlextGUjXxDkEsvAAhGC5q5t3ANWUM5"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "9b1c4811af9b712419ce9aaa0a1358df",
    "a46b2adee86e25d54fc312303c2732a2",
    "6ff9370817beba345bfc15b98cdcfa63",
    "a22ba16c8962abaa89351ea1b9bbcce3"
]

LEGIT_PERM_IDS = [
    "05833a8c9e9b94dff971d8d20c1997fd",
    "eec81c892099395beac5239b3c8ed430"
]

NEEDLES = [
    {
        "id": "1FQWfW6XxdxzfmXoSCWo6qmGa1wrO925SQN8mx875pKx",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "9b1c4811af9b712419ce9aaa0a1358df",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1jICZeGcCMYYdy0zB4eaXhtuNoT1GKK2gcT0VyFRPX1H",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "a46b2adee86e25d54fc312303c2732a2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vyCUdpFsaUJGJiEUkP8JUwAAFMahb0wMzVe3IPnVklE",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "6ff9370817beba345bfc15b98cdcfa63",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1Ht9KTUdx9GwXNlextGUjXxDkEsvAAhGC5q5t3ANWUM5",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "a22ba16c8962abaa89351ea1b9bbcce3",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1i93NNgns0VPGDtbOAG1NGRBixbOMqcQ5jjTezjhZQRI",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "05833a8c9e9b94dff971d8d20c1997fd",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1NbGrlnqAhRivatwAvADW2axKp8JmXGM4K325uRibldA",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1JcohNT59VWDPXD3Xlp1VN0NOtdrXTeYP7ue77jRrbVe",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1mvujGSPgZYHTdKDfuzxlKfk53iI6Oyz78TjKY2fG86Z",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "eec81c892099395beac5239b3c8ed430",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
