"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1GYJMSpZUTZbW3wMyXgCfG2EoEd350LFPZxsbGlz3mgI",
    "1WYR132pu1ddPNUfppPeMVYJAdxZZZZuVCoq6LzcwCBa",
    "1BGTfv4mOHMvOid3YA2Bup60X3PX57fpvfiCj3Pomr8I"
]

NEEDLE_FILE_NAMES = [
    "Series A Cap Table.xlsx",
    "Payroll Register Q2.xlsx",
    "prod-secrets.env"
]

OVERSHARE_PERM_IDS = [
    "c9adeddfc20a44b6ef5cb72c1c0d1164",
    "32d0b1305db5b3c09ea28db96196cd0c",
    "2e6106375f3228c9321553c7c4d52d8a"
]

LEGIT_PERM_IDS = [
    "3c23217c41d21d2a0be22a907b18b5cb",
    "77febe514377a452d088eada91d23939"
]

NEEDLES = [
    {
        "id": "1GYJMSpZUTZbW3wMyXgCfG2EoEd350LFPZxsbGlz3mgI",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "c9adeddfc20a44b6ef5cb72c1c0d1164",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1WYR132pu1ddPNUfppPeMVYJAdxZZZZuVCoq6LzcwCBa",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "32d0b1305db5b3c09ea28db96196cd0c",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1BGTfv4mOHMvOid3YA2Bup60X3PX57fpvfiCj3Pomr8I",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Cardinal production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "2e6106375f3228c9321553c7c4d52d8a",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Tn2TbpAiZxZBeocQpihABiGgNNGK4KTsvDyt5b9ZwVp",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "14YHhEBZJF2WOsbaKnKU5MTsDlCFALvLHcySgqOJFYiD",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "3c23217c41d21d2a0be22a907b18b5cb",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    },
    {
        "id": "1eaS6Sr4veN4c1tcR5vgU9gQFMbFL1uikrK2prMldYKr",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1MELIhzNaxsFPP8lPVZ1NCr9n6oOIBPmHMFlRjwqJrvP",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "77febe514377a452d088eada91d23939",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 50}
