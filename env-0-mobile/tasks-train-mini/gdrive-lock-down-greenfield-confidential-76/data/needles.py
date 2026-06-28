"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1btLe3jD6CVcA9xLgUPGY17cmbgUSpBXABhhDyrDg6Qe",
    "1E3BvTb7eMzBBgEoOu3OPg9XaTNPbnVUVdWM0hRCLpzj",
    "1apBpIf7Nw1T9BRCANb9Hg4yyEpqyg9meNmzO4j9caz1"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "09e44a4673f7c04d1a339c6ef2a2e430",
    "aa43c389b265a384677155aab769c276",
    "0c84db8cb9aa79af0483b7035658b557"
]

LEGIT_PERM_IDS = [
    "b4209d343bf46a635d861aa9eda5c499",
    "51d5effb71471c3cec53f35dcc83e1ef",
    "d0443e44e8a0f570e7957999bf4a8bf2"
]

NEEDLES = [
    {
        "id": "1btLe3jD6CVcA9xLgUPGY17cmbgUSpBXABhhDyrDg6Qe",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "09e44a4673f7c04d1a339c6ef2a2e430",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1E3BvTb7eMzBBgEoOu3OPg9XaTNPbnVUVdWM0hRCLpzj",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "aa43c389b265a384677155aab769c276",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1apBpIf7Nw1T9BRCANb9Hg4yyEpqyg9meNmzO4j9caz1",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "0c84db8cb9aa79af0483b7035658b557",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1lJSgczp2Qibpzz5DzIniZ2yrSuI7mtZI23DQLGzOdcD",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1Vk3liXaT3cgNKvKMfT10zHIQk67idLqqQEu1XER3rAl",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "b4209d343bf46a635d861aa9eda5c499",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1MCr2bUJMnWjr9WKOhtd6vaRC4ZLdy0KY8d1O9DXDfJw",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "51d5effb71471c3cec53f35dcc83e1ef",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1K6eLv53LE6JTAuEIfq3gERuo4ef3O8e2i5rrVxxsWoQ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "d0443e44e8a0f570e7957999bf4a8bf2",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
