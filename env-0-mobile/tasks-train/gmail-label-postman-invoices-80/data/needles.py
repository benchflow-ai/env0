"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Postman"
VENDOR_EMAIL = "billing@postman.com"
TARGET_LABEL = "Postman Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "May 2026",
    "Mar 2026",
    "Nov 2025",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: Dec 2025\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: May 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: Mar 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
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
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: Apr 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
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
    {   'sender_name': 'Adobe',
        'sender_email': 'billing@adobe.com',
        'subject': 'Adobe Creative Cloud invoice',
        'body_plain': 'Hi there,\n'
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
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your 1Password Families plan renewed for $4.99/mo.\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 13,
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
