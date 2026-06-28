"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1HJSlbyGJWlU3a9naPkMVaHtd4MNWz9u4TQzhDlN8wk0",
    "1o4LSrFTuoOtqyXsoSW9DkJXzvi1IemGUuW44vfei9p2",
    "1rrNDbr30EzbyH7WOBdNIUIifdM12TGE3w1AQekekjCz",
    "1SvvrvSrwwvqolkoEw0tBFiHRuPwGzvTOToR86enyLFn"
]

NEEDLE_FILE_NAMES = [
    "Layoff Plan - Draft",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "Series A Cap Table.xlsx"
]

OVERSHARE_PERM_IDS = [
    "81b9e19f03e60331afa307ba53c5bb54",
    "c13e56ea11bb7c59bbc1945671283144",
    "f572c7d41950e3c696397419e756ec3f",
    "5944c1cb91c14c0148b4d12514b4a553"
]

LEGIT_PERM_IDS = [
    "3aecbf61b332f9d99fd48ecd8bac13b0"
]

NEEDLES = [
    {
        "id": "1HJSlbyGJWlU3a9naPkMVaHtd4MNWz9u4TQzhDlN8wk0",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "81b9e19f03e60331afa307ba53c5bb54",
            "type": "user",
            "role": "reader",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1o4LSrFTuoOtqyXsoSW9DkJXzvi1IemGUuW44vfei9p2",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 24,
        "overshare": {
            "id": "c13e56ea11bb7c59bbc1945671283144",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1rrNDbr30EzbyH7WOBdNIUIifdM12TGE3w1AQekekjCz",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "f572c7d41950e3c696397419e756ec3f",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1SvvrvSrwwvqolkoEw0tBFiHRuPwGzvTOToR86enyLFn",
        "name": "Series A Cap Table.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Finance",
        "content_text": "Cap Table - Brightwave\n\nShareholder\tShares\t%Ownership\nFounders\t6,000,000\t60%\nSeed Investors\t2,500,000\t25%\nOption Pool\t1,500,000\t15%\n\nPost-money valuation: $42M\n",
        "days_ago": 17,
        "overshare": {
            "id": "5944c1cb91c14c0148b4d12514b4a553",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Wd87ZdGdrsiG7vSW3eE9whwo8TmJ37WtK1ydGGUhVrf",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 3
    },
    {
        "id": "1OhnJaIRGYyi6SvuNq2yCVSXpnXsVwrqIQHzcrCmqnYY",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 3,
        "shared_with": [
            {
                "id": "3aecbf61b332f9d99fd48ecd8bac13b0",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1NG3OTC25i2hSFPfqgO3dfrc4bGPULnWF2JHUmntNiEw",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    },
    {
        "id": "1OsdisKAubmhrK3T1f5ByPiFoqgaxLPsts9OfIjiuSQx",
        "name": "Brand Color Palette",
        "mimeType": "application/pdf",
        "folder": "Marketing/Brand",
        "content_text": "Brand Colors\nPrimary #0F62FE\nAccent #FF7A59\n",
        "days_ago": 3
    },
    {
        "id": "1P28wfsPjb7NSJ7xJNzUTdUJthFmDlpSeUDPKW77BACH",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 50}
