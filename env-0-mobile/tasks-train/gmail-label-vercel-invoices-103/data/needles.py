"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Vercel"
VENDOR_EMAIL = "invoices@vercel.com"
TARGET_LABEL = "Vercel Billing"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "May 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Jun 2026\n'
                      'Usage: included\n'
                      'Amount due: $96.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — May 2026',
        'body_plain': 'Hi Alex,\n'
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
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'Vercel invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Vercel Pro plan has been invoiced.\n'
                      '\n'
                      'Billing cycle: Dec 2025\n'
                      'Usage: included\n'
                      'Amount due: $24.00\n'
                      '\n'
                      'View invoice: https://vercel.com/account/invoices\n'
                      '\n'
                      '— Vercel',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': "Vercel product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Vercel this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Vercel Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Vercel',
        'sender_email': 'invoices@vercel.com',
        'subject': 'A new sign-in to your Vercel account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Vercel account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Vercel Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 19,
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
        'days_ago': 13,
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
