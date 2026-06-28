"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Brightwave"
INTERNAL_DOMAIN = "brightwave.io"
PRIMARY_EMAIL = "alex@brightwave.io"

NEEDLE_FILE_IDS = [
    "1YVXlJXd33FWBPGn0U29pwr7lnyLKohfdjojPChetHh9",
    "1fcplPT3YpeHSpx72FTPg3C0drpnDBAhqglHOrPb5k9T",
    "1Q29rm2p7UwJ392E4cBWqN8HsiYJeZLngMgJ8wJi6nQn",
    "1iZbVsycN0sgmixr7BRwyCf4mj8VGKXoaSIADLBxmaxt",
    "1ndOY3gjDUUqULSfop5IIUvkt8rxffkl3IWPflHL0Tbr"
]

NEEDLE_FILE_NAMES = [
    "Board Deck Q2 (final)",
    "Payroll Register Q2.xlsx",
    "Acquisition LOI - Project Falcon",
    "prod-secrets.env",
    "Layoff Plan - Draft"
]

OVERSHARE_PERM_IDS = [
    "95fda527f98e7228fb5517cb22a1f797",
    "ef8e8b6e3d8ae3130f9220ff3abd382f",
    "5d762b8abe14b2585aff2b4268077239",
    "53334f6e0ef5f9f0ade096d4a139ecfc",
    "e33a69c4149d5a1025e3ce454d3eb472"
]

LEGIT_PERM_IDS = [
    "02901559675aaef9e4906ae06eb380ce",
    "2351a8fda96b502923af9841d39052a3"
]

NEEDLES = [
    {
        "id": "1YVXlJXd33FWBPGn0U29pwr7lnyLKohfdjojPChetHh9",
        "name": "Board Deck Q2 (final)",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Board",
        "content_text": "Board Deck Q2 - Brightwave\n\nARR: $5.8M (+41% YoY)\nNet burn: $310K/mo\nRunway: 16 months. Raising Series B in Q4 at ~$180M pre.\n",
        "days_ago": 17,
        "overshare": {
            "id": "95fda527f98e7228fb5517cb22a1f797",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1fcplPT3YpeHSpx72FTPg3C0drpnDBAhqglHOrPb5k9T",
        "name": "Payroll Register Q2.xlsx",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "HR",
        "content_text": "Payroll Register Q2 - Brightwave\n\nEmployee\tBase\tBonus\nA. Rivera\t$162,000\t$18,000\nB. Cho\t$148,000\t$12,000\nC. Nwosu\t$139,000\t$9,000\n",
        "days_ago": 17,
        "overshare": {
            "id": "ef8e8b6e3d8ae3130f9220ff3abd382f",
            "type": "user",
            "role": "writer",
            "email": "omar@northstar-vc.com",
            "display_name": "Omar Haddad (Northstar-Vc)"
        }
    },
    {
        "id": "1Q29rm2p7UwJ392E4cBWqN8HsiYJeZLngMgJ8wJi6nQn",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nBrightwave proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 24,
        "overshare": {
            "id": "5d762b8abe14b2585aff2b4268077239",
            "type": "user",
            "role": "reader",
            "email": "dylan.brooks@vantagecap.com",
            "display_name": "Dylan Brooks (Vantagecap)"
        }
    },
    {
        "id": "1iZbVsycN0sgmixr7BRwyCf4mj8VGKXoaSIADLBxmaxt",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Brightwave production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 17,
        "overshare": {
            "id": "53334f6e0ef5f9f0ade096d4a139ecfc",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1ndOY3gjDUUqULSfop5IIUvkt8rxffkl3IWPflHL0Tbr",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Brightwave (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "e33a69c4149d5a1025e3ce454d3eb472",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "17lNtsl5nwnYhsyItrWRwtpl5oeKi1Ve2cCnCwwTWGEk",
        "name": "Vendor Contact List",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Ops",
        "content_text": "Vendor\tContact\nAcme Supplies\tsales@acme.test\n",
        "days_ago": 11
    },
    {
        "id": "16fnpfUimA73VFHjgNsuVWdDO83Ly15uK3avd6o8SDMP",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "02901559675aaef9e4906ae06eb380ce",
                "type": "user",
                "role": "writer",
                "email": "jordan@brightwave.io",
                "display_name": "Jordan (Brightwave)"
            }
        ]
    },
    {
        "id": "1jnuwmevWFHdCqRJ2Fdk1xiw2ktL2EIcGO6JmEiU97Av",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 3
    },
    {
        "id": "1cRSSxqDvuuBifurvKTMQDxasembMXCySACRttjYXyzh",
        "name": "Public Blog Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Content",
        "content_text": "DRAFT: 5 lessons from our first year. Shared for editor feedback.\n",
        "days_ago": 29,
        "shared_with": [
            {
                "id": "2351a8fda96b502923af9841d39052a3",
                "type": "anyone",
                "role": "reader"
            }
        ]
    }
]

FILL_CONFIG = {"target_count": 30}
