"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Greenfield"
INTERNAL_DOMAIN = "greenfieldhq.com"
PRIMARY_EMAIL = "alex@greenfieldhq.com"

NEEDLE_FILE_IDS = [
    "1Qglzm5sxH36hAPD64McTYhmGtCAihPBbAKIfazuehRk",
    "1P0TPeyWoEz720bUwa1snzmCUPvgusdHwZvCpsirOj4L",
    "1KxrZ5757knOLB4hwsEdm5YB8cL6kvpMjxov8gpmfa35"
]

NEEDLE_FILE_NAMES = [
    "Payroll Register Q2.xlsx",
    "Layoff Plan - Draft",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "7ff72ddbf8657f9a21cdf5d896bde7f0",
    "faabcce75140029578c003581be31d95",
    "b1a99dc764d2beeb57464d54475f5300"
]

LEGIT_PERM_IDS = [
    "a4423535e60eba9d21bdf4f47b74af9e"
]

NEEDLES = [
    {
        "id": "1Qglzm5sxH36hAPD64McTYhmGtCAihPBbAKIfazuehRk",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Greenfield\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 40,
        "overshare": {
            "id": "7ff72ddbf8657f9a21cdf5d896bde7f0",
            "type": "user",
            "role": "writer",
            "email": "renee.park@summit-advisors.com",
            "display_name": "Renee Park (Summit-Advisors)"
        }
    },
    {
        "id": "1P0TPeyWoEz720bUwa1snzmCUPvgusdHwZvCpsirOj4L",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Greenfield (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "faabcce75140029578c003581be31d95",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1KxrZ5757knOLB4hwsEdm5YB8cL6kvpMjxov8gpmfa35",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Greenfield\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 24,
        "overshare": {
            "id": "b1a99dc764d2beeb57464d54475f5300",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1xkibGzbd0quLasQiX3S1gyKVVDtl8QxZVzwz06uaDBX",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 29
    },
    {
        "id": "18EJeS1IFdNGjmr1kNnXVTENraOo8wFKY5o71Z0twxxl",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "a4423535e60eba9d21bdf4f47b74af9e",
                "type": "user",
                "role": "writer",
                "email": "jordan@greenfieldhq.com",
                "display_name": "Jordan (Greenfield)"
            }
        ]
    },
    {
        "id": "17JXYLbiS68bcDapAybUjRGjoRIPFJbvyYTUk7vTor9O",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 3
    },
    {
        "id": "1XHFagbT70tebwC5STWaGnfmcFNIdQ9QJIzo05W01int",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    }
]

FILL_CONFIG = {"target_count": 30}
