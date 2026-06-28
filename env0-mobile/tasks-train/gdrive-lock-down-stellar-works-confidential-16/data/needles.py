"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1TV3gwGkYfGf5QZm0wMKoEAVqwXziYg4eY4xlQMlOPjx",
    "1yvlxveIzaE6O1YluGXgk20HgljXboCeS9aTN3fGrOSY",
    "1W6HaiVkCxV2mNM4i1hpzRoTAYUk7cT4caqHJaT3hG1j"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "518bfba8126b1075e215192452045132",
    "7e2e1f1c373991235e736257a8cca539",
    "4cc275600ee32121d1e5d9db4ef60f21"
]

LEGIT_PERM_IDS = [
    "7e6594e318e23a986a64ed9a090085e7",
    "a113a40afd8dc0b1c4dde542d030fc7d"
]

NEEDLES = [
    {
        "id": "1TV3gwGkYfGf5QZm0wMKoEAVqwXziYg4eY4xlQMlOPjx",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "518bfba8126b1075e215192452045132",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1yvlxveIzaE6O1YluGXgk20HgljXboCeS9aTN3fGrOSY",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "7e2e1f1c373991235e736257a8cca539",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1W6HaiVkCxV2mNM4i1hpzRoTAYUk7cT4caqHJaT3hG1j",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "4cc275600ee32121d1e5d9db4ef60f21",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1xn54DuCUdLsPtxdL83vV8JmHZUsVnIgbgW5ax9GagaZ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "14iAN5GvxI0hlnuP05DNQQOs3n8kZFbRQnrhTk3zVtLL",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7e6594e318e23a986a64ed9a090085e7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1puYR8LYG50Vv7jptep8taWxNQDlWLRmAOl4j3iGK54V",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a113a40afd8dc0b1c4dde542d030fc7d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1YVHpU9G5QhSAPEJTC0eoWKCPp3aUv9xMY7pMreR3KO7",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
