"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1MhoBzFFi6Y1aUQSCgWlFOVKMvjr4bpg1CnpUVRN2ir9",
    "1RzGd6f9Zu7AWFten44l5SeqcQJdvvwgapCF0Z4HI9PZ",
    "10WhPk4j8xXVdCQX3Us2fXv5cG6Nfw8wgXmdonsuFOj3",
    "15TAAOpcgfnlm52dMwbj8qCFUnLdgpvDWtKCla9NrfXn",
    "12VRnVSiSqxmjHG2IPaiUL7xrh423bX72I5pCEQSJtvE"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "80849bc4c68e84eb2e1dd5556c480cab",
    "3a182c5f762a09360135815d3e454504",
    "7c2a4bf942cb64b5ed0213f394f6abc6",
    "258999e14f6bd25db2746ade31822693",
    "615b25cfcb04072186f750bcdd04d822"
]

LEGIT_PERM_IDS = [
    "068c0cf46ddb2aeb47c5dc9f564767a0"
]

NEEDLES = [
    {
        "id": "1MhoBzFFi6Y1aUQSCgWlFOVKMvjr4bpg1CnpUVRN2ir9",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Foundry Labs production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "80849bc4c68e84eb2e1dd5556c480cab",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1RzGd6f9Zu7AWFten44l5SeqcQJdvvwgapCF0Z4HI9PZ",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3a182c5f762a09360135815d3e454504",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "10WhPk4j8xXVdCQX3Us2fXv5cG6Nfw8wgXmdonsuFOj3",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "7c2a4bf942cb64b5ed0213f394f6abc6",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "15TAAOpcgfnlm52dMwbj8qCFUnLdgpvDWtKCla9NrfXn",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "258999e14f6bd25db2746ade31822693",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "12VRnVSiSqxmjHG2IPaiUL7xrh423bX72I5pCEQSJtvE",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "615b25cfcb04072186f750bcdd04d822",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1oMDNdoQtVd2mwnz6L2zh3oFIBcYrnOrBQfmd4Yq4suT",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1mSAkLETp67gAVFY0uAd37ijcW355Uyq4tcDiZVrfPBS",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "14rfJrnLfuuM5cU7O9BdURRCdAUCUURU7kzxT0JutACI",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "068c0cf46ddb2aeb47c5dc9f564767a0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1UHpEtnNrOsmrdFjFMrDo9dq1cLRvzkEcEYkcilX0x0x",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 50}
