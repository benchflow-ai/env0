"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "DigitalOcean"
VENDOR_EMAIL = "billing@digitalocean.com"
TARGET_LABEL = "DigitalOcean Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "May 2026",
    "Jan 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'DigitalOcean',
        'sender_email': 'billing@digitalocean.com',
        'subject': 'Your DigitalOcean invoice for May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your DigitalOcean usage has been invoiced.\n'
                      '\n'
                      'Billing period: May 2026\n'
                      'Droplets: 2\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://cloud.digitalocean.com/account/billing\n'
                      '\n'
                      '— DigitalOcean',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'DigitalOcean',
        'sender_email': 'billing@digitalocean.com',
        'subject': 'Your DigitalOcean invoice for Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your DigitalOcean usage has been invoiced.\n'
                      '\n'
                      'Billing period: Jan 2026\n'
                      'Droplets: 2\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://cloud.digitalocean.com/account/billing\n'
                      '\n'
                      '— DigitalOcean',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'DigitalOcean',
        'sender_email': 'billing@digitalocean.com',
        'subject': 'Your DigitalOcean invoice for Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your DigitalOcean usage has been invoiced.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Droplets: 2\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://cloud.digitalocean.com/account/billing\n'
                      '\n'
                      '— DigitalOcean',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'DigitalOcean',
        'sender_email': 'billing@digitalocean.com',
        'subject': 'Action needed: confirm your DigitalOcean email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using DigitalOcean.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— DigitalOcean',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 19,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'DigitalOcean',
        'sender_email': 'billing@digitalocean.com',
        'subject': "DigitalOcean product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in DigitalOcean this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The DigitalOcean Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
        'days_ago': 22,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
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
        'days_ago': 4,
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
