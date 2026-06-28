"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1D2olUDPI6Odz9GY4KI4pv1RCpIwOZiNwntdbJUaGYP9",
    "11Iu8RW8Jl3bU5PfAKHuT87l0a1DCFEHWscdkHB9zrX2",
    "1e2KiTNd912VfJkJooizfTvLJ6yoJX2UavJojuVOKbPk",
    "1UPzQxAtz7pAhgWmKc9KkGEvaAggGcYBm5MH84sbMAYi"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "prod-secrets.env",
    "Acquisition LOI - Project Falcon",
    "Board Deck Q2 (final)"
]

OVERSHARE_PERM_IDS = [
    "e25eca6f72a84dc2402ed0e7e05d82e8",
    "07ed0442fe5b45ccc7ed9e4a27b62149",
    "cfb60ec3ed75bb85476c725020f5468a",
    "f2264791a0d113ca27aa07e17df5e68d"
]

LEGIT_PERM_IDS = [
    "299ad09b0a23d6fe1893b9436489532b",
    "79593b2fa5d1bdc755eec2dd9ae838f6",
    "f38ca14d5965d9f5dcd6f72898bfc12c"
]

NEEDLES = [
    {
        "id": "1D2olUDPI6Odz9GY4KI4pv1RCpIwOZiNwntdbJUaGYP9",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "e25eca6f72a84dc2402ed0e7e05d82e8",
            "type": "user",
            "role": "writer",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "11Iu8RW8Jl3bU5PfAKHuT87l0a1DCFEHWscdkHB9zrX2",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 40,
        "overshare": {
            "id": "07ed0442fe5b45ccc7ed9e4a27b62149",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1e2KiTNd912VfJkJooizfTvLJ6yoJX2UavJojuVOKbPk",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nCardinal proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "cfb60ec3ed75bb85476c725020f5468a",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1UPzQxAtz7pAhgWmKc9KkGEvaAggGcYBm5MH84sbMAYi",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Cardinal\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "f2264791a0d113ca27aa07e17df5e68d",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1IZGQhFYv44IfRFUhcxkW8mDwWXNTKKFWi7kHItMqO8a",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1yS4Igw9E8puZ4E8kdUMIwsjVox8YGsIldu4uQAgSRSP",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "299ad09b0a23d6fe1893b9436489532b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1U96rIt3bobqSWN3SGyIhINd8me2L2JBirpt9bhZY6RW",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "79593b2fa5d1bdc755eec2dd9ae838f6",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1fTpspN8ibhGtimUgIMl8jejKcVasiYBjz3BmB7luDyx",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 11
    },
    {
        "id": "1Ejt8hZznHKlkpcQtB9zYyKt5VsCgfl6XiRAuNAsl3a8",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1HRrZLgILNhKcjTrbpNrTWcSEwl2r5GMWS9iVcR8FmUk",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "f38ca14d5965d9f5dcd6f72898bfc12c",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
