"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1xPGciewYIykqwC72nTrXtctA6f05vU8C930k8YsMTtC",
    "1OpuGGMRv8A1n6At5fMaYdgdxHPwCchrcnjBsWoUyaP5",
    "10hXmWClBOW2pWSH4l9ZQdYbO0AqCFBFldW1kiqgi1yh",
    "1Sj7YLuZVkLBudNTmSHcpBc2Tyz2aV1f9BMRydxbSElC"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx"
]

OVERSHARE_PERM_IDS = [
    "b7916ab329b11dfe955f01a723c69602",
    "b6734c9d0c75e405e0ab7605dd6008de",
    "95f56a1119a788522f0c670185ac0cf5",
    "c2afc73ce80e3bb6426b6f62869bfe51"
]

LEGIT_PERM_IDS = [
    "92d9e4fe947f7e9134b0ee5732aa263c",
    "1c53d0fef7869d43f185816cd5588e94",
    "2b6125d6da538a5085d172c7d6b804e7"
]

NEEDLES = [
    {
        "id": "1xPGciewYIykqwC72nTrXtctA6f05vU8C930k8YsMTtC",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "b7916ab329b11dfe955f01a723c69602",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1OpuGGMRv8A1n6At5fMaYdgdxHPwCchrcnjBsWoUyaP5",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nFoundry Labs proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "b6734c9d0c75e405e0ab7605dd6008de",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "10hXmWClBOW2pWSH4l9ZQdYbO0AqCFBFldW1kiqgi1yh",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "95f56a1119a788522f0c670185ac0cf5",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Sj7YLuZVkLBudNTmSHcpBc2Tyz2aV1f9BMRydxbSElC",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "c2afc73ce80e3bb6426b6f62869bfe51",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "133ZmpIlHEBi6nb3pTiQrqodA94iDFNBkO5TbqfTmGmJ",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1peWTtdQQHobjgf6CRpjurRigjK019te8ew793LNXF7U",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "92d9e4fe947f7e9134b0ee5732aa263c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1DFwCAqKaS4eUXPfUySW8MBqayJy3Q4JtRza36QEF4NB",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "1c53d0fef7869d43f185816cd5588e94",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "18esicD604j2Uh4JICB4bGfn6J25cVFGah9B7Xc2EfZ0",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "12yfb4LEggSgyU3cAiLeJsU4vm8u17aBGOK3MP26a2gJ",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "2b6125d6da538a5085d172c7d6b804e7",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
