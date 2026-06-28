"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Asana"
VENDOR_EMAIL = "billing@asana.com"
TARGET_LABEL = "Asana Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jan 2026",
    "Nov 2025",
    "Dec 2025",
    "Jun 2026",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Jan 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Nov 2025\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Dec 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Jun 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'Your Asana invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Asana subscription has been invoiced.\n'
                      '\n'
                      'Plan: Premium\n'
                      'Period: Apr 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.asana.com/admin/billing\n'
                      '\n'
                      '— Asana',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': "Asana product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Asana this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Asana Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Asana',
        'sender_email': 'billing@asana.com',
        'subject': 'A new sign-in to your Asana account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Asana account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Asana Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
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
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
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
