"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Framer"
VENDOR_EMAIL = "billing@framer.com"
TARGET_LABEL = "Framer Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "Mar 2026",
    "Feb 2026",
    "May 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: May 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Action needed: confirm your Framer email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Framer.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
        'is_read': False,
        'days_ago': 13,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 22,
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
        'is_read': True,
        'days_ago': 22,
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
