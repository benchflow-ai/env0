"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Atlassian"
VENDOR_EMAIL = "billing@atlassian.com"
TARGET_LABEL = "Atlassian Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Jun 2026",
    "May 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Feb 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Jun 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: May 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Dec 2025\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'A new sign-in to your Atlassian account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Atlassian account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Atlassian Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': "Atlassian product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Atlassian this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The Atlassian Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Adobe',
        'sender_email': 'billing@adobe.com',
        'subject': 'Adobe Creative Cloud invoice',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Creative Cloud plan was billed $54.99 this month.\n'
                      '\n'
                      '— Adobe',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Spotify',
        'sender_email': 'receipts@spotify.com',
        'subject': 'Your Spotify Premium receipt',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Spotify Premium subscription renewed. Amount: $11.99.\n'
                      '\n'
                      '— Spotify',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 4,
        'role': 'decoy',
        'params': {}}]

GMAIL_FILL_CONFIG = {
    "target_count": 800,
    "include_ambiguous": True,
    "distribution": {
        "notifications": 0.35,
        "newsletters": 0.25,
        "work": 0.20,
        "personal": 0.15,
        "spam": 0.05,
    },
}
