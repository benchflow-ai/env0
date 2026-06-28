"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Atlassian"
VENDOR_EMAIL = "billing@atlassian.com"
TARGET_LABEL = "Atlassian Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Apr 2026",
    "Dec 2025",
    "Mar 2026",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Nov 2025\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Apr 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Dec 2025\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Mar 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Feb 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': "Atlassian product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Atlassian this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The Atlassian Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Spotify',
        'sender_email': 'receipts@spotify.com',
        'subject': 'Your Spotify Premium receipt',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Spotify Premium subscription renewed. Amount: $11.99.\n'
                      '\n'
                      '— Spotify',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 4,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Adobe',
        'sender_email': 'billing@adobe.com',
        'subject': 'Adobe Creative Cloud invoice',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Creative Cloud plan was billed $54.99 this month.\n'
                      '\n'
                      '— Adobe',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': '1Password',
        'sender_email': 'receipts@1password.com',
        'subject': 'Your 1Password receipt',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your 1Password Families plan renewed for $4.99/mo.\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 22,
        'role': 'decoy',
        'params': {}}]

GMAIL_FILL_CONFIG = {
    "target_count": 400,
    "include_ambiguous": True,
    "distribution": {
        "notifications": 0.35,
        "newsletters": 0.25,
        "work": 0.20,
        "personal": 0.15,
        "spam": 0.05,
    },
}
