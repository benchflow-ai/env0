"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Render"
VENDOR_EMAIL = "billing@render.com"
TARGET_LABEL = "Render Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Dec 2025",
    "Nov 2025",
    "Apr 2026",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Render',
        'sender_email': 'billing@render.com',
        'subject': 'Render invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Render services have been invoiced.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Services: 2 web, 1 db\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://dashboard.render.com/billing\n'
                      '\n'
                      '— Render',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Render',
        'sender_email': 'billing@render.com',
        'subject': 'Render invoice — Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Render services have been invoiced.\n'
                      '\n'
                      'Billing period: Dec 2025\n'
                      'Services: 2 web, 1 db\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://dashboard.render.com/billing\n'
                      '\n'
                      '— Render',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Render',
        'sender_email': 'billing@render.com',
        'subject': 'Render invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Render services have been invoiced.\n'
                      '\n'
                      'Billing period: Nov 2025\n'
                      'Services: 2 web, 1 db\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://dashboard.render.com/billing\n'
                      '\n'
                      '— Render',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Render',
        'sender_email': 'billing@render.com',
        'subject': 'Render invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Render services have been invoiced.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Services: 2 web, 1 db\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://dashboard.render.com/billing\n'
                      '\n'
                      '— Render',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Render',
        'sender_email': 'billing@render.com',
        'subject': 'Render invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Render services have been invoiced.\n'
                      '\n'
                      'Billing period: Feb 2026\n'
                      'Services: 2 web, 1 db\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://dashboard.render.com/billing\n'
                      '\n'
                      '— Render',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Render',
        'sender_email': 'billing@render.com',
        'subject': 'Action needed: confirm your Render email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Render.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Render',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
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
        'days_ago': 4,
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
