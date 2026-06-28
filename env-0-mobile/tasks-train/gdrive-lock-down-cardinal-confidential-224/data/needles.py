"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Cardinal"
INTERNAL_DOMAIN = "cardinaldata.com"
PRIMARY_EMAIL = "alex@cardinaldata.com"

NEEDLE_FILE_IDS = [
    "1FitKIyVKMCgGr5CBQwwkfolNGRUOS0gEnMCOdfpK0S0",
    "1WHh0MQuKoStC6keQm94sFOr7ayxxL53J0NmyGxTaJhx",
    "1TWZOwKE33i8mlqOauJJ0D1BeeyxrEZPH6TALRVAFiPN"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "1afc2e771709cdfc6f2bc9d3347951f7",
    "d6df804809b3927a5004e39664a7199b",
    "9a489f8260e79d0f5d13fff426109eb1"
]

LEGIT_PERM_IDS = [
    "15003558a88674af8885bed2c5a28ab8",
    "a6ade3fdb14f181178d43ba3efe3591d",
    "047e5add9798d789ca249392a8a1c3a7"
]

NEEDLES = [
    {
        "id": "1FitKIyVKMCgGr5CBQwwkfolNGRUOS0gEnMCOdfpK0S0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Cardinal (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 40,
        "overshare": {
            "id": "1afc2e771709cdfc6f2bc9d3347951f7",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1WHh0MQuKoStC6keQm94sFOr7ayxxL53J0NmyGxTaJhx",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Cardinal\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 8,
        "overshare": {
            "id": "d6df804809b3927a5004e39664a7199b",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1TWZOwKE33i8mlqOauJJ0D1BeeyxrEZPH6TALRVAFiPN",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Cardinal\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 40,
        "overshare": {
            "id": "9a489f8260e79d0f5d13fff426109eb1",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "11CCiEYftqSDRK3xKoOvHt6S0eKqwksZvf1jdw2HzSeO",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "15003558a88674af8885bed2c5a28ab8",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1VO94S1J6pkDBeZQ1KuCMLx4bPe1IaytkZqoUXwQJTDb",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "a6ade3fdb14f181178d43ba3efe3591d",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1xCmS6JzWYkSB9kvrTWIzkVwkxkDzWy1jhjQEaSyStw6",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1N40ETh87t68lObHGoKH94slldHe23e2eSZ7uV3V1CSf",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    },
    {
        "id": "1g55FhhIyql9HNccvt7ZPoajvZtjltQ3f6g9xY9WJNcO",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "047e5add9798d789ca249392a8a1c3a7",
                "type": "user",
                "role": "writer",
                "email": "jordan@cardinaldata.com",
                "display_name": "Jordan (Cardinal)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
