"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1iOPLyOWLhXkPHTuh8HBb0QB4skF0hPQSUXcoj9Ty25S",
    "1dw6oUVsR9GIWxuWTxPwKyBQgAtD4vhC32j8Yvutpofl",
    "1QyGwUSNIVHtRUrTctCkB3EEEcmUKTgn3eMpKLSJCFza",
    "1bxs7fHONjFFttISPljbeztSJhwQnJgPX66n4ya9HXwJ",
    "1tVjNWB8rqfDA5A59mq3bLFoNJ2tMbEQvitS8ORYQ2bV"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "cb697cf8d9e7e267481c7aad28564f1c",
    "f44d3cdfe6313d458a8ea5b7efc784c8",
    "825a6bdf9bfac4c958e0be25d5123e79",
    "c5c3135ed2f56741dc46590da6487053",
    "fede822f73d52f12c3f7d44dbef28165"
]

LEGIT_PERM_IDS = [
    "c304e7c0dccb568ecf81649abd2b4a4a",
    "e5be7aa5fcfe7b9cb414640fc8e79927",
    "b157ebf31b3731b2f67c169cd2ed0fa8"
]

NEEDLES = [
    {
        "id": "1iOPLyOWLhXkPHTuh8HBb0QB4skF0hPQSUXcoj9Ty25S",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "cb697cf8d9e7e267481c7aad28564f1c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1dw6oUVsR9GIWxuWTxPwKyBQgAtD4vhC32j8Yvutpofl",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "f44d3cdfe6313d458a8ea5b7efc784c8",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1QyGwUSNIVHtRUrTctCkB3EEEcmUKTgn3eMpKLSJCFza",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "825a6bdf9bfac4c958e0be25d5123e79",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1bxs7fHONjFFttISPljbeztSJhwQnJgPX66n4ya9HXwJ",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "c5c3135ed2f56741dc46590da6487053",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1tVjNWB8rqfDA5A59mq3bLFoNJ2tMbEQvitS8ORYQ2bV",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "fede822f73d52f12c3f7d44dbef28165",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1YRS9ZjDYkCp5Fc0zoRZ42CyXKnjySenWBn63HnZzpoO",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "14CcUsKsv48PSg87RmXfDeOPS6rD8KVGTkuVwzgi7yzg",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "c304e7c0dccb568ecf81649abd2b4a4a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Kj0TAVuxRnm1ksSyMsOoZDBovy2b0tuOEDN2mE1GKew",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1Egw4yUltodVgDntDU8Jp1XV5xCP7K9Y2nBJ4zeYAicJ",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1mRdqpEjzalXhsOtxkTeLxuO30wBTWpQoJVTOIYvBUFo",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "e5be7aa5fcfe7b9cb414640fc8e79927",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1tp84kgq9F1r4jdeVVyRdRfqm1XLS0C1QjcRGs4LXv8z",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "b157ebf31b3731b2f67c169cd2ed0fa8",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
