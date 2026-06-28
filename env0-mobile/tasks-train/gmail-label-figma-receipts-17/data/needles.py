"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Figma"
VENDOR_EMAIL = "receipts@figma.com"
TARGET_LABEL = "Figma Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jan 2026",
    "Jun 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'Your Figma receipt — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your payment. Here is your receipt.\n'
                      '\n'
                      'Plan: Figma Professional\n'
                      'Billing period: Jan 2026\n'
                      'Amount charged: $18.00\n'
                      'Payment method: Visa •••• 4242\n'
                      '\n'
                      'Manage your subscription: https://figma.com/settings/billing\n'
                      '\n'
                      '— Figma',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'Your Figma receipt — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your payment. Here is your receipt.\n'
                      '\n'
                      'Plan: Figma Professional\n'
                      'Billing period: Jun 2026\n'
                      'Amount charged: $15.00\n'
                      'Payment method: Visa •••• 4242\n'
                      '\n'
                      'Manage your subscription: https://figma.com/settings/billing\n'
                      '\n'
                      '— Figma',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'Your Figma receipt — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Thanks for your payment. Here is your receipt.\n'
                      '\n'
                      'Plan: Figma Professional\n'
                      'Billing period: Dec 2025\n'
                      'Amount charged: $15.00\n'
                      'Payment method: Visa •••• 4242\n'
                      '\n'
                      'Manage your subscription: https://figma.com/settings/billing\n'
                      '\n'
                      '— Figma',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': "Figma product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Figma this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Figma Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
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
        'is_read': False,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 4,
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
