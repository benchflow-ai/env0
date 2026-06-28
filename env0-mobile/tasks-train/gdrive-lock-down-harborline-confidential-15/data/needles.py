"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1YjIurkUuh9sNsT2ShnPKAyIjQBoDGBM18pi171WtoYt",
    "1VRYFeYFBRQGWWwoAG033yNqGUbWQSxDbw4U5c08djzw",
    "1TKD6ikUpsK82XXb44in29mi04axypBBztNXfpeYRYAI",
    "14AUoRmQMxFMfHQhpPGv35yohAYYZyWvjunHalUJmGeT"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "dde6a77289023739123abe2216f538c8",
    "133a73dbb23e9a8c4c0e2b81e817acac",
    "215cd2620b50d0627a5e33ec917c851e",
    "e382ba6d583c82f94ccadbf9f4967d1d"
]

LEGIT_PERM_IDS = [
    "ea920ae8849a4c08896d3ca0684a680c"
]

NEEDLES = [
    {
        "id": "1YjIurkUuh9sNsT2ShnPKAyIjQBoDGBM18pi171WtoYt",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Harborline\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "dde6a77289023739123abe2216f538c8",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1VRYFeYFBRQGWWwoAG033yNqGUbWQSxDbw4U5c08djzw",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "133a73dbb23e9a8c4c0e2b81e817acac",
            "type": "user",
            "role": "reader",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1TKD6ikUpsK82XXb44in29mi04axypBBztNXfpeYRYAI",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "215cd2620b50d0627a5e33ec917c851e",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "14AUoRmQMxFMfHQhpPGv35yohAYYZyWvjunHalUJmGeT",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "e382ba6d583c82f94ccadbf9f4967d1d",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "11eFlqAMpPod7WziQNIpdfne3NdXPHE4sZTr7KGjoKaq",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "ea920ae8849a4c08896d3ca0684a680c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1vTa2IwpotOXeFGtggoqg3l3oPmZX8TrgcSrWvrYfWRJ",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1wNal18BviSj4LBMgtvlolRlfJk1GkTUmYwPnYhz3R1C",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "16YHUTx4Tpxi1JByuBv2gwkTrr0nXBSdk7aOGNsaCrgC",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 40}
