"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Figma"
VENDOR_EMAIL = "receipts@figma.com"
TARGET_LABEL = "Figma Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Jun 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'Your Figma receipt — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment. Here is your receipt.\n'
                      '\n'
                      'Plan: Figma Professional\n'
                      'Billing period: Nov 2025\n'
                      'Amount charged: $15.00\n'
                      'Payment method: Visa •••• 4242\n'
                      '\n'
                      'Manage your subscription: https://figma.com/settings/billing\n'
                      '\n'
                      '— Figma',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'Your Figma receipt — Jun 2026',
        'body_plain': 'Hi Alex,\n'
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
        'subject': 'Your Figma receipt — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment. Here is your receipt.\n'
                      '\n'
                      'Plan: Figma Professional\n'
                      'Billing period: Mar 2026\n'
                      'Amount charged: $96.00\n'
                      'Payment method: Visa •••• 4242\n'
                      '\n'
                      'Manage your subscription: https://figma.com/settings/billing\n'
                      '\n'
                      '— Figma',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'A new sign-in to your Figma account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Figma account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Figma Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
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
        'days_ago': 22,
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
