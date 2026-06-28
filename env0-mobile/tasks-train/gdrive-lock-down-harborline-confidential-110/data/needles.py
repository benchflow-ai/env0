"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1VHlNxHyjFjE81Y6ADJaJ7cKEPtjoXasublcTfduqpGt",
    "1uHrMMzYCBqA7tmY3m35IZlCWlBWm7dMLOOKzWN0YCFO",
    "1UrCEyncPo281butyw5m8MlDppfXcQcrWIoMrrhO9S2M",
    "1LrzgIXeJBPjlJwb23Z7CFs1NEKUnFzWgXkr2BgVvU14",
    "1dea3BBXH1oECV6rA9winrxI02irJle9WksLXcTWK6J4"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "5860bf023ff20caef0a5035e4c382c11",
    "de5c63e87ef47745c4cece24fa7a269b",
    "5af366c9149467778d5745a3dfaa4da1",
    "3f81d2cd691b69db621e57bc9c8e817e",
    "2d85ec9134cb8951d9a306b576d0464b"
]

LEGIT_PERM_IDS = [
    "d6c6bfc46fa8420a88b1512aec1e7b7d",
    "418c40f02d716d1f455f6bd71f9566e7"
]

NEEDLES = [
    {
        "id": "1VHlNxHyjFjE81Y6ADJaJ7cKEPtjoXasublcTfduqpGt",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "5860bf023ff20caef0a5035e4c382c11",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1uHrMMzYCBqA7tmY3m35IZlCWlBWm7dMLOOKzWN0YCFO",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "de5c63e87ef47745c4cece24fa7a269b",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1UrCEyncPo281butyw5m8MlDppfXcQcrWIoMrrhO9S2M",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "5af366c9149467778d5745a3dfaa4da1",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1LrzgIXeJBPjlJwb23Z7CFs1NEKUnFzWgXkr2BgVvU14",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "3f81d2cd691b69db621e57bc9c8e817e",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1dea3BBXH1oECV6rA9winrxI02irJle9WksLXcTWK6J4",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "2d85ec9134cb8951d9a306b576d0464b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1JEVrxtNLNlxLW4v8LKISgXrPkTC14YYk4pwuFYkps4K",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d6c6bfc46fa8420a88b1512aec1e7b7d",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1urxcfxHdyrg3Qv88KBebBOM8ZxbAOA7dMC9u1PkUjIB",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1TexXnDM2zyP0ZB9NBjHiXrHkg62K3mXkQdx9B8Kfej5",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1j2FlWt521TD6uhIVoRC7uh45fpzUtubqwDXHo6Mad9E",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1WivvRWqfVfnOUvB5rMklTnQpwshiTvdbzm3eFFIcRNE",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "418c40f02d716d1f455f6bd71f9566e7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
