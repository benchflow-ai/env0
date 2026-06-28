"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Asana"
VENDOR_EMAIL = "billing@asana.com"
TARGET_LABEL = "Asana Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "May 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Feb 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: May 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Mar 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': "Asana product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Asana this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Asana Team',
        'labels': ['INBOX'],
        'is_read': True,
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
        'is_read': True,
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
        'is_read': True,
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
