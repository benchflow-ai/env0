"""Seed data for gdoc-search-keyword-index task."""

DOC = "application/vnd.google-apps.document"

# Stable document IDs — opaque join keys between gdrive and gdoc
DOC_BUDGET_PROPOSAL = "1fG8hI9jK0lM1nO2pQ3rS4tU5vW6xY7zA8bC9dE0fG1h"
DOC_PHOENIX_STATUS = "1hI0jK1lM2nO3pQ4rS5tU6vW7xY8zA9bC0dE1fG2hI3j"
DOC_ANNUAL_PLANNING = "1jK2lM3nO4pQ5rS6tU7vW8xY9zA0bC1dE2fG3hI4jK5l"
DOC_VENDOR_EVAL = "1lM4nO5pQ6rS7tU8vW9xY0zA1bC2dE3fG4hI5jK6lM7n"
DOC_FACILITIES_COST = "1qR7sT8uV9wX0yZ1aB2cD3eF4gH5iJ6kL7mN8oP9qR0s"

BUDGET_DOC_IDS = [
    DOC_BUDGET_PROPOSAL, DOC_PHOENIX_STATUS, DOC_ANNUAL_PLANNING,
    DOC_VENDOR_EVAL, DOC_FACILITIES_COST,
]

NEEDLES = [
    {
        "id": DOC_BUDGET_PROPOSAL,
        "name": "Q1 Department Budget Proposal",
        "mimeType": DOC,
        "content_text": """Q1 Department Budget Proposal

Engineering department budget request for Q1 2026.

Personnel: $850,000
Infrastructure: $120,000
Tools and licenses: $45,000
Training budget: $15,000

Total requested budget: $1,030,000

Approved by: Finance Director
""",
        "days_ago": 20,
    },
    {
        "id": DOC_PHOENIX_STATUS,
        "name": "Project Phoenix Status Report",
        "mimeType": DOC,
        # "budget" appears only once, buried in a long status doc — harder
        # for agents that do a quick keyword scan and give up early.
        "content_text": """Project Phoenix Status Report
March 1, 2026

Progress:
- Phase 1 complete (data migration)
- Phase 2 in progress (API redesign)
- Phase 3 planning started (frontend rewrite)

Risks:
- Vendor lock-in with current cloud provider
- Key engineer on paternity leave until April
- Staffing gap on mobile team

Timeline:
- March 15: API freeze
- April 1: Internal beta
- May 1: GA launch

Resource utilization:
- Cloud compute: 78% of allocated capacity
- Current spend is 15% over the planned budget allocation
- Need additional $30,000 for cloud infrastructure

Next steps:
- Sync with finance team by March 10
- Finalize API contracts
- Begin load testing infrastructure
""",
        "days_ago": 17,
    },
    {
        "id": DOC_ANNUAL_PLANNING,
        "name": "Annual Planning Meeting Notes",
        "mimeType": DOC,
        # Uses "budget" but only in context of other topics — title gives
        # no hint this is a budget doc.
        "content_text": """Annual Planning Meeting Notes
February 10, 2026

Attendees: Sarah, Marcus, Alex, Elena

Key topics discussed:
1. Revenue targets for 2026
2. Hiring plan and headcount budget
3. Product roadmap priorities
4. Marketing budget allocation for Q2

Decisions:
- Marketing budget increased by 20% for product launch
- Engineering headcount budget approved for 8 new hires
""",
        "days_ago": 36,
    },
    {
        "id": DOC_VENDOR_EVAL,
        "name": "Vendor Evaluation Summary",
        "mimeType": DOC,
        # "budget" appears twice but only as modifiers, not headings
        "content_text": """Vendor Evaluation Summary

Evaluated 5 vendors for cloud monitoring solution.

Top 3 candidates:
1. DataDog - $2,400/month - best features
2. New Relic - $1,800/month - good value
3. Grafana Cloud - $900/month - budget friendly option

Recommendation: DataDog for production, Grafana for staging.
The budget impact is approximately $28,800/year for DataDog.
""",
        "days_ago": 12,
    },
    {
        # New needle: "budget" appears exactly once, deep in a long doc
        # whose title and opening paragraphs are about facilities/operations.
        # Agents doing fullText search will find it, but agents scanning
        # titles or skimming first paragraphs will miss it.
        "id": DOC_FACILITIES_COST,
        "name": "Facilities Operations Review",
        "mimeType": DOC,
        "content_text": """Facilities Operations Review
March 2026

Overview:
The facilities team completed its quarterly review of all operational
areas including HVAC maintenance, security systems, janitorial services,
and parking lot management.

HVAC:
Preventive maintenance completed on all 12 rooftop units. Unit 7 needs
compressor replacement — vendor quote received at $8,200. Expected
completion by April 15.

Security Systems:
Badge reader firmware updated across all 3 buildings. Camera system
recording retention increased from 30 to 90 days per new policy.
Annual service contract renewed with SecureTech ($42,000/year).

Janitorial:
Switched from CleanCo to BrightSpace effective April 1. New contract
saves $1,200/month with same service level.

Parking:
Employee parking utilization is at 67%. Considering converting level 3
to visitor-only to reduce congestion on levels 1-2.

Financial Summary:
Total facilities spend YTD: $287,000 against an annual budget of
$1.15M. On track for 98% utilization. No variances flagged.

Action Items:
- Approve HVAC compressor replacement (Marcus)
- Review parking proposal with HR (Elena)
- Renew fire suppression inspection contract (Dan)
""",
        "days_ago": 45,
    },
]

