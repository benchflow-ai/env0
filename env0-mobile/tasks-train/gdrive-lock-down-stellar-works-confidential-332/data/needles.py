"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1PmQUDvrPOYU0Suv7GV6NsW3PVQ3uGI086nYvKKQT1pX",
    "1SF6oggpqoZ3tihlT7XT4nXHlKhD9mvaS7U58p15XAMf",
    "14MwFmgdqsyM5GwWFcBaAiFaR3WWpcgGcv1w2MGtsMRQ",
    "1qboSfh12u7rttAy500fn5Y6Pdaq6W9nKmcQRDEqfnEQ",
    "1GVwTJzdgraAWzRZJneU4JPi8fXE3cagnXNmc4pi1v67"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "db7f678b970be85b737fb5ffaa42fb41",
    "8dacab437abcd1238af338172ec521d1",
    "a1af5395043683cb1e743c390f10f895",
    "cc24cf0810105516284e60649a868bbb",
    "820bec9a7a548c9afe3dc65d53b99b89"
]

LEGIT_PERM_IDS = [
    "fde4302f1b3673c89335dce97dd733ad",
    "a9d760604df115f00fb34dec6cf8b348",
    "fc0f5835d1e8c595d9fe11ef9b6b0186"
]

NEEDLES = [
    {
        "id": "1PmQUDvrPOYU0Suv7GV6NsW3PVQ3uGI086nYvKKQT1pX",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "db7f678b970be85b737fb5ffaa42fb41",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1SF6oggpqoZ3tihlT7XT4nXHlKhD9mvaS7U58p15XAMf",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "8dacab437abcd1238af338172ec521d1",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "14MwFmgdqsyM5GwWFcBaAiFaR3WWpcgGcv1w2MGtsMRQ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a1af5395043683cb1e743c390f10f895",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1qboSfh12u7rttAy500fn5Y6Pdaq6W9nKmcQRDEqfnEQ",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "cc24cf0810105516284e60649a868bbb",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1GVwTJzdgraAWzRZJneU4JPi8fXE3cagnXNmc4pi1v67",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "820bec9a7a548c9afe3dc65d53b99b89",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "10gv5zz7TXblPlgBjAtsof0YQe5ZTR1LfK2aSKk3B20O",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1ibMHRmArcXPDRIZuok3T7VRDXx7dBWJRdvcBUfrM0y7",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1EGpaLhi5iTMpo5OZ72evML59ERxo40ObbxlQcsEEYUK",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1FcYJaXyX9IE7invZpn6G3uKVUp6GRTvxE6SuU8OtqiZ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "fde4302f1b3673c89335dce97dd733ad",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "163DrJNVSur798mCYQewAVyvipvcPwKH0yk3IIP9wdBt",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a9d760604df115f00fb34dec6cf8b348",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1VUCnkqP3GrqX12kYRNsvbXKhr0smqiFDtrYMzzHzOFS",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "fc0f5835d1e8c595d9fe11ef9b6b0186",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
