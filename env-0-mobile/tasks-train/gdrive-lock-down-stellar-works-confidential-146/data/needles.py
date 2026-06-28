"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Stellar Works"
INTERNAL_DOMAIN = "stellarworks.io"
PRIMARY_EMAIL = "alex@stellarworks.io"

NEEDLE_FILE_IDS = [
    "15C3WML84SG3k6n7Jo7QVZHqPxN6RTtB62XEY1q9tjlI",
    "165Qj990cVBjThovLxZ1rmQzHsC3ELAhSj6FosGhjA18",
    "11NAQTmAQpCUtqDFDpYPyb75NVNBuxcK17dmPecHzB5A"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "96549951a21676167026e1d8732b8494",
    "05decd800101629753cec0ba37a13492",
    "044155edc30f7100b23de4675154923e"
]

LEGIT_PERM_IDS = [
    "133001e3750806fdb100aed4c27471d7",
    "a9b29ceb01e1ed5a0abde92b330b4b73"
]

NEEDLES = [
    {
        "id": "15C3WML84SG3k6n7Jo7QVZHqPxN6RTtB62XEY1q9tjlI",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Stellar Works\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "96549951a21676167026e1d8732b8494",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "165Qj990cVBjThovLxZ1rmQzHsC3ELAhSj6FosGhjA18",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Stellar Works (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 17,
        "overshare": {
            "id": "05decd800101629753cec0ba37a13492",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "11NAQTmAQpCUtqDFDpYPyb75NVNBuxcK17dmPecHzB5A",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Stellar Works\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 8,
        "overshare": {
            "id": "044155edc30f7100b23de4675154923e",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1euLiVi3rnz86iEwkLRdiwwnbVdWE49RFSB0AkMih1ve",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "133001e3750806fdb100aed4c27471d7",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1ALujNjXZAcFHpw33nx5fEol1dgvqoy3e4W5xpBqIxYN",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1NbD5aqgeLUqvoVBKrLNzVTUJ75GB9fckZtt4xNRdCep",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "a9b29ceb01e1ed5a0abde92b330b4b73",
                "type": "user",
                "role": "writer",
                "email": "jordan@stellarworks.io",
                "display_name": "Jordan (Stellar Works)"
            }
        ]
    },
    {
        "id": "1dXj3jm7C2IeR8zvaSoazMWd4zGqsLNIK1Ad4jFmhCcA",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    }
]

FILL_CONFIG = {"target_count": 40}
