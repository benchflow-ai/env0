"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "13ZOFI6wLTy1vkQkGrw2KN8inPJjfm8DkejQKZ2b1WNs",
    "1xXFCsKP1AYhWzndqFBWaoRnXFKuRthms4mURMJHr5wu",
    "103EzQZ6IpkskmNaqiSJmpOdDvpT2SGaodLtMXGC4z9U",
    "1KlHtNspW0VGgpUZxwdf5UcLGbhLxuirLa7uzpfh4yNv",
    "1y0fzLzEVeTQsijuJuWdZQYOWdnCRYy4gYTUw7boSYgu"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "d5e5252c73ec70aa23bab5847fb248f3",
    "f2472dbe484af46659153b06af406cc1",
    "ece10de1f392b558bce85db3c9dbda8b",
    "f1e164f01e95f8d50b4bee555e5af6a2",
    "e684b9bbe8c428b89d1f262555303ea0"
]

LEGIT_PERM_IDS = [
    "d23897ae6291f9c39854be4fe2dc90b8",
    "f39a23e8b151a24967bc9d41743e04f0"
]

NEEDLES = [
    {
        "id": "13ZOFI6wLTy1vkQkGrw2KN8inPJjfm8DkejQKZ2b1WNs",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "d5e5252c73ec70aa23bab5847fb248f3",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xXFCsKP1AYhWzndqFBWaoRnXFKuRthms4mURMJHr5wu",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "f2472dbe484af46659153b06af406cc1",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "103EzQZ6IpkskmNaqiSJmpOdDvpT2SGaodLtMXGC4z9U",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Stellar Works production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "ece10de1f392b558bce85db3c9dbda8b",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1KlHtNspW0VGgpUZxwdf5UcLGbhLxuirLa7uzpfh4yNv",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "f1e164f01e95f8d50b4bee555e5af6a2",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1y0fzLzEVeTQsijuJuWdZQYOWdnCRYy4gYTUw7boSYgu",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Stellar Works\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "e684b9bbe8c428b89d1f262555303ea0",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1wYUKhZgkWo0092fZCN6spG6DIk7LjlSyTIVhFEPExGC",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d23897ae6291f9c39854be4fe2dc90b8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1usdZTRGd4WTIRmLZDtHG1bZCn0v7v60f2UEQbmuH3Ag",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f39a23e8b151a24967bc9d41743e04f0",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1fx4Is9uWRnPFV2BSC4kmS42UvRaUeeK47IsOLwhIWd6",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "18OfjrcxdDik3aZQuPOOvWYNsh9i5fbYa1djKDfisV0Q",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "1Gi8gijyoHchMvakYoxnrhDL6eplFEX7Xi5wemvd6G2s",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 50}
