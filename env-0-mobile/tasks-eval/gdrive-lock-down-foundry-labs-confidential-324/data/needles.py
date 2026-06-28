"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1W21L03FfYXJp3PH2Tl8YJU7z2MzgPdhVTD2P3wAoiJ2",
    "1x1oMh1QjMFnuH8YQ2U5j0zfcVRULx4cdEjbHI8GK7jm",
    "131Aec8RIMn4Gj2LMpwuXcVJmRkWF5uKtE01Tl8S5MQX",
    "13ruec5XoRYnvvxRfgMJPMuuNutLi9vUukuk8LbBiAE1",
    "16FZyDnIUefzfStMH9kxdVr8nrxysA7o6m48WQVQAU89"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "prod-secrets.env",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "061238ea46cb1b6c2802bc46041d6085",
    "ca923a33645018f34cd1baaa684e12d3",
    "5c87f776f5e7a9c8aa7c212615d44feb",
    "de81cc37c95970f73acaf29a27334374",
    "a75532509790aff937c8c8d291788f60"
]

LEGIT_PERM_IDS = [
    "e3ac7c19344e64650fa2b4a2913dec77",
    "374d782e3ec376d27194fef40ef73687"
]

NEEDLES = [
    {
        "id": "1W21L03FfYXJp3PH2Tl8YJU7z2MzgPdhVTD2P3wAoiJ2",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "061238ea46cb1b6c2802bc46041d6085",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1x1oMh1QjMFnuH8YQ2U5j0zfcVRULx4cdEjbHI8GK7jm",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "ca923a33645018f34cd1baaa684e12d3",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "131Aec8RIMn4Gj2LMpwuXcVJmRkWF5uKtE01Tl8S5MQX",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5c87f776f5e7a9c8aa7c212615d44feb",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "13ruec5XoRYnvvxRfgMJPMuuNutLi9vUukuk8LbBiAE1",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "de81cc37c95970f73acaf29a27334374",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "16FZyDnIUefzfStMH9kxdVr8nrxysA7o6m48WQVQAU89",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "a75532509790aff937c8c8d291788f60",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1PfvI7JtL64yp3xOpoKqRAwwTEhQWNvLip0qCbhaLs8N",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e3ac7c19344e64650fa2b4a2913dec77",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1LSGmrkzW5iPqEdti8YRmU9BEbewwP2nriDs7Jm0DdMv",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1ODlbz3IiRpPlBiWMiIw6kEIFSTy2O9xKMY643pYmH4X",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1YNR5Rkw4QJ7bcY897grK9s8Z5FOvMmuFZ1a3rMw70ZY",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "374d782e3ec376d27194fef40ef73687",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1JjIOCcVuYuVeHC3w4A9kurav3ufUUMUks8IarpAGkVc",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
