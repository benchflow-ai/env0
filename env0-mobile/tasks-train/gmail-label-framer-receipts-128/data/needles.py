"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Framer"
VENDOR_EMAIL = "billing@framer.com"
TARGET_LABEL = "Framer Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jan 2026",
    "Jun 2026",
    "Nov 2025",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Nov 2025',
        'body_plain': 'Hi Alex,\n'
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
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Feb 2026',
        'body_plain': 'Hi Alex,\n'
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
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Action needed: confirm your Framer email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Framer.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'A new sign-in to your Framer account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Framer account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Framer Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
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
