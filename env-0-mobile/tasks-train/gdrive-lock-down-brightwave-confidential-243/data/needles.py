"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1XzmVKyXNrr8bm6WBi086dKdkAX02dSmwmAnVF6PQAe6",
    "1fqGCNtvziMoZSvmLvaNxadJQ1CCfLJ4a7z5j3KgGLd4",
    "1xmpje0JCxs0RrA3nJeVYQo3QHrY6v4FeJx88s9FaWuw",
    "1Go8n8VR0qZ873cSCCudM4cJIjbnR5FVtly6k4jk3ZRJ",
    "1Roxm0aSePbuWmsK4M3yAURl24RhR3FJkcB5xUjZK3F1"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "3aef72cf12c9ce466908fa51a0429af7",
    "b6e3916e27635680c9885b74d45eb5c9",
    "5f51c26427daf587e6bd61b593210927",
    "f8bfa17c44d1f2fb1078acd4abefeefc",
    "8cf20459bfce96f2f0ac22cac2ed8d18"
]

LEGIT_PERM_IDS = [
    "f01dc0cb0a776df0605028c024cc0235",
    "bd79922613889566da9400f57ee17d6d"
]

NEEDLES = [
    {
        "id": "1XzmVKyXNrr8bm6WBi086dKdkAX02dSmwmAnVF6PQAe6",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 40,
        "overshare": {
            "id": "3aef72cf12c9ce466908fa51a0429af7",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1fqGCNtvziMoZSvmLvaNxadJQ1CCfLJ4a7z5j3KgGLd4",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "b6e3916e27635680c9885b74d45eb5c9",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1xmpje0JCxs0RrA3nJeVYQo3QHrY6v4FeJx88s9FaWuw",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "5f51c26427daf587e6bd61b593210927",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Go8n8VR0qZ873cSCCudM4cJIjbnR5FVtly6k4jk3ZRJ",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 8,
        "overshare": {
            "id": "f8bfa17c44d1f2fb1078acd4abefeefc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1Roxm0aSePbuWmsK4M3yAURl24RhR3FJkcB5xUjZK3F1",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "8cf20459bfce96f2f0ac22cac2ed8d18",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1bqSuMqjI6XzEEQb5sbQFnpRnJxavKRIurOaOqWXrkb1",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1TcfVGZgBq74QOSYcOSJWBuceAmHbDM3MTJqUdlo1gdk",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f01dc0cb0a776df0605028c024cc0235",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1IUmS3t2CXG2FWh4me4nU8L7vPbYKE0WJz188BgM1yEi",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "17ibEDuyCJL0u6qWz7J0oc9WosfjblnM9OHP1vWFYF2V",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "bd79922613889566da9400f57ee17d6d",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
