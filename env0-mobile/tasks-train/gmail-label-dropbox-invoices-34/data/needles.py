"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Dropbox"
VENDOR_EMAIL = "billing@dropbox.com"
TARGET_LABEL = "Dropbox Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Apr 2026",
    "Feb 2026",
    "Dec 2025",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Storage: included\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://dropbox.com/account/billing\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — Apr 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Storage: included\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://dropbox.com/account/billing\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: Feb 2026\n'
                      'Storage: included\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://dropbox.com/account/billing\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Storage: included\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://dropbox.com/account/billing\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: Mar 2026\n'
                      'Storage: included\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://dropbox.com/account/billing\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'A new sign-in to your Dropbox account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Dropbox account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Dropbox Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Action needed: confirm your Dropbox email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Dropbox.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
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
        'days_ago': 13,
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
        'days_ago': 4,
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
