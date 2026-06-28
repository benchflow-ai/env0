"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1w9N4GrSd2gJyZdufwkFbAGjpH5YOsarbD3jOGY1RkQq",
    "1K6r7oFqvSXZNZgjigPvaVtYiFB0CzfHFQ1Kdc2dznHi",
    "1kMNb6UCLuds7Db54zS242Rb8rEWSdubbFlDGU9BKD4R",
    "1RENvroJ4Hac8HtJPEHOiWoVAslD5cSOEjcN9cXyB4VN",
    "1sCoflje92QAbTxqRaNZL64Ce9LPVIGatIIRnRBSBUCF"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "f3e0f4ca717924af0f98c2ba139d919b",
    "98ed2c899aa47f9764aab6aa88004cf3",
    "f59b21fede02f71164b11de454bb63e7",
    "025daa50e54bb83ce9b1da483c5b50dd",
    "d0506c3597ab67dd009e4a7b38de3a67"
]

LEGIT_PERM_IDS = [
    "d09439b9f8e30a50737f0798b4c76ad4",
    "05f8d5a71399e7b239eb0a255cb862a9",
    "3241d2b172b2300416b1e1e2ec3d13c8"
]

NEEDLES = [
    {
        "id": "1w9N4GrSd2gJyZdufwkFbAGjpH5YOsarbD3jOGY1RkQq",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "f3e0f4ca717924af0f98c2ba139d919b",
            "type": "user",
            "role": "reader",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1K6r7oFqvSXZNZgjigPvaVtYiFB0CzfHFQ1Kdc2dznHi",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 8,
        "overshare": {
            "id": "98ed2c899aa47f9764aab6aa88004cf3",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1kMNb6UCLuds7Db54zS242Rb8rEWSdubbFlDGU9BKD4R",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "f59b21fede02f71164b11de454bb63e7",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1RENvroJ4Hac8HtJPEHOiWoVAslD5cSOEjcN9cXyB4VN",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "025daa50e54bb83ce9b1da483c5b50dd",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1sCoflje92QAbTxqRaNZL64Ce9LPVIGatIIRnRBSBUCF",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "d0506c3597ab67dd009e4a7b38de3a67",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1keP4epbdSGHFk3do7UraZwkXhn1vcs5ee2MTYOczSpU",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1wQb7Z7mnUhkzkYVgTO0OV5TKzvl6U9aVa8JqAXRBURN",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "d09439b9f8e30a50737f0798b4c76ad4",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1cgY05yLuHoZKSzbKbTqas2Dsj7AAmlGS7hydHXkKGIA",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1dBFzEFJ7BzWL9WXxYhAfRtSVLdBEvysWCmdlOG70Y3i",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "05f8d5a71399e7b239eb0a255cb862a9",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Wf81TUxDPbLlohLaMqfoDPsqdxOm9T0pMVWL9cEFEJw",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "3241d2b172b2300416b1e1e2ec3d13c8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
