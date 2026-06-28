"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Cloudflare"
VENDOR_EMAIL = "billing@cloudflare.com"
TARGET_LABEL = "Cloudflare Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Dec 2025",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Nov 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'Your Cloudflare invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $12.00\n'
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
        'subject': 'Your Cloudflare invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Cloudflare plan has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Jan 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://dash.cloudflare.com/billing\n'
                      '\n'
                      '— Cloudflare',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Cloudflare',
        'sender_email': 'billing@cloudflare.com',
        'subject': 'A new sign-in to your Cloudflare account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Cloudflare account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Cloudflare Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
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
        'is_read': False,
        'days_ago': 11,
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
        'days_ago': 4,
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
        'is_read': True,
        'days_ago': 31,
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
