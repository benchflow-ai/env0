"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Vercel"
VENDOR_EMAIL = "invoices@vercel.com"
TARGET_LABEL = "Vercel Billing"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "Apr 2026",
    "May 2026",
    "Dec 2025",
    "Jun 2026"
]

NEEDLES = [   {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Mar 2026\n'
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
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Apr 2026\n'
                      'Usage: included\n'
                      'Amount due: $15.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: May 2026\n'
                      'Usage: included\n'
                      'Amount due: $45.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Dec 2025\n'
                      'Usage: included\n'
                      'Amount due: $12.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Jun 2026\n'
                      'Usage: included\n'
                      'Amount due: $15.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
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
        'is_read': True,
        'days_ago': 31,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 22,
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
        'is_read': True,
        'days_ago': 31,
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
