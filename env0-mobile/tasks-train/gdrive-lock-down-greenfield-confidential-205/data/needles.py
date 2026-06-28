"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "17gfgktPuXylprlsQr77VeyUcFkmC8HVidtW69YZPzLv",
    "19sSmVrnXkkcXSUI5DAF8MxnIWdiNSdyfYZmVFYbDGdn",
    "1I9tqaySwR1aJcpmdJ2waslBgBtZJgTecM7HHV3Y5JsI",
    "12OLMAjmiGkvByfOKPSkuhDxJiynh6sdzs6oy99ceoi0"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "6e7aa651286fae3d3f5ba7a3579ec016",
    "0e01f9e0fa9f99e12dcd308fe695ef76",
    "610d7adc58e5a9297b06c44e8ca8ad23",
    "48e3362034f6e5684b68cdcb8127c3aa"
]

LEGIT_PERM_IDS = [
    "bec540ad695066c825be905dbcbff8fb",
    "f2038eda62b1d459fe34cdbc166d985a",
    "f79d09de5771f465cf123003217a5a81"
]

NEEDLES = [
    {
        "id": "17gfgktPuXylprlsQr77VeyUcFkmC8HVidtW69YZPzLv",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "6e7aa651286fae3d3f5ba7a3579ec016",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "19sSmVrnXkkcXSUI5DAF8MxnIWdiNSdyfYZmVFYbDGdn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "0e01f9e0fa9f99e12dcd308fe695ef76",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1I9tqaySwR1aJcpmdJ2waslBgBtZJgTecM7HHV3Y5JsI",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "610d7adc58e5a9297b06c44e8ca8ad23",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12OLMAjmiGkvByfOKPSkuhDxJiynh6sdzs6oy99ceoi0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "48e3362034f6e5684b68cdcb8127c3aa",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1BUh9TbXnqvIlGC3DQ83UZ4eKjKXOJ0aBTuE3IHAAQOO",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "1Q3plkil87WTFaroNZ2iY138dIMR9Ns7bj90Eh740gF4",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "bec540ad695066c825be905dbcbff8fb",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "1L2j9G3S5Tb4MOmFZErW3gXorN8qE3k2ES3a4WMxp4gf",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1K8z0zhWM6yzKOQagN9dF9jl9HsinZVfF2srgPLfIPwa",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1QNnO3vW88ZafobBuwJ6VazHEoFhcQMpbAT7waJlZjmh",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f2038eda62b1d459fe34cdbc166d985a",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "127jWq0t8RpG07uvvFPpzaXNOFYpeZ1CN1UD568ZUw3J",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f79d09de5771f465cf123003217a5a81",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
