"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "GitHub"
VENDOR_EMAIL = "receipt@github.com"
TARGET_LABEL = "GitHub Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Jun 2026",
    "Mar 2026",
    "Dec 2025",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': '[GitHub] Payment receipt for Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your GitHub payment was successful.\n'
                      '\n'
                      'Period: Feb 2026\n'
                      'Plan: GitHub Pro\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing settings: https://github.com/settings/billing\n'
                      '\n'
                      '— GitHub',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': '[GitHub] Payment receipt for Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your GitHub payment was successful.\n'
                      '\n'
                      'Period: Jun 2026\n'
                      'Plan: GitHub Pro\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing settings: https://github.com/settings/billing\n'
                      '\n'
                      '— GitHub',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': '[GitHub] Payment receipt for Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your GitHub payment was successful.\n'
                      '\n'
                      'Period: Mar 2026\n'
                      'Plan: GitHub Pro\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing settings: https://github.com/settings/billing\n'
                      '\n'
                      '— GitHub',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': '[GitHub] Payment receipt for Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your GitHub payment was successful.\n'
                      '\n'
                      'Period: Dec 2025\n'
                      'Plan: GitHub Pro\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing settings: https://github.com/settings/billing\n'
                      '\n'
                      '— GitHub',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': '[GitHub] Payment receipt for Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your GitHub payment was successful.\n'
                      '\n'
                      'Period: Nov 2025\n'
                      'Plan: GitHub Pro\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing settings: https://github.com/settings/billing\n'
                      '\n'
                      '— GitHub',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'GitHub',
        'sender_email': 'receipt@github.com',
        'subject': 'Action needed: confirm your GitHub email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using GitHub.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— GitHub',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 11,
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
        'is_read': False,
        'days_ago': 4,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 31,
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
