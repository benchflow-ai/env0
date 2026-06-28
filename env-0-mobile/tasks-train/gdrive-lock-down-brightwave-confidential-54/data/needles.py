"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1ALJh8F7z1CneEaUgOCdo6AOlN91SW0nblDHNKI1W8N3",
    "13vJTAgX6u263ubC1sPNgM9Qu8ytkKELZ0MthhitK7sw",
    "1lrIhsbW0LL4H4MXOQFz6oIEFugMGoxnc9Dah8fRMoWh"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "48c3a7080be781d04a4b66613f664c7c",
    "d79f93d3abee1ddf0b34123981f28214",
    "4e1f08efecec75bfdaae704ec43dc739"
]

LEGIT_PERM_IDS = [
    "bc39ae70a279f1b0000f0416a6639a82",
    "e6f47b913843ca2c3dde275129da87b7",
    "ab246388456ed1152114bfadcf4cff76"
]

NEEDLES = [
    {
        "id": "1ALJh8F7z1CneEaUgOCdo6AOlN91SW0nblDHNKI1W8N3",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "48c3a7080be781d04a4b66613f664c7c",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "13vJTAgX6u263ubC1sPNgM9Qu8ytkKELZ0MthhitK7sw",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d79f93d3abee1ddf0b34123981f28214",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1lrIhsbW0LL4H4MXOQFz6oIEFugMGoxnc9Dah8fRMoWh",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "4e1f08efecec75bfdaae704ec43dc739",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Oxja9FZIugTyg9YfsUDFAInhW4YqDUyZ4aXSVpMfmBI",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "bc39ae70a279f1b0000f0416a6639a82",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1Nkb99LBTN25bOpvnZmuFgFewFj6AnxLEDlWgLjCnxcz",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e6f47b913843ca2c3dde275129da87b7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "13nQamGuTmqBjogp0Qo3JoggY6BpwuR7BOKtXRGnvLo0",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1s66rW3yFCnQ1jBIHPp67W3f1FBrD7oPCr8vQrfsnMnl",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1PFcSGUKDgeWsZLbjGoHeFBvGgbFz0I51NYPUJxwNPwj",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ab246388456ed1152114bfadcf4cff76",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1h0GJCfckrDFJf4pNBkqsldzT9peCRsPFrNKbYV7N3R8",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
