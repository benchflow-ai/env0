"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Notion"
VENDOR_EMAIL = "billing@notion.so"
TARGET_LABEL = "Notion Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "Jun 2026",
    "May 2026",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for Mar 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: Mar 2026\n'
                      'Total: $96.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for Jun 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: Jun 2026\n'
                      'Total: $12.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for May 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: May 2026\n'
                      'Total: $96.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for Apr 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: Apr 2026\n'
                      'Total: $45.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Action needed: confirm your Notion email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Notion.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Notion',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 13,
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
        'days_ago': 4,
        'role': 'decoy',
        'params': {}}]

GMAIL_FILL_CONFIG = {
    "target_count": 600,
    "include_ambiguous": True,
    "distribution": {
        "notifications": 0.35,
        "newsletters": 0.25,
        "work": 0.20,
        "personal": 0.15,
        "spam": 0.05,
    },
}
