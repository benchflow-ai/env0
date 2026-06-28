"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1MG3czN7O6IJk4Zuq4GtGn3TydCDcR28COn8Ieh8ESMP",
    "1ho9UOYX5fd5eUNrWhC5ArG3knH5TVRT7Kht3w89CQzO",
    "1gjcpM6CjcS9xdkd0jn2H7vHUsxl6qS9KE3mI0ZNLPaj",
    "1IfCrt3rUpQXxYWatHTZjdyEdIgMjyIlKapbHpTU2qXI",
    "1aN3WHAW5GeUHIe7GfE6LRhLdHAjoZuAD5Q07xRlCgpu"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "23add09438ace72fcf79d4c7ec390118",
    "0ac334b41af3accf0258d444a7ccaed9",
    "cdd4923319deefdca8e2c7a2961021fc",
    "599ecf6b0d271cf7e351825552f939ac",
    "79bd82cee81f30367aa662a44a63d694"
]

LEGIT_PERM_IDS = [
    "d8630324581cf9bf98937a629c787829",
    "2814e7c6670c36f456b3f67952779726",
    "e3acebccc0473d36d9115ad8f6a25966"
]

NEEDLES = [
    {
        "id": "1MG3czN7O6IJk4Zuq4GtGn3TydCDcR28COn8Ieh8ESMP",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "23add09438ace72fcf79d4c7ec390118",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1ho9UOYX5fd5eUNrWhC5ArG3knH5TVRT7Kht3w89CQzO",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "0ac334b41af3accf0258d444a7ccaed9",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1gjcpM6CjcS9xdkd0jn2H7vHUsxl6qS9KE3mI0ZNLPaj",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "cdd4923319deefdca8e2c7a2961021fc",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1IfCrt3rUpQXxYWatHTZjdyEdIgMjyIlKapbHpTU2qXI",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "599ecf6b0d271cf7e351825552f939ac",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1aN3WHAW5GeUHIe7GfE6LRhLdHAjoZuAD5Q07xRlCgpu",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "79bd82cee81f30367aa662a44a63d694",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Y7H7tkzJcNHHxgefaOjUDyPdmd5u7wbtHcn2guqGJSp",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1jEW0NIEdg06NKGBTSuHwRa9y3lTX7gda202nWxLUPly",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1BBCtJiEP3ii9xQ9PmFXCcitSXzBKhqdiJGOasDlnvwJ",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1HmElNQAIG0RIcBj8RwFnR9xIZZ3jPiHufeS4hCjEAIx",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d8630324581cf9bf98937a629c787829",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1GHqT39UC17WtNryKuo17eOelIEGS7lQw3MsHYF0Mqyr",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "2814e7c6670c36f456b3f67952779726",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1ShK2EpuKY3Vuxe6jRNl12ZZIFM3ff4EDoY7WstxnWz6",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "e3acebccc0473d36d9115ad8f6a25966",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
