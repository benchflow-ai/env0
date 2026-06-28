"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Intercom"
VENDOR_EMAIL = "billing@intercom.com"
TARGET_LABEL = "Intercom Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jan 2026",
    "Jun 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'Intercom invoice for Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Intercom subscription has been invoiced.\n'
                      '\n'
                      'Plan: Advanced\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://app.intercom.com/billing\n'
                      '\n'
                      '— Intercom',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Intercom',
        'sender_email': 'billing@intercom.com',
        'subject': 'A new sign-in to your Intercom account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Intercom account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Intercom Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
        'days_ago': 22,
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
