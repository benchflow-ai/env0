"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1WBBexnFSus8CqrUjuy6prdI0Kkrx4udj1gMjlX8mw5I",
    "12zzBUrtaQZFdi0sAKclx4WjXtnKU8uQEd0kCnOrpMkU",
    "1B4piR7ktxCps7Ca9H3pz2YjnMnMi7QAM5S5fUVfIWA8",
    "1HL3679QIsmXO8SST0hS7gCHFuSeLLUWUj68MwYMRBW7",
    "14sjUAf2mTGRowzcz2PcxPiKrhLAyKXhOkQDcsDed2op"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "c208f6bade4766821fb39e34e465235d",
    "d0b53e05b10b155f06c2736db57f6710",
    "c82bf957904e2745745b72cd4e8da8ba",
    "e3cfe4ca7dc3ac7eea89caad325daf1e",
    "1afcf66734306180466d33f7c36ad83b"
]

LEGIT_PERM_IDS = [
    "dd4f8583cada3169d90d568d89187c2b",
    "27fcedf7a22ab327ef9c9ee6e595a354",
    "88269ef9e8f5d5f3b87e4858bfd350e5"
]

NEEDLES = [
    {
        "id": "1WBBexnFSus8CqrUjuy6prdI0Kkrx4udj1gMjlX8mw5I",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "c208f6bade4766821fb39e34e465235d",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12zzBUrtaQZFdi0sAKclx4WjXtnKU8uQEd0kCnOrpMkU",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "d0b53e05b10b155f06c2736db57f6710",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1B4piR7ktxCps7Ca9H3pz2YjnMnMi7QAM5S5fUVfIWA8",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "c82bf957904e2745745b72cd4e8da8ba",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1HL3679QIsmXO8SST0hS7gCHFuSeLLUWUj68MwYMRBW7",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "e3cfe4ca7dc3ac7eea89caad325daf1e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "14sjUAf2mTGRowzcz2PcxPiKrhLAyKXhOkQDcsDed2op",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1afcf66734306180466d33f7c36ad83b",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Qq1nBQrPLpsOaeLbxmAiWEBP0gr7A7GYYMX3ApOibWN",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "dd4f8583cada3169d90d568d89187c2b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1LJNt7OO89IdJp9ACxaXPHaS1YUB2otgWBdnMBny281E",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1XC05QNf5HBcNDeiABzenAYY6MIDGzYnfoshfu1mnUkN",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "27fcedf7a22ab327ef9c9ee6e595a354",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1LqEEZiEjlSnei2u28SSUJ2r7Ua4soY2DUlMOjo6XSwf",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1x7sqDhTs8HhyWY5kxYAsKLLVi2uM66VfKZbKs812zHL",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1oR7pVPNXXD1RmV2OjoSNgjmURMgcVYusgfE4QRDrZkf",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "88269ef9e8f5d5f3b87e4858bfd350e5",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
