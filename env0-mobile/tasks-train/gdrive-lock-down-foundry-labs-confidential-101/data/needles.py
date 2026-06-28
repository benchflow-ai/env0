"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1SwxJoJgHhUjR5f2RMrLFaRdmPOZvJnYJ93UiZUDjWLa",
    "1mPTREpDPOBo7K3MN08HBFjxpIUoFcp6XAn1ZRznTBQm",
    "1HVPpJlEVUNi8Py7zRAkap0XmEh5Dy1l3jGNc5eatHOH",
    "1cc8tDoEDtjS4TXu3KdFYSWs6Dpx4L1pfloNVogfiees",
    "1qeAoiVIJSYZ63bU7sY0GizfWqnW5hiqA9gL3U4WeasQ"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "ba391731b9f9d7f27a98a0c4bef3c647",
    "41e688ab069bfcf6b22575e392462411",
    "d1abb9dd2d9b1eec69c9e71f1d1f3b59",
    "7e382fd8006a70c033cacccc80c37df4",
    "6194e1af6a533214d372a92b5acdac46"
]

LEGIT_PERM_IDS = [
    "c5a431006ea0448c3a1f6b80a37ada6e",
    "e40ce38e0f4c3e019f88496c396ab36b",
    "dbe187d9a2398a76940439ce0cd068cb"
]

NEEDLES = [
    {
        "id": "1SwxJoJgHhUjR5f2RMrLFaRdmPOZvJnYJ93UiZUDjWLa",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "ba391731b9f9d7f27a98a0c4bef3c647",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1mPTREpDPOBo7K3MN08HBFjxpIUoFcp6XAn1ZRznTBQm",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "41e688ab069bfcf6b22575e392462411",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1HVPpJlEVUNi8Py7zRAkap0XmEh5Dy1l3jGNc5eatHOH",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "d1abb9dd2d9b1eec69c9e71f1d1f3b59",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1cc8tDoEDtjS4TXu3KdFYSWs6Dpx4L1pfloNVogfiees",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "7e382fd8006a70c033cacccc80c37df4",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1qeAoiVIJSYZ63bU7sY0GizfWqnW5hiqA9gL3U4WeasQ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "6194e1af6a533214d372a92b5acdac46",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "17EVCPzmOscCboFoMAQuio9y4pWGof3qdqm49BOmn1l8",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1vnYN0yuEC06j3kOytGWMYmxo5wq1jBrRKDiG47B3tmX",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c5a431006ea0448c3a1f6b80a37ada6e",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1QfkANMEG9B5GR3woGsJg8VW3EPE36ynYcY8dGFgeU4u",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1KOFLAv9IdsU9LBlSg8dhmSNf1HTPoBc2RVJshciIMRq",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e40ce38e0f4c3e019f88496c396ab36b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "144yXfpnIfrPiwze8TLejUKGFGLTmc0Z2nW2Q32rZ4IH",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "dbe187d9a2398a76940439ce0cd068cb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1l44vwlE0gLdaAivNWTyPuVoadVsRMOQ4mGE3LmqOWeM",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 30}
