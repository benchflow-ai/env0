"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Notion"
VENDOR_EMAIL = "billing@notion.so"
TARGET_LABEL = "Notion Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Apr 2026",
    "May 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for Apr 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: Apr 2026\n'
                      'Total: $18.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for May 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: May 2026\n'
                      'Total: $12.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'Notion invoice for Mar 2026',
        'body_plain': 'Hello Alex,\n'
                      '\n'
                      'Your Notion workspace was billed.\n'
                      '\n'
                      'Workspace: Personal Pro\n'
                      'Period: Mar 2026\n'
                      'Total: $24.00\n'
                      '\n'
                      'Download invoice: https://notion.so/invoices\n'
                      '\n'
                      '— The Notion Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Notion',
        'sender_email': 'billing@notion.so',
        'subject': 'A new sign-in to your Notion account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Notion account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Notion Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
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
        'days_ago': 19,
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
        'is_read': False,
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
