"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Airtable"
VENDOR_EMAIL = "billing@airtable.com"
TARGET_LABEL = "Airtable Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Jun 2026",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'Your Airtable invoice for Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Airtable workspace has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://airtable.com/account/billing\n'
                      '\n'
                      '— Airtable',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'Your Airtable invoice for Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Airtable workspace has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://airtable.com/account/billing\n'
                      '\n'
                      '— Airtable',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'Your Airtable invoice for May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Airtable workspace has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Billing period: May 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://airtable.com/account/billing\n'
                      '\n'
                      '— Airtable',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Airtable',
        'sender_email': 'billing@airtable.com',
        'subject': 'A new sign-in to your Airtable account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Airtable account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Airtable Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
        'days_ago': 4,
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
        'days_ago': 13,
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
