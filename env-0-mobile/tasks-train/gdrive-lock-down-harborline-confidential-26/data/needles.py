"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1L7m8LUlUmtwLxSWzvOmXCtS65jvJOwOgf7Cm7Rbb3e3",
    "1D0Zs7z6Cn9ai1R2bW9ho504P4iRQYZyXNa3ZzpWicVs",
    "1bA1HrfL2rZU3kHQVO3XEtyHRVYEtl9QGi0tplThIya8",
    "1Vf5gcLXbCQkkrtTQvuVqlzMoJ2CF5B2mBPpEvI1HBok",
    "1sSldaXHzhqat76NukamP4rsIxk5Zbi0roLem4KhI8Lg"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "500838c5604e1bda14e74d43f2ca4761",
    "64e895d9fae2266ab8edc6e4a9c3b855",
    "4570d9166186c97ef27a53899bbdf28a",
    "eaf0062e6d1cdd160f14fb5ea563a733",
    "cdba401bc36cbb249d38a22a6f2faf2b"
]

LEGIT_PERM_IDS = [
    "205a207df24b8f992b3920dd2421def4"
]

NEEDLES = [
    {
        "id": "1L7m8LUlUmtwLxSWzvOmXCtS65jvJOwOgf7Cm7Rbb3e3",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "500838c5604e1bda14e74d43f2ca4761",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1D0Zs7z6Cn9ai1R2bW9ho504P4iRQYZyXNa3ZzpWicVs",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "64e895d9fae2266ab8edc6e4a9c3b855",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1bA1HrfL2rZU3kHQVO3XEtyHRVYEtl9QGi0tplThIya8",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "4570d9166186c97ef27a53899bbdf28a",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1Vf5gcLXbCQkkrtTQvuVqlzMoJ2CF5B2mBPpEvI1HBok",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "eaf0062e6d1cdd160f14fb5ea563a733",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1sSldaXHzhqat76NukamP4rsIxk5Zbi0roLem4KhI8Lg",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "cdba401bc36cbb249d38a22a6f2faf2b",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1xBPWYzMvrSYUHaPEiaG9vol9SvGqfMrzkWIHMtWjlpS",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "205a207df24b8f992b3920dd2421def4",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "1mcO99ZmZ4MtRbQsCiveVaXYGxgH84VGJ0bjvbMsayWC",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1CA19qiuRSdFZhtu3eZ6h920g3m1fmya3njWK0epKKX3",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1OG9tFVhGX8GadPfpgp3rfqFIb14IxDeKumi6S6cCXvE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1XBfX4NJ1aM30osyrkYlOCTjYtu3B9CcQiP4EE459WHj",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
