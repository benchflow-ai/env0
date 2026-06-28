"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Retool"
VENDOR_EMAIL = "billing@retool.com"
TARGET_LABEL = "Retool Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Feb 2026",
    "Nov 2025",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Jun 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Feb 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Nov 2025\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Jan 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': "Retool product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Retool this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Retool Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
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
        'is_read': False,
        'days_ago': 13,
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
