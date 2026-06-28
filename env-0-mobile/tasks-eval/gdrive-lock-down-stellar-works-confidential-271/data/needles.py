"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "1LlLsa0XxNnOcL94vQC6si6QKAItliHhzMD1m3S8j5QU",
    "12v1uKC0FrNcJG4yM2fMpA9vZLsUuvFAHLMdpjLEooUf",
    "1CnSfBplJOlAZ78lzDKyVYyuVPpC5nqmLDNtYrHVdR71"
]

NEEDLE_FILE_NAMES = [
    "Acquisition LOI - Project Falcon",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "6effffebaead80edd561583e19705b17",
    "35236c1dd01b5d15fd4adf93ee91a983",
    "3d35403858168efba3b5783eb011d69a"
]

LEGIT_PERM_IDS = [
    "7117b0627aaef38e916a446e9252c264",
    "b4de9315bedb654af67a34f5b03f94ce",
    "7facf6df8a1a77103fe7a795e92332ff"
]

NEEDLES = [
    {
        "id": "1LlLsa0XxNnOcL94vQC6si6QKAItliHhzMD1m3S8j5QU",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nStellar Works proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 17,
        "overshare": {
            "id": "6effffebaead80edd561583e19705b17",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "12v1uKC0FrNcJG4yM2fMpA9vZLsUuvFAHLMdpjLEooUf",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "35236c1dd01b5d15fd4adf93ee91a983",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    },
    {
        "id": "1CnSfBplJOlAZ78lzDKyVYyuVPpC5nqmLDNtYrHVdR71",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "3d35403858168efba3b5783eb011d69a",
            "type": "user",
            "role": "reader",
            "email": "tasha.greene@oakridge-pe.com",
            "display_name": "Tasha Greene (Oakridge-Pe)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1FPfAIjeGleimhLzDi18t72a7Sz32UFVoEv1aupZNwvB",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "7117b0627aaef38e916a446e9252c264",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1svs2RQi5MF7FcXRuKZs3NTbDiN8YAwNpV3HMPKu1Htl",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "11WarkBOImdUTqpD1SLD5pJvN1PncXINEPwSYkNNR5xs",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "b4de9315bedb654af67a34f5b03f94ce",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1wjfKcquFnjt3v1kijF6uyaB13UzwhqfZDA3ZT4SRdmm",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1u7ohKu1IGecAVDX57ukCS2TWIymtjK7slq7x4y2NPX5",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "7facf6df8a1a77103fe7a795e92332ff",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
