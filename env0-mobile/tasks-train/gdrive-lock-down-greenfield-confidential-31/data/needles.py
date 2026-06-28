"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1zLYgHRXH9S7QM3lEofoE3c3EfZUNmSNeMFDQL24KXXX",
    "1ZNKU5hTbT6tyUUnukfstLzQyMikyK2cDZpUzJuqUS56",
    "1P032mgKE3d7RlnPyVdbEZCa9fQ1neotBMpJuQUWM9qE",
    "1g2TQ50gShtZsJ40gG2FJco652TNBsLt2DWacnVRuWFD",
    "1FvhRSo2UMECzPm7tbCzClNYJFWTXJtcxk4hRyKcuztL"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "3edcfdb784ef4ff563dfe068372845bf",
    "bb6e2104b5f36cc977441d16e7bfd3b7",
    "d60188d7b36f99abbe36b588bdb84719",
    "90e27355a95b043178d6a38616caf1ad",
    "043c305dabce81a1fe465fb4d051979e"
]

LEGIT_PERM_IDS = [
    "67e8b81ffdb1eeb39cc26b3a9053c1c7",
    "86f8832c09697afb120acde0820c8b81"
]

NEEDLES = [
    {
        "id": "1zLYgHRXH9S7QM3lEofoE3c3EfZUNmSNeMFDQL24KXXX",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Greenfield production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "3edcfdb784ef4ff563dfe068372845bf",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ZNKU5hTbT6tyUUnukfstLzQyMikyK2cDZpUzJuqUS56",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "bb6e2104b5f36cc977441d16e7bfd3b7",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1P032mgKE3d7RlnPyVdbEZCa9fQ1neotBMpJuQUWM9qE",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "d60188d7b36f99abbe36b588bdb84719",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1g2TQ50gShtZsJ40gG2FJco652TNBsLt2DWacnVRuWFD",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nGreenfield proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "90e27355a95b043178d6a38616caf1ad",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1FvhRSo2UMECzPm7tbCzClNYJFWTXJtcxk4hRyKcuztL",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Greenfield\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "043c305dabce81a1fe465fb4d051979e",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1MYcfBH1mbOk5yQzxtmEh1prBXnBTOQLAtXXn54e1U9K",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "67e8b81ffdb1eeb39cc26b3a9053c1c7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1Yu5frPIdE4LADqa7KH6DB8cmq2nQqfjQdb4mz5dFCoJ",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "86f8832c09697afb120acde0820c8b81",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "160NkqDGfO1vemlbrSOamiX7fRD7hrHlFXm1tEBilEfn",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 11
    },
    {
        "id": "16FBMVag3EW0BDlLvzFyvlGf76r96H5pcQvZGpoHdxMZ",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1Vwh4el6Dj5loycA9OCdBwGJan3guxmEv2qeSFZSbzNT",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
