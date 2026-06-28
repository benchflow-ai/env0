"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1HGsTqFe0zXNgUgjwrZ9085yGiTlvMwj99tcKvMgCfjL",
    "1u2b9n9QnT7PA0iroI5Vjf7fCC2zGqZ3CGLL2JWvGNWK",
    "1B1KUE6iM68znDRVsPGKmegNJ18UHV19U7zU2uRwDZt3",
    "1r67neHecwzljz2grM8Sv050gUMU62NHXU60X4jVMOo7"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "09a50aa96c6e4a6dd8a6e43bdd1d283b",
    "dedd66dc20d190ad9970b183b294342e",
    "f61d4e6e39db78d6469e29cf6c8913f6",
    "be8dd50fbed7211bf96c7b116b8e94ad"
]

LEGIT_PERM_IDS = [
    "b8b61c8c30817575335ae4a696da4feb",
    "75fa1e32663a3e1ee94adaa59b713e18",
    "d3ddf8126c36794fa06d1b37bf44c20b"
]

NEEDLES = [
    {
        "id": "1HGsTqFe0zXNgUgjwrZ9085yGiTlvMwj99tcKvMgCfjL",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "09a50aa96c6e4a6dd8a6e43bdd1d283b",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1u2b9n9QnT7PA0iroI5Vjf7fCC2zGqZ3CGLL2JWvGNWK",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "dedd66dc20d190ad9970b183b294342e",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1B1KUE6iM68znDRVsPGKmegNJ18UHV19U7zU2uRwDZt3",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "f61d4e6e39db78d6469e29cf6c8913f6",
            "type": "user",
            "role": "writer",
            "email": "felix.yuan@brightline-recruit.com",
            "display_name": "Felix Yuan (Brightline-Recruit)"
        }
    },
    {
        "id": "1r67neHecwzljz2grM8Sv050gUMU62NHXU60X4jVMOo7",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "be8dd50fbed7211bf96c7b116b8e94ad",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1rCSj3P1XbPqY2mWOi1eUnF5W5KJ0qcnnS8A4BVGMOvF",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1jaHcNwwDPfnwZbT6CIrFFrfIIXlEjlOFGkwyFfvZ4Pv",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "b8b61c8c30817575335ae4a696da4feb",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1ANvwzNe0KCKU5s9CdwJsez9oetdGkEnh9K51NNLOQKb",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "75fa1e32663a3e1ee94adaa59b713e18",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "18lKQRxG54FpT4Vbzt41zy6ey2A9zwZlz2Kj2z8AgNfq",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1sA6eqVH5YAp0bc1ubSZqmtrAw6JzRPzhWtRCyPlVtmC",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "d3ddf8126c36794fa06d1b37bf44c20b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
