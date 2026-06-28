"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1aoUX2rrK42AGIRoerdd0Pv4cqF6PHjNPY2v6hFSVL5e",
    "1qdcDV8rVJsr8prmRVBUxlgdTgEYeFmcAAZk5gsG99kf",
    "10qvFA7u2HhYefVEuulNTYp5Usa0pmsY6kOV9s2JNiRA"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "0786aaaab9477e5d7aac6072bf19ec2a",
    "506416553519ee588fd8b979a94a5b62",
    "a4c0519d658d3d5ff6a6a54d7c3a44ce"
]

LEGIT_PERM_IDS = [
    "790587175f08cafcf96005b44fb96ee5",
    "46ebb6c11288937df3e5df195b690cbb",
    "85409a6d849f35e567d892f0e05b0048"
]

NEEDLES = [
    {
        "id": "1aoUX2rrK42AGIRoerdd0Pv4cqF6PHjNPY2v6hFSVL5e",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "0786aaaab9477e5d7aac6072bf19ec2a",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1qdcDV8rVJsr8prmRVBUxlgdTgEYeFmcAAZk5gsG99kf",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "506416553519ee588fd8b979a94a5b62",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "10qvFA7u2HhYefVEuulNTYp5Usa0pmsY6kOV9s2JNiRA",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "a4c0519d658d3d5ff6a6a54d7c3a44ce",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Im6aGI2bnzCwVrcoAL6BqZaU3JPb4Nq88m2XBLFHa1W",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1iwbTMPX98s4O15PyoBaOxIs5znwktMoVVRMpUVhgSvQ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1AJSXyq9OC6BhrUU3tAKOBjYc4Z5QXhBMyfSiV2iy4wq",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "790587175f08cafcf96005b44fb96ee5",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "12seTLiSTmN4vuD2KbjSnbFTr9cHUasN2pxMsmao4BaC",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "46ebb6c11288937df3e5df195b690cbb",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1WztqzQkPclHkHvG7wM98zax69Hufmr9ECzCeTnWgK5Y",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1RpLNzohv9Q6RRYUWzjmlRRHX5vhLXiVryjO8MkXqoVb",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "85409a6d849f35e567d892f0e05b0048",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
