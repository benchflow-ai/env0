"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "1gEaTDFwjXrvHi4LVHPkeCsVFOJ4yORQbcy90tWoFDMw",
    "10obootwOOo0KuLHSo9kErDL3LrNeX2RNV9DtCHSMz8C",
    "12mhxFi9OfyfOvDDytgPEBHAwV6254xzkTRTABpbv3Te",
    "1WuutuwXM6k5GLnlbt2OVCedodxCmJlH4he6H7PEtalc",
    "1HgJwsFMoCbYRXsT4GGQw3J5edgbFX3yj23LWmIqwSl7"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "df23be352b218d4b720b2a1849a8f5c8",
    "76d9db43c79bb3dfbee0f6534febd47b",
    "6be5265768002f21a156014634db7ec2",
    "ddfa7ae23fa268b56c5f21001917c992",
    "3c7969bd934ff4f54bd327778bc9d723"
]

LEGIT_PERM_IDS = [
    "385bd6357eb56606631922a6308d7c25",
    "c1990fb24dcd079e7876533c85aebcb3"
]

NEEDLES = [
    {
        "id": "1gEaTDFwjXrvHi4LVHPkeCsVFOJ4yORQbcy90tWoFDMw",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "df23be352b218d4b720b2a1849a8f5c8",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "10obootwOOo0KuLHSo9kErDL3LrNeX2RNV9DtCHSMz8C",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Harborline\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "76d9db43c79bb3dfbee0f6534febd47b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12mhxFi9OfyfOvDDytgPEBHAwV6254xzkTRTABpbv3Te",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "6be5265768002f21a156014634db7ec2",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1WuutuwXM6k5GLnlbt2OVCedodxCmJlH4he6H7PEtalc",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Harborline\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "ddfa7ae23fa268b56c5f21001917c992",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1HgJwsFMoCbYRXsT4GGQw3J5edgbFX3yj23LWmIqwSl7",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "3c7969bd934ff4f54bd327778bc9d723",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1IyInGnTb8FGSINeCPWL3ctVgUW1oWPILYXPCA19yn3V",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "385bd6357eb56606631922a6308d7c25",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "15VnTKu58hoar58ko2uljnlLezmzej8B1UX9e5UFADex",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "c1990fb24dcd079e7876533c85aebcb3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "15LTXDV4V0yKqT43oKS3phRh94fGZp5f7Fw0rlZJ6Rhx",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "16AT6B6ThxKEYNWisZh5fzZ5fIYm0uUiymVWkkyN77xE",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
