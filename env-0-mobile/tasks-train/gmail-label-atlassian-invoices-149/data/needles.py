"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Atlassian"
VENDOR_EMAIL = "billing@atlassian.com"
TARGET_LABEL = "Atlassian Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Mar 2026",
    "Jan 2026",
    "May 2026",
    "Jun 2026"
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
                      'Amount: $45.00\n'
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
        'subject': 'Your Atlassian invoice — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Mar 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Atlassian subscription has been invoiced.\n'
                      '\n'
                      'Products: Jira, Confluence\n'
                      'Period: Jan 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Manage billing: https://admin.atlassian.com/billing\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Your Atlassian invoice — May 2026',
        'body_plain': 'Hi there,\n'
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
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
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
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Atlassian',
        'sender_email': 'billing@atlassian.com',
        'subject': 'Action needed: confirm your Atlassian email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Atlassian.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Atlassian',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 13,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': '1Password',
        'sender_email': 'receipts@1password.com',
        'subject': 'Your 1Password receipt',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your 1Password Families plan renewed for $4.99/mo.\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 31,
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
