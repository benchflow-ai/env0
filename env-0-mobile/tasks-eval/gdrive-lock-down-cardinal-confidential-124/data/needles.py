"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1T1GOFdvVYaOWE0L2PcJid95oNE8j1Br5Uqip9HjLHTa",
    "1IomeR0DAtjgRkZpvATgYtOEl4M8gZtVz7SWIQTbyybd",
    "1MOXrrPRj5fueYwz91uPzLyrcZYuIawTjhBpDLthwCv7",
    "1Pdq9P91GKtPJiJlDVxjWI6Wz5yTpn6ndXlbF1jmDOBN",
    "1LZyBZOYIC50uiE50cByLjEyvvqSJsmmq8DpMTyeAxcL"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "b937354d75f73e6f979e45fa84ad6aa5",
    "c96290d7e7a8245626087378ac526b92",
    "186e3c7b2b2a9ee8994608c677c77296",
    "625f71ee2c035a2c8b9ba6f5f9e53753",
    "cb5b5712394ac9b0f346b06fcda27ef1"
]

LEGIT_PERM_IDS = [
    "0bd6111601fb15736efb783d640063b4"
]

NEEDLES = [
    {
        "id": "1T1GOFdvVYaOWE0L2PcJid95oNE8j1Br5Uqip9HjLHTa",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "b937354d75f73e6f979e45fa84ad6aa5",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1IomeR0DAtjgRkZpvATgYtOEl4M8gZtVz7SWIQTbyybd",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "c96290d7e7a8245626087378ac526b92",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1MOXrrPRj5fueYwz91uPzLyrcZYuIawTjhBpDLthwCv7",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "186e3c7b2b2a9ee8994608c677c77296",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Pdq9P91GKtPJiJlDVxjWI6Wz5yTpn6ndXlbF1jmDOBN",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "625f71ee2c035a2c8b9ba6f5f9e53753",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1LZyBZOYIC50uiE50cByLjEyvvqSJsmmq8DpMTyeAxcL",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "cb5b5712394ac9b0f346b06fcda27ef1",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1GjmqVzYbghnUBihpKVrgVxPDjmOhCoX9e4LReCkvJRf",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1r7cFx0Jcz2gatxibnnTd8YCzo3rN8ZvST0OACt4Gp27",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1lLyMtvfcbPFsjwp5jQIAa8jtUbUQjy3nhBOyH3qw54h",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1ExBbWrDychnwa3aH5Jo5TvnoiK3YkxLnNFrHZgXhzQX",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0bd6111601fb15736efb783d640063b4",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
