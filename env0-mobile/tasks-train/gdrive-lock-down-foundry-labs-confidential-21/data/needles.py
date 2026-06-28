"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1dYnNnQ1pf1wfv8kNZSAxpVvRkf5xiGUBwFxgegcM62T",
    "1cCphPhJtLFo9Bql7ohzUIOCW9VzCRUuGc73iYqjQlag",
    "1HE1SNWHI7LyuWRERlyRreDpiaoShancfpzDo6A8yd8S",
    "15LT5CTtc7trPAspk2MSglo5u705bBZwJ7pulOKnZNPj",
    "1vrWgy69PcjpoItv1nwvdmrhDNsNOPe941XfhnC5nrMd"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "8c1c8693bcf7bb6a1f0a94f4ae7c9c94",
    "e9c3629a675101362bd23f31e13694ec",
    "dff3639688f6309ac39f651bc454e33a",
    "ace9c3bc531651b8718d2c175c15a5b8",
    "1517cb75dd4aa29a1dbde0a6dcd38fe6"
]

LEGIT_PERM_IDS = [
    "a1f9c75c7f9bde6a29e732c0c7df4653",
    "2eb68fa6ce797fd51a952b6b2ea7d3d8"
]

NEEDLES = [
    {
        "id": "1dYnNnQ1pf1wfv8kNZSAxpVvRkf5xiGUBwFxgegcM62T",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "8c1c8693bcf7bb6a1f0a94f4ae7c9c94",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1cCphPhJtLFo9Bql7ohzUIOCW9VzCRUuGc73iYqjQlag",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "e9c3629a675101362bd23f31e13694ec",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1HE1SNWHI7LyuWRERlyRreDpiaoShancfpzDo6A8yd8S",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "dff3639688f6309ac39f651bc454e33a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15LT5CTtc7trPAspk2MSglo5u705bBZwJ7pulOKnZNPj",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "ace9c3bc531651b8718d2c175c15a5b8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1vrWgy69PcjpoItv1nwvdmrhDNsNOPe941XfhnC5nrMd",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "1517cb75dd4aa29a1dbde0a6dcd38fe6",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "19qgFXhoZFhZtsMGEm40WhaKNOeOK5tj5D04Rc6CZsxu",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1AUCMCIeZjQUL29juoUPnm3MEeXzaXx67hd2HLFYMpYb",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "14abPNXGVZsGpCEKbWJ0Wm2mE5INCJD6hl8AYkjD8Wj2",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a1f9c75c7f9bde6a29e732c0c7df4653",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1tqm5FHtqGQT4VBCfVj9j6JnF01Ru6hzwAWAWsrhwzDL",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1OvqZqlrkTIrBgfcAKuEZy8TJ1ih9VQ1FgCDqlDrUNTU",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1SIWToXy6k6MS8Lh740kfQE5FoLoIHEcGRawUTNWX2qt",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "2eb68fa6ce797fd51a952b6b2ea7d3d8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
