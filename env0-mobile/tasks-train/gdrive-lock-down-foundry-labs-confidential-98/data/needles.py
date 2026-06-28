"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1xRGOt9UtCtbumQCNsvfgPyBJpm0Om4tEz57Z1IYKyVA",
    "1MNgajJPENaDC9Zz99POxtuuN9Ytv9cQu6Ea7onCIwRJ",
    "1RLEp5ZOML3YtekETtdd3FFJabfNVNNgvDd3OwNT6tEq"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "ccb2261020414c1df8b2ee337c71ffe5",
    "9e5cf522262ba36b20b8f9a4528f0703",
    "859f52517e6ad7e16ad049f68cbe3070"
]

LEGIT_PERM_IDS = [
    "51aea8ace233c4ac7680877cb32c14e3",
    "27d9ab7d60107505bc679f364fa55442",
    "9d167d25d357b0e9dd699108b1d34d74"
]

NEEDLES = [
    {
        "id": "1xRGOt9UtCtbumQCNsvfgPyBJpm0Om4tEz57Z1IYKyVA",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "ccb2261020414c1df8b2ee337c71ffe5",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1MNgajJPENaDC9Zz99POxtuuN9Ytv9cQu6Ea7onCIwRJ",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "9e5cf522262ba36b20b8f9a4528f0703",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1RLEp5ZOML3YtekETtdd3FFJabfNVNNgvDd3OwNT6tEq",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "859f52517e6ad7e16ad049f68cbe3070",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ii74FdcsZAmTlgBhnq5MGp3OEyimKQlwBFNg0pr4N1l",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1ZnPlqYrgrvGGtBYOgyygI2JmrYCgczcC3mrKMqLYflX",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "51aea8ace233c4ac7680877cb32c14e3",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    },
    {
        "id": "1fwAuM1GIPF3P3YRxJL0Gj7DRktoMJBipLMZSLBh1R6b",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "27d9ab7d60107505bc679f364fa55442",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1XXyzAYzI0jgziJ22rZ2Ddl0PVmBLCKlECaF2HRgvWQk",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9d167d25d357b0e9dd699108b1d34d74",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
