"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1rchBAHuMhxx92Daf382JT59oYRAkAJXLTMHE9WxgKrz",
    "1SQDMOj5Ww1T2EMs1sKCYzg1jMajfflPVrEjowYvtNYX",
    "1bIOETAGV5GK7nxxMyEv6f9urIgP5lGRKfijSHrGa1MK",
    "1Qs2GV3fwXGBqX8SxA4R2DXAJafsZuhAENl8Qk9i4MRK"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "24a5d070559596b924f2774acd6543dc",
    "0170bce35390657883b33262ef8dc745",
    "1a888cf837d661dff0c83d8b1f35452c",
    "46d1d3dae929d9378fc923672c7ccf77"
]

LEGIT_PERM_IDS = [
    "896e09973278a99d23d66434291a0cf2",
    "ae0f120d6ee099a584f9c733a899ac5c"
]

NEEDLES = [
    {
        "id": "1rchBAHuMhxx92Daf382JT59oYRAkAJXLTMHE9WxgKrz",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "24a5d070559596b924f2774acd6543dc",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1SQDMOj5Ww1T2EMs1sKCYzg1jMajfflPVrEjowYvtNYX",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 24,
        "overshare": {
            "id": "0170bce35390657883b33262ef8dc745",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1bIOETAGV5GK7nxxMyEv6f9urIgP5lGRKfijSHrGa1MK",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "1a888cf837d661dff0c83d8b1f35452c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Qs2GV3fwXGBqX8SxA4R2DXAJafsZuhAENl8Qk9i4MRK",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "46d1d3dae929d9378fc923672c7ccf77",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1ixOMUKEcwhdESM3f2ZysJxPJHH7h5iaHkUFAGChHMzW",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "1jhGQ25fZJxcUcZdxsgcqQpnF9YSWwRx45DbhF1ohHKA",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "896e09973278a99d23d66434291a0cf2",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1M25WDZnjNkSWHEEbINsaRm4jUvf5CqIELlIL91DJebF",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "ae0f120d6ee099a584f9c733a899ac5c",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1qE6uiA3lP1L68i5mR8OUiQEMaoRruPzxxsWIcN7MCF7",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
