"""Auto-generated env-0 tasks-lite needle data (gdrive revoke oversharing).
Dependency-free; consumed by the gdrive seeder and the evaluator."""

COMPANY = "Harborline"
INTERNAL_DOMAIN = "harborline.com"
PRIMARY_EMAIL = "alex@harborline.com"

NEEDLE_FILE_IDS = [
    "18LkDMAtP8jVsh3WaAdWn9q7lYdatrBHLtt2WV0ofSyc",
    "1rE2cAhMrSq9mcHsz5XAwfbXG4WUeVkrQox1YCDiCnUU",
    "1UxRLR8Iv6sjfrzjvDkMbHM2hTOGGh6cSapWdVSRyQOp"
]

NEEDLE_FILE_NAMES = [
    "prod-secrets.env",
    "Layoff Plan - Draft",
    "Acquisition LOI - Project Falcon"
]

OVERSHARE_PERM_IDS = [
    "4d79229e955231a7d6e08f2b925eccee",
    "0552ece9f8bd7a02bd888a5f40ca71d3",
    "521c66a612df736240c6cdf346377a05"
]

LEGIT_PERM_IDS = [
    "e7a33c138478f2b00032b78cc405eda1",
    "9a050e921b75ec1361954780d90b8b3b"
]

NEEDLES = [
    {
        "id": "18LkDMAtP8jVsh3WaAdWn9q7lYdatrBHLtt2WV0ofSyc",
        "name": "prod-secrets.env",
        "mimeType": "text/plain",
        "folder": "Engineering/Config",
        "content_text": "# Harborline production secrets - DO NOT SHARE\nDATABASE_URL=postgres://admin:hunter2@db.internal:5432/prod\nJWT_SIGNING_KEY=eyJhbGciOiJIUzI1Niw9\nSENDGRID_API_KEY=SG.live.0a1b2c3d4e5f\n",
        "days_ago": 24,
        "overshare": {
            "id": "4d79229e955231a7d6e08f2b925eccee",
            "type": "anyone",
            "role": "reader"
        }
    },
    {
        "id": "1rE2cAhMrSq9mcHsz5XAwfbXG4WUeVkrQox1YCDiCnUU",
        "name": "Layoff Plan - Draft",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "HR/Confidential",
        "content_text": "RIF Planning - Harborline (DRAFT)\n\nProposed reductions: 8 roles across Sales & Ops.\nSeverance: 10 weeks. Comms embargo until board sign-off.\n",
        "days_ago": 8,
        "overshare": {
            "id": "0552ece9f8bd7a02bd888a5f40ca71d3",
            "type": "user",
            "role": "reader",
            "email": "carmen@lighthouse-consult.com",
            "display_name": "Carmen Ortiz (Lighthouse-Consult)"
        }
    },
    {
        "id": "1UxRLR8Iv6sjfrzjvDkMbHM2hTOGGh6cSapWdVSRyQOp",
        "name": "Acquisition LOI - Project Falcon",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Corp Dev",
        "content_text": "Letter of Intent - Project Falcon\n\nHarborline proposes to acquire the target\nfor $11.5M in cash and stock. Diligence period: 45 days.\nSTRICTLY CONFIDENTIAL - do not circulate.\n",
        "days_ago": 8,
        "overshare": {
            "id": "521c66a612df736240c6cdf346377a05",
            "type": "anyone",
            "role": "reader"
        }
    }
]

NORMAL_FILES = [
    {
        "id": "1Ahw4qpuNDE9tOKin7JRYCcNNydsdPP2jibPupi0VWPI",
        "name": "Weekly Sync Agenda",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Team",
        "content_text": "Weekly Sync\n1. Wins\n2. Blockers\n3. Next steps\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "e7a33c138478f2b00032b78cc405eda1",
                "type": "user",
                "role": "writer",
                "email": "jordan@harborline.com",
                "display_name": "Jordan (Harborline)"
            }
        ]
    },
    {
        "id": "12i6Rn5zT0uz9P5xrnLFzgXNfmbJtSo4tP1XXUOtF2xM",
        "name": "Onboarding Checklist",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "People/Onboarding",
        "content_text": "New Hire Checklist\n\n[ ] Laptop\n[ ] Accounts\n[ ] Buddy assigned\n",
        "days_ago": 11
    },
    {
        "id": "1dQqDPB7ViksrjnX2FKXDEf03TMtCLlUXLKkRuGJivdY",
        "name": "Customer Webinar Slides",
        "mimeType": "application/vnd.google-apps.document",
        "folder": "Marketing/Events",
        "content_text": "Webinar: Getting Started\nShared publicly on purpose for registrants.\n",
        "days_ago": 11,
        "shared_with": [
            {
                "id": "9a050e921b75ec1361954780d90b8b3b",
                "type": "anyone",
                "role": "reader"
            }
        ]
    },
    {
        "id": "1l9M0dfPEtfwITa9p8hqRuz4NsomHxYS4hgieodeJ3eN",
        "name": "Office Seating Map",
        "mimeType": "application/vnd.google-apps.spreadsheet",
        "folder": "Facilities",
        "content_text": "Floor 3 Seating\n\nDesk\tName\n3A\tA. Rivera\n3B\tB. Cho\n",
        "days_ago": 29
    }
]

FILL_CONFIG = {"target_count": 30}
