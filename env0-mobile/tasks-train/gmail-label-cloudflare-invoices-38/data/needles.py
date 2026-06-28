"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Cloudflare"
VENDOR_EMAIL = "billing@cloudflare.com"
TARGET_LABEL = "Cloudflare Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Nov 2025",
    "Jun 2026",
    "Apr 2026"
]

NEEDLES = [   {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Action needed: confirm your Cloudflare email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Cloudflare.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': "Cloudflare product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Cloudflare this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The Cloudflare Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
        'days_ago': 22,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
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
