"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Loom"
VENDOR_EMAIL = "billing@loom.com"
TARGET_LABEL = "Loom Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Jan 2026",
    "May 2026",
    "Apr 2026",
    "Jun 2026"
]

NEEDLES = [   {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': 'Your Loom receipt for Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Loom Business plan was charged.\n'
                      '\n'
                      'Billing period: Feb 2026\n'
                      'Seats: 3\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Manage subscription: https://loom.com/settings/billing\n'
                      '\n'
                      '— Loom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': 'Your Loom receipt for Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Loom Business plan was charged.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
                      'Seats: 3\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Manage subscription: https://loom.com/settings/billing\n'
                      '\n'
                      '— Loom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': 'Your Loom receipt for May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Loom Business plan was charged.\n'
                      '\n'
                      'Billing period: May 2026\n'
                      'Seats: 3\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Manage subscription: https://loom.com/settings/billing\n'
                      '\n'
                      '— Loom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': 'Your Loom receipt for Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Loom Business plan was charged.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Seats: 3\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Manage subscription: https://loom.com/settings/billing\n'
                      '\n'
                      '— Loom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': 'Your Loom receipt for Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Loom Business plan was charged.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Seats: 3\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Manage subscription: https://loom.com/settings/billing\n'
                      '\n'
                      '— Loom',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': 'A new sign-in to your Loom account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Loom account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Loom Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': "Loom product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Loom this month. Check out the changelog to '
                      "see what's new.\n"
                      '\n'
                      '— The Loom Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
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
        'is_read': False,
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
