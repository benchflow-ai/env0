"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Miro"
VENDOR_EMAIL = "invoices@miro.com"
TARGET_LABEL = "Miro Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Jan 2026",
    "May 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'Miro invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Miro subscription has been invoiced.\n'
                      '\n'
                      'Plan: Miro Business\n'
                      'Period: Nov 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Download invoice: https://miro.com/app/settings/billing\n'
                      '\n'
                      '— Miro',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'Miro invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Miro subscription has been invoiced.\n'
                      '\n'
                      'Plan: Miro Business\n'
                      'Period: Jan 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Download invoice: https://miro.com/app/settings/billing\n'
                      '\n'
                      '— Miro',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'Miro invoice — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Miro subscription has been invoiced.\n'
                      '\n'
                      'Plan: Miro Business\n'
                      'Period: May 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Download invoice: https://miro.com/app/settings/billing\n'
                      '\n'
                      '— Miro',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'Miro invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Miro subscription has been invoiced.\n'
                      '\n'
                      'Plan: Miro Business\n'
                      'Period: Dec 2025\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Download invoice: https://miro.com/app/settings/billing\n'
                      '\n'
                      '— Miro',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': "Miro product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Miro this month. Check out the changelog to '
                      "see what's new.\n"
                      '\n'
                      '— The Miro Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Miro',
        'sender_email': 'invoices@miro.com',
        'subject': 'A new sign-in to your Miro account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Miro account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Miro Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
