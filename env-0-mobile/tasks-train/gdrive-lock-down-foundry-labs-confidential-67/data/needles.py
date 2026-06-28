"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1tixcyDh6T2krQvNiPLlQvBV5Zl01gPkX50VQg0rx5i4",
    "1Qnbtj5ilKl1GbiBxIHQ9hA2Y2H9ogJQvnVx2XzYBEFi",
    "1RH2Q27HNLRBkyacwukkhXjUzk9igdz9HeYameQNAM2O",
    "13k8qNOJQqrVsZTzY6D098iqXxonz6TtwiChCc52DDW9"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "84c97b8ab5815987bb935cf6c71dd6a3",
    "c39652abe312ea826b1362b8393b3aac",
    "7d239faf98e5e2ca7fa6f72e7e7213e8",
    "e7ad2efeb37224cbbf13f505db000c56"
]

LEGIT_PERM_IDS = [
    "acf44a53781d3859402421593851f902"
]

NEEDLES = [
    {
        "id": "1tixcyDh6T2krQvNiPLlQvBV5Zl01gPkX50VQg0rx5i4",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "84c97b8ab5815987bb935cf6c71dd6a3",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1Qnbtj5ilKl1GbiBxIHQ9hA2Y2H9ogJQvnVx2XzYBEFi",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "c39652abe312ea826b1362b8393b3aac",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1RH2Q27HNLRBkyacwukkhXjUzk9igdz9HeYameQNAM2O",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 40,
        "overshare": {
            "id": "7d239faf98e5e2ca7fa6f72e7e7213e8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "13k8qNOJQqrVsZTzY6D098iqXxonz6TtwiChCc52DDW9",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "e7ad2efeb37224cbbf13f505db000c56",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "17ncs6XXp6I09uoo4qlVGkry5WxWvPrs44PtG4ka8d0Q",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1zLKDugIJDaCMEWFTAZ8XTvpvq9xhCAMBe6BjmYrcwIj",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "acf44a53781d3859402421593851f902",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1mN30jo4EONWUpB5N4C6ultVKCNbAAFETBIJIEOgyVRM",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1CUq7vAXphA7ND2Biwqi8IS2ggZjTu3LRLBU8hegxWcN",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
