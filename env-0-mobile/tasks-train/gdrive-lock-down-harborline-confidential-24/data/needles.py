"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1ClLjhbkjiG4yZycFnbl4NtkQFiSTlpldPEJv5biHKdH",
    "1J9ksAIulCyUQExgTGwPlrDDibeNriVHZOlJc8zBNCRJ",
    "1Q8WKDDSO9ChO0MuTtV08i88as7mGbDluyHjE4ynjBd7",
    "1KJlVgD3fnFJJQOsh0o27SSgbDTVgESI0xS9L4myaims"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "59187f650606003b4bb52d75abd8d2a1",
    "0bef4be0481e229099aad0c301bd65c2",
    "ec6d84ac4bf777f3a1bc756d9d079b47",
    "883f307edaeff87a9c3833b007475a17"
]

LEGIT_PERM_IDS = [
    "e7e505491f7605fec26ceedba048b312"
]

NEEDLES = [
    {
        "id": "1ClLjhbkjiG4yZycFnbl4NtkQFiSTlpldPEJv5biHKdH",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "59187f650606003b4bb52d75abd8d2a1",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1J9ksAIulCyUQExgTGwPlrDDibeNriVHZOlJc8zBNCRJ",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "0bef4be0481e229099aad0c301bd65c2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Q8WKDDSO9ChO0MuTtV08i88as7mGbDluyHjE4ynjBd7",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ec6d84ac4bf777f3a1bc756d9d079b47",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1KJlVgD3fnFJJQOsh0o27SSgbDTVgESI0xS9L4myaims",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "883f307edaeff87a9c3833b007475a17",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1BmZKhwE8N9OAudWyEnD1lrqVWO7QpwAk1jmIsOsWCi6",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1dceUzwE2U8G8LKj93S9fUlxJrHetaqbgU7uiQCLxnQF",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1y9daHCniSMfiRa3p3YK2V5qNQuuj5TEd3uoxObRqOfA",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1nGJdpOdPZTI1kjydN6G0PB2TESywO0pCB4AsC8hoSy1",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e7e505491f7605fec26ceedba048b312",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1vKny7WHuEmREc89BulgWprYG75OFkWs4BCHJitMgr9d",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
