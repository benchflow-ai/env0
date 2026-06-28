"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1nXb7Du2y9uQUanpbfFvXP30vFzGLn1RaEqx7jqZyU8Y",
    "1hGXGiKCnpjbOMMt74T9fJaL6wW3odSz33bTrySkgbBO",
    "1gqPBOJh6fmylzAwBrmcyViIaoY0F5tmdcetqi6oH4hS"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "e03e99f582b8dc31714a81ef40c419e5",
    "575a9148038a9b70547adcd576ad4845",
    "ebdf765ac2d5330a490dbbab00334fa8"
]

LEGIT_PERM_IDS = [
    "6f96e4b41ae6cdff675be80b1b4b8848",
    "59a98cd5ef153047fc0a629c9941dddd"
]

NEEDLES = [
    {
        "id": "1nXb7Du2y9uQUanpbfFvXP30vFzGLn1RaEqx7jqZyU8Y",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "e03e99f582b8dc31714a81ef40c419e5",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1hGXGiKCnpjbOMMt74T9fJaL6wW3odSz33bTrySkgbBO",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "575a9148038a9b70547adcd576ad4845",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1gqPBOJh6fmylzAwBrmcyViIaoY0F5tmdcetqi6oH4hS",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "ebdf765ac2d5330a490dbbab00334fa8",
            "type": "user",
            "role": "writer",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "13VN07XpwGhPf92U41ynWEINJfbSWJXv51iQx5vYNj1P",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "6f96e4b41ae6cdff675be80b1b4b8848",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1kjzvcDvaHiv1TWJakljJUeNCoQ2iXiOH4PjJxDAk8nv",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1W46OQHR9to0t8ePg5tUm0UP6bNb3OeIjCuvPvwVVyx5",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1hLLVCsGDnJYpvPcHsJNxOEzFyZSDcry0ejDxWFgJcjJ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "59a98cd5ef153047fc0a629c9941dddd",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
