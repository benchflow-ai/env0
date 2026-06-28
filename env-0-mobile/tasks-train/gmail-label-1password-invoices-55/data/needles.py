"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "1Password"
VENDOR_EMAIL = "billing@1password.com"
TARGET_LABEL = "1Password Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Apr 2026",
    "Jan 2026",
    "Nov 2025",
    "Dec 2025",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': '1Password',
        'sender_email': 'billing@1password.com',
        'subject': 'Your 1Password invoice for Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your 1Password Business subscription has been invoiced.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Members: 5\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://my.1password.com/billing\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': '1Password',
        'sender_email': 'billing@1password.com',
        'subject': 'Your 1Password invoice for Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your 1Password Business subscription has been invoiced.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
                      'Members: 5\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://my.1password.com/billing\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': '1Password',
        'sender_email': 'billing@1password.com',
        'subject': 'Your 1Password invoice for Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your 1Password Business subscription has been invoiced.\n'
                      '\n'
                      'Billing period: Nov 2025\n'
                      'Members: 5\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://my.1password.com/billing\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': '1Password',
        'sender_email': 'billing@1password.com',
        'subject': 'Your 1Password invoice for Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your 1Password Business subscription has been invoiced.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Members: 5\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://my.1password.com/billing\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': '1Password',
        'sender_email': 'billing@1password.com',
        'subject': 'Your 1Password invoice for Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your 1Password Business subscription has been invoiced.\n'
                      '\n'
                      'Billing period: Mar 2026\n'
                      'Members: 5\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://my.1password.com/billing\n'
                      '\n'
                      '— 1Password',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': '1Password',
        'sender_email': 'billing@1password.com',
        'subject': "1Password product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in 1Password this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The 1Password Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
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
