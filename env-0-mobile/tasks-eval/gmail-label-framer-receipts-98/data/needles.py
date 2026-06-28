"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Framer"
VENDOR_EMAIL = "billing@framer.com"
TARGET_LABEL = "Framer Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "May 2026",
    "Mar 2026",
    "Apr 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: May 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $96.00\n'
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
        'subject': 'Your Framer payment receipt — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'A new sign-in to your Framer account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Framer account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Framer Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 22,
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
        'days_ago': 31,
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
        'days_ago': 31,
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
