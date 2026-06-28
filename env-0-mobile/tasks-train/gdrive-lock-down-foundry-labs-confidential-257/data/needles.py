"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Foundry Labs"
INTERNAL_DOMAIN = "foundrylabs.co"
PRIMARY_EMAIL = "alex@foundrylabs.co"

NEEDLE_FILE_IDS = [
    "1L9RdDSqwUT9ImdkiX8RI6nOBbmFP9Sc6Dyw3arUFdCs",
    "1IrsUmYFFszpJG9znKmNedRzBj1RtNDtXw9gPMKr9N0c",
    "1UZrWvwUZuAZwxU7KuADWhyQvPZh8di622hYMgjsVx8b",
    "1ZL2EHnxOtGnrBipTtHjPW0MOF66muBkJBWEeUUfL8fc"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Board Deck Q2 (final)",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "1a20c74615326de6aefdc42b115ab660",
    "edf43c6a20e656d38ee1a8361803cb31",
    "758ffa791615c8275baae1ef62bbe844",
    "a8ae23fdd62847b6234a135359587ef9"
]

LEGIT_PERM_IDS = [
    "4f0919a5fa238a34f5d52c4a5d088160",
    "d44c10bb4bcd99ffb48165c85b051d35"
]

NEEDLES = [
    {
        "id": "1L9RdDSqwUT9ImdkiX8RI6nOBbmFP9Sc6Dyw3arUFdCs",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Foundry Labs\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "1a20c74615326de6aefdc42b115ab660",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1IrsUmYFFszpJG9znKmNedRzBj1RtNDtXw9gPMKr9N0c",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Foundry Labs (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 24,
        "overshare": {
            "id": "edf43c6a20e656d38ee1a8361803cb31",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1UZrWvwUZuAZwxU7KuADWhyQvPZh8di622hYMgjsVx8b",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Foundry Labs\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "758ffa791615c8275baae1ef62bbe844",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ZL2EHnxOtGnrBipTtHjPW0MOF66muBkJBWEeUUfL8fc",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Foundry Labs\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "a8ae23fdd62847b6234a135359587ef9",
            "type": "user",
            "role": "writer",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1AuhvRsxNzjTGcZ7MUoJyoN9yMctELmkl0oiQME9ulUn",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1ZRsDt1NmlZ9qwVySuH1IiOOvOj4QVno1crknfU7ZYe0",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 29
    },
    {
        "id": "1TBjyR8ZQlOqMRI1OKZltT00nN0fwXpvM23ATxrDcT6q",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "4f0919a5fa238a34f5d52c4a5d088160",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1bMzhnCby2MSOq6uKSvnblElZwZFYEp6Bc9Zay2jtYmK",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "d44c10bb4bcd99ffb48165c85b051d35",
                "type": "user",
                "role": "writer",
                "email": "jordan@foundrylabs.co",
                "display_name": "Jordan (Foundry Labs)"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 40}
