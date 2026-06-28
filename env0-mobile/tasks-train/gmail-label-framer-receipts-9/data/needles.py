"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Framer"
VENDOR_EMAIL = "billing@framer.com"
TARGET_LABEL = "Framer Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "May 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': 'Your Framer payment receipt — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Framer plan was charged.\n'
                      '\n'
                      'Plan: Framer Pro\n'
                      'Billing period: May 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
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
                      'Amount: $18.00\n'
                      '\n'
                      'Manage billing: https://framer.com/settings/billing\n'
                      '\n'
                      '— Framer',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Framer',
        'sender_email': 'billing@framer.com',
        'subject': "Framer product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Framer this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Framer Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
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
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
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
