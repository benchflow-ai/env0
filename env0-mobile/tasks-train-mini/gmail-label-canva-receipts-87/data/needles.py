"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Canva"
VENDOR_EMAIL = "receipts@canva.com"
TARGET_LABEL = "Canva Receipts"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Jan 2026",
    "Dec 2025",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'Your Canva receipt for May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Canva Pro subscription renewed.\n'
                      '\n'
                      'Billing period: May 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://canva.com/settings/billing\n'
                      '\n'
                      '— Canva',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': 'A new sign-in to your Canva account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Canva account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Canva Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Canva',
        'sender_email': 'receipts@canva.com',
        'subject': "Canva product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Canva this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Canva Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 19,
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
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
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
