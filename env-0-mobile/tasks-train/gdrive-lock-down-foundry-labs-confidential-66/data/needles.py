"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1BM1hmBRtA87r7y1SYADilfFMRFw0RSMuLVQHFGZjtLr",
    "1rA1634NagmfD7cmKTzrj5YKJWfAZgp1hEFmQc7ygIMd",
    "10MAtPJfiYKChduZ6nl9mznmcmWc8SLAjgDBHwTYcJzR",
    "1WP7z25hvH3xLWugikC8KkQyWamA0cFXw0jNwAS38CE9",
    "1wf4YolzU2bPKqC6T1qyCP38wt6tnpDJJEndy2lkZRL9"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "6d6b5335c876b578f15000126a784cbf",
    "ad658cff8b72916138b54d083055c601",
    "9edefacbb804a6f862baefcd0a2b560b",
    "dd4dfd8f8ab9992339123061d04258a7",
    "ce9446701a53fe0e4ca75421ff519f2b"
]

LEGIT_PERM_IDS = [
    "22b2eb68cba900da281583fed36dd058"
]

NEEDLES = [
    {
        "id": "1BM1hmBRtA87r7y1SYADilfFMRFw0RSMuLVQHFGZjtLr",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "6d6b5335c876b578f15000126a784cbf",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1rA1634NagmfD7cmKTzrj5YKJWfAZgp1hEFmQc7ygIMd",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "ad658cff8b72916138b54d083055c601",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "10MAtPJfiYKChduZ6nl9mznmcmWc8SLAjgDBHwTYcJzR",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "9edefacbb804a6f862baefcd0a2b560b",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1WP7z25hvH3xLWugikC8KkQyWamA0cFXw0jNwAS38CE9",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "dd4dfd8f8ab9992339123061d04258a7",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1wf4YolzU2bPKqC6T1qyCP38wt6tnpDJJEndy2lkZRL9",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ce9446701a53fe0e4ca75421ff519f2b",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1j5K3ry2O4G5TLnFDRE9gCBoQCaQU4e9hUZeYzvBheek",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1wcUu4MonMAdrGxOWj7JGyFBe91sTQq5ucIU6Ghc4Pde",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1LoTmEFRxAo2vyG2ZrF8DM4fvIe6ybiSXi2u33ghUIfF",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1XbDsFrzDxMkB2YUYWHOf534fFX5G7L5rzvtUWZ2izdN",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "22b2eb68cba900da281583fed36dd058",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "19Ka0AWgoHTRaENH8o2XLJRTWEyO1JUYO6dT6oMPvWqX",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
