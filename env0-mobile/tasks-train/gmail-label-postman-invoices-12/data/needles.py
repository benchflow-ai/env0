"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Postman"
VENDOR_EMAIL = "billing@postman.com"
TARGET_LABEL = "Postman Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Jan 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: Jun 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: Jan 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: Nov 2025\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Action needed: confirm your Postman email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Postman.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'A new sign-in to your Postman account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Postman account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Postman Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
        'days_ago': 4,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 22,
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
