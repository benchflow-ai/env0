"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Retool"
VENDOR_EMAIL = "billing@retool.com"
TARGET_LABEL = "Retool Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "Mar 2026",
    "Feb 2026",
    "Jun 2026",
    "Nov 2025"
]

NEEDLES = [   {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Dec 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Dec 2025\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Mar 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Feb 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Jun 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'Your Retool invoice — Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Retool subscription has been invoiced.\n'
                      '\n'
                      'Plan: Team\n'
                      'Period: Nov 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://retool.com/settings/billing\n'
                      '\n'
                      '— Retool',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': "Retool product update: what's new this month",
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We shipped some new features in Retool this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Retool Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Retool',
        'sender_email': 'billing@retool.com',
        'subject': 'A new sign-in to your Retool account',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'We noticed a new sign-in to your Retool account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Retool Security',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 28,
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
        'days_ago': 22,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 4,
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
