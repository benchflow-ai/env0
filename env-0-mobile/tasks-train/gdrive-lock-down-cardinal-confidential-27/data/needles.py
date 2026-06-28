"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1VCqETCfUJYk5Y86fxEr36BJZdF1u28MdHIoq1rEGAGm",
    "1iR6QKmXfAUX4PuTC5BwssqE8H5jyx5Rg7gxm5suupHU",
    "1LHm6eYza2sCwHY7UVG014P3vNhR29BGcdazIC6bNHR9",
    "1fN0DQvXwZMe69PfFYrihBzib6ASZTOpDW8sSy51w0iv"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "4ec79cb85fa43a55b14392a1a73502d2",
    "5672dd02eb1c526e4c0438623ddbd19d",
    "caaed9274d3e4e599be2bd4dd707c61e",
    "cbef878c8dcd17bfb553f270d0d5e903"
]

LEGIT_PERM_IDS = [
    "ec0b4b21407079386603c875db2e0507",
    "9de02b871b6c0cfd3e32416981fc871f"
]

NEEDLES = [
    {
        "id": "1VCqETCfUJYk5Y86fxEr36BJZdF1u28MdHIoq1rEGAGm",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "4ec79cb85fa43a55b14392a1a73502d2",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1iR6QKmXfAUX4PuTC5BwssqE8H5jyx5Rg7gxm5suupHU",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "5672dd02eb1c526e4c0438623ddbd19d",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1LHm6eYza2sCwHY7UVG014P3vNhR29BGcdazIC6bNHR9",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "caaed9274d3e4e599be2bd4dd707c61e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1fN0DQvXwZMe69PfFYrihBzib6ASZTOpDW8sSy51w0iv",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "cbef878c8dcd17bfb553f270d0d5e903",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1W5uBQXgkyuL79Genawjn7D2aJ72kRDNIfKCIeXCHC2M",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1JqviU78P4Yv7Vx1FQdw8KLT1kX6CgNieh1CyW2veItC",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1UltKPWCy1arNKYCrX836S6rNzKtC56AUpS1zbydkMkq",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "ec0b4b21407079386603c875db2e0507",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1qAG2HoWDvXn4R5BHUXu1RnkeDdQNZb0IxJQMsBETiSt",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9de02b871b6c0cfd3e32416981fc871f",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1tu3djrVUzKw6q0zmSrDFDuBYKCsTAm1uWPTUJxSeN9a",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 40}
