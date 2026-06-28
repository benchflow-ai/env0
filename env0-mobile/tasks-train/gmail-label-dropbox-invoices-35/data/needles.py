"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Dropbox"
VENDOR_EMAIL = "billing@dropbox.com"
TARGET_LABEL = "Dropbox Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Jun 2026",
    "May 2026",
    "Feb 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: Nov 2025\n'
                      'Storage: included\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://dropbox.com/account/billing\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Storage: included\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://dropbox.com/account/billing\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: May 2026\n'
                      'Storage: included\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://dropbox.com/account/billing\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: Feb 2026\n'
                      'Storage: included\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://dropbox.com/account/billing\n'
                      '\n'
                      '— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': 'Your Dropbox invoice — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Dropbox Business plan has been invoiced.\n'
                      '\n'
                      'Billing period: Mar 2026\n'
                      'Storage: included\n'
                      'Amount: $12.00\n'
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
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'billing@dropbox.com',
        'subject': "Dropbox product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Dropbox this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Dropbox Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
        'days_ago': 4,
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
