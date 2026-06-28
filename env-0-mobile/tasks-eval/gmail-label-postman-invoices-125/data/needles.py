"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Postman"
VENDOR_EMAIL = "billing@postman.com"
TARGET_LABEL = "Postman Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Apr 2026",
    "Dec 2025",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: Jun 2026\n'
                      'Amount: $12.00\n'
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
        'subject': 'Postman invoice for Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: Apr 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: Dec 2025\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'Postman invoice for May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Postman team subscription has been invoiced.\n'
                      '\n'
                      'Plan: Basic\n'
                      'Period: May 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://go.postman.co/billing\n'
                      '\n'
                      '— Postman',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': "Postman product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Postman this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Postman Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Postman',
        'sender_email': 'billing@postman.com',
        'subject': 'A new sign-in to your Postman account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Postman account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Postman Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
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
        'is_read': True,
        'days_ago': 13,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
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
