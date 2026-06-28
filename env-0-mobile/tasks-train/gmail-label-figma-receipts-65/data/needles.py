"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Figma"
VENDOR_EMAIL = "receipts@figma.com"
TARGET_LABEL = "Figma Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "May 2026",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'Your Figma receipt — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment. Here is your receipt.\n'
                      '\n'
                      'Plan: Figma Professional\n'
                      'Billing period: Mar 2026\n'
                      'Amount charged: $45.00\n'
                      'Payment method: Visa •••• 4242\n'
                      '\n'
                      'Manage your subscription: https://figma.com/settings/billing\n'
                      '\n'
                      '— Figma',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'Your Figma receipt — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment. Here is your receipt.\n'
                      '\n'
                      'Plan: Figma Professional\n'
                      'Billing period: May 2026\n'
                      'Amount charged: $24.00\n'
                      'Payment method: Visa •••• 4242\n'
                      '\n'
                      'Manage your subscription: https://figma.com/settings/billing\n'
                      '\n'
                      '— Figma',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'Your Figma receipt — Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Thanks for your payment. Here is your receipt.\n'
                      '\n'
                      'Plan: Figma Professional\n'
                      'Billing period: Jan 2026\n'
                      'Amount charged: $45.00\n'
                      'Payment method: Visa •••• 4242\n'
                      '\n'
                      'Manage your subscription: https://figma.com/settings/billing\n'
                      '\n'
                      '— Figma',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Figma',
        'sender_email': 'receipts@figma.com',
        'subject': 'Action needed: confirm your Figma email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Figma.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Figma',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
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
        'is_read': False,
        'days_ago': 19,
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
        'days_ago': 4,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
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
