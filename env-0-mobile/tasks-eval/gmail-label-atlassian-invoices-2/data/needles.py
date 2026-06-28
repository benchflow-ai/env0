"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Atlassian"
VENDOR_EMAIL = "billing@atlassian.com"
TARGET_LABEL = "Atlassian Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Jun 2026",
    "Nov 2025",
    "Dec 2025",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
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
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Jun 2026\n'
                      'Amount: $24.00\n'
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
        'subject': 'Your Atlassian invoice — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Nov 2025\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Dec 2025\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: May 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
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
        'is_read': True,
        'days_ago': 28,
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
        'is_read': True,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 13,
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
