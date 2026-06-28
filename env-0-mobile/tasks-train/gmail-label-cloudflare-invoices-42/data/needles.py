"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Cloudflare"
VENDOR_EMAIL = "billing@cloudflare.com"
TARGET_LABEL = "Cloudflare Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "May 2026",
    "Dec 2025",
    "Nov 2025",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: May 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': "Cloudflare product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Cloudflare this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The Cloudflare Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
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
