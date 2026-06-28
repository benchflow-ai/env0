"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1rzjw8m1UvdHDGEXjWL4ChP6WbGmmhSbB9QfsbXBiO2d",
    "1AYwCxIinzG76hqTFuJ6XUyR1ZbCz8xvHpfy52ynMLQn",
    "1wJnHyLTBzNPDhhOpcOiSK4McTFHUBXmH0hjstbJVbrv",
    "1IFAjfrv6BNsPRyhYiOp2zXwoPDn29JK6GHcsULJeZPR"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "45f86926b62854543277446aca49cb24",
    "8b7f3d2088de0f67a818a5558f1c54c6",
    "7493e36b8edd76bfb21c6e82114258bf",
    "a4f290b93823bce4372ba5d32494bcaf"
]

LEGIT_PERM_IDS = [
    "0eb9d1bf06f89c51bc42b1e46a14e9ab",
    "27dff1fc4c963db80f564e3fef50223f",
    "524d9642083fe954431dc6f91b745809"
]

NEEDLES = [
    {
        "id": "1rzjw8m1UvdHDGEXjWL4ChP6WbGmmhSbB9QfsbXBiO2d",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "45f86926b62854543277446aca49cb24",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1AYwCxIinzG76hqTFuJ6XUyR1ZbCz8xvHpfy52ynMLQn",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "8b7f3d2088de0f67a818a5558f1c54c6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1wJnHyLTBzNPDhhOpcOiSK4McTFHUBXmH0hjstbJVbrv",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "7493e36b8edd76bfb21c6e82114258bf",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1IFAjfrv6BNsPRyhYiOp2zXwoPDn29JK6GHcsULJeZPR",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "a4f290b93823bce4372ba5d32494bcaf",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1aa9F2ErAtVYVt0OTwwmXBkga3VbrsT32eyaxA72mOEQ",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "0eb9d1bf06f89c51bc42b1e46a14e9ab",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1auautUH0Y9FZU8Nvzv1tnuQZoMXvVE1nlqe91xembN0",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1NOwbV1X3L14CafF3Mx3X1eWyiNbCTHrNgC4n7Oox6Er",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "27dff1fc4c963db80f564e3fef50223f",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1MXHt1jBE6qVnmKwfDX6aGoQrX7W2rypp6TudOD7ct3Y",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "524d9642083fe954431dc6f91b745809",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
