"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1zO9wIWqnHwVWWygXRDjJjlC2kEPcqSrrd2x0Ka4XfDx",
    "1EdEUjbDStovfNcgtOVex1qJ4NpcRiaYNdwMhwZuiLNx",
    "1rKkharmm18cTfoHjVuLHbZXaXRWZeQ6cvFtD3tjUkob",
    "18PqIxDjjk977o1so5tqKygLRYCfGGZyxBGJcNkpppX0",
    "1QGoJtbRLvV3iYXjbMfkAaTP1SyqrYNYPelFH76pDRlM"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "856be1c2f1c8f404b7b20204e10576cb",
    "e7d489717cbbf38617f180471cf71bdc",
    "038e69c1512aac76ec51f4820b366196",
    "6a46383fd564da2f52db4296a002401b",
    "24d1871deec1c76f56c7f46d83c126c2"
]

LEGIT_PERM_IDS = [
    "a031f79424f1b4288245ecb9854f318c",
    "59881aa13af73ff0fa9b846ad628c3d9"
]

NEEDLES = [
    {
        "id": "1zO9wIWqnHwVWWygXRDjJjlC2kEPcqSrrd2x0Ka4XfDx",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "856be1c2f1c8f404b7b20204e10576cb",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1EdEUjbDStovfNcgtOVex1qJ4NpcRiaYNdwMhwZuiLNx",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "e7d489717cbbf38617f180471cf71bdc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1rKkharmm18cTfoHjVuLHbZXaXRWZeQ6cvFtD3tjUkob",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "038e69c1512aac76ec51f4820b366196",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "18PqIxDjjk977o1so5tqKygLRYCfGGZyxBGJcNkpppX0",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "6a46383fd564da2f52db4296a002401b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QGoJtbRLvV3iYXjbMfkAaTP1SyqrYNYPelFH76pDRlM",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "24d1871deec1c76f56c7f46d83c126c2",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1brPFhIdAM1FKbICqQsjsGfordNZDlTx3XA1az4oOAww",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a031f79424f1b4288245ecb9854f318c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "15BF4moQ2uTxO30WgJbwqZ9MIIci6geouxMnlNOZEwr5",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "59881aa13af73ff0fa9b846ad628c3d9",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1FCSJgeOOMImq88mimEiBIrUflBzBPvLZGCdtKKVZuov",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1791OkLwgBLQO8OUQeeZ41merS8je1PVj37fKeZhf32F",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1jZ4rQTm0onVLAvAicapJMeQv1hNC8TIOSiVlMwfxi9M",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
