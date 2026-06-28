"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Vercel"
VENDOR_EMAIL = "invoices@vercel.com"
TARGET_LABEL = "Vercel Billing"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Jun 2026",
    "Mar 2026",
    "Nov 2025",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Feb 2026\n'
                      'Usage: included\n'
                      'Amount due: $24.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Jun 2026\n'
                      'Usage: included\n'
                      'Amount due: $45.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Mar 2026\n'
                      'Usage: included\n'
                      'Amount due: $12.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Nov 2025\n'
                      'Usage: included\n'
                      'Amount due: $96.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Apr 2026\n'
                      'Usage: included\n'
                      'Amount due: $24.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Action needed: confirm your Vercel email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Vercel.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': "Vercel product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Vercel this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Vercel Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 31,
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
