"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Loom"
VENDOR_EMAIL = "billing@loom.com"
TARGET_LABEL = "Loom Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "May 2026",
    "Jan 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': 'Your Loom receipt for Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Loom Business plan was charged.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Seats: 3\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Manage subscription: https://loom.com/settings/billing\n'
                      '\n'
                      '— Loom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
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
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': 'Your Loom receipt for Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Loom Business plan was charged.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
                      'Seats: 3\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Manage subscription: https://loom.com/settings/billing\n'
                      '\n'
                      '— Loom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Loom',
        'sender_email': 'billing@loom.com',
        'subject': 'Your Loom receipt for Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Loom Business plan was charged.\n'
                      '\n'
                      'Billing period: Mar 2026\n'
                      'Seats: 3\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Manage subscription: https://loom.com/settings/billing\n'
                      '\n'
                      '— Loom',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
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
        'is_read': False,
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
        'days_ago': 22,
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
        'days_ago': 4,
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