NORMAL_FILES = [
    {
        "name": "Team Standup Notes - March 10",
        "mimeType": DOC,
        "content_text": "Sprint progress: 8 of 12 stories complete. No blockers reported. Demo scheduled for Friday.",
        "days_ago": 8,
    },
    {
        "name": "API v2.0 Design Document",
        "mimeType": DOC,
        "content_text": "REST API redesign. New endpoints for user management, authentication, and reporting. GraphQL considered but deferred.",
        "days_ago": 25,
    },
    {
        "name": "Incident Postmortem - March 3",
        "mimeType": DOC,
        "content_text": "Root cause: database connection pool exhaustion. Resolution: increased pool size from 20 to 50. Action items: add monitoring alerts.",
        "days_ago": 15,
    },
    {
        "name": "Code Review Guidelines",
        "mimeType": DOC,
        "content_text": "All PRs require at least 2 approvals. Security-sensitive changes need lead review. Max PR size: 400 lines.",
        "days_ago": 50,
    },
    {
        "name": "Onboarding Checklist",
        "mimeType": DOC,
        "content_text": "Day 1: laptop setup. Day 2: codebase orientation. Day 3: first task assignment. Day 5: 1-on-1 with manager.",
        "days_ago": 40,
    },
    # --- Near-miss decoys: financial context but do NOT mention "budget" ---
    {
        "name": "Q4 Revenue Forecast",
        "mimeType": DOC,
        "content_text": """Q4 Revenue Forecast

Projected revenue for Q4 2026:
- Product sales: $1.2M
- Service contracts: $450K
- Licensing: $200K

Total projected: $1.85M
Variance from plan: +3.2%

Note: finance team to review projections by end of month.
""",
        "days_ago": 14,
    },
    {
        "name": "Compensation Review Process",
        "mimeType": DOC,
        "content_text": """Compensation Review Process

Annual compensation reviews begin April 1.
Managers should prepare salary adjustment recommendations.
Total compensation pool: $2.1M allocated across departments.
Equity refresh grants will be handled separately.

Timeline:
- April 1-15: Manager submissions
- April 16-30: VP approvals
- May 1: Employee notifications
""",
        "days_ago": 22,
    },
    {
        "name": "Office Lease Renewal Terms",
        "mimeType": DOC,
        "content_text": """Office Lease Renewal Terms

Current lease expires June 30, 2026.
Proposed renewal: 3-year term at $18/sq ft (up from $16.50).
Annual cost increase: approximately $45,000.

Landlord requires decision by April 15.
Facilities team recommends renewal — relocation costs would exceed $200K.
""",
        "days_ago": 30,
    },
    {
        # Aggressive decoy: title says "Cost Allocation" and content is
        # heavily financial — talks about spending, funding, allocations —
        # but never uses the word "budget". This should trap agents that
        # over-include based on financial topic matching.
        "name": "Q2 Cost Allocation Proposal",
        "mimeType": DOC,
        "content_text": """Q2 Cost Allocation Proposal

Department: Engineering
Prepared by: Marcus Chen

Proposed cost allocations for Q2 2026:

Cloud Infrastructure:
- AWS spend: $180,000 (up 12% from Q1)
- GCP spend: $45,000 (steady)
- Total compute: $225,000

Staffing Costs:
- Contractor pool: $320,000 (4 contractors x 3 months)
- Recruiting fees: $60,000 (3 open headcount)

Software & Tooling:
- Annual license renewals: $88,000
- New tool evaluations: $12,000

Total proposed allocation: $705,000
Funding source: Engineering operating fund

Approval required from: VP Engineering, Finance Director
Deadline: March 31 for Q2 lock
""",
        "days_ago": 18,
    },
]

FILL_CONFIG = {
    "target_count": 300,
}
