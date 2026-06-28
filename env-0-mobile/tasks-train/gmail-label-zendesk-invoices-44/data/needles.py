"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Zendesk"
VENDOR_EMAIL = "invoices@zendesk.com"
TARGET_LABEL = "Zendesk Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Mar 2026",
    "Jun 2026",
    "Jan 2026",
    "Feb 2026",
    "May 2026"
]

NEEDLES = [   {   'sender_name': 'Zendesk',
        'sender_email': 'invoices@zendesk.com',
        'subject': 'Your Zendesk invoice — Mar 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Zendesk subscription has been invoiced.\n'
                      '\n'
                      'Plan: Suite Team\n'
                      'Period: Mar 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://www.zendesk.com/account/billing\n'
                      '\n'
                      '— Zendesk',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Zendesk',
        'sender_email': 'invoices@zendesk.com',
        'subject': 'Your Zendesk invoice — Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Zendesk subscription has been invoiced.\n'
                      '\n'
                      'Plan: Suite Team\n'
                      'Period: Jun 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://www.zendesk.com/account/billing\n'
                      '\n'
                      '— Zendesk',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Zendesk',
        'sender_email': 'invoices@zendesk.com',
        'subject': 'Your Zendesk invoice — Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Zendesk subscription has been invoiced.\n'
                      '\n'
                      'Plan: Suite Team\n'
                      'Period: Jan 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://www.zendesk.com/account/billing\n'
                      '\n'
                      '— Zendesk',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'Zendesk',
        'sender_email': 'invoices@zendesk.com',
        'subject': 'Your Zendesk invoice — Feb 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Zendesk subscription has been invoiced.\n'
                      '\n'
                      'Plan: Suite Team\n'
                      'Period: Feb 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://www.zendesk.com/account/billing\n'
                      '\n'
                      '— Zendesk',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Zendesk',
        'sender_email': 'invoices@zendesk.com',
        'subject': 'Your Zendesk invoice — May 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your Zendesk subscription has been invoiced.\n'
                      '\n'
                      'Plan: Suite Team\n'
                      'Period: May 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://www.zendesk.com/account/billing\n'
                      '\n'
                      '— Zendesk',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Zendesk',
        'sender_email': 'invoices@zendesk.com',
        'subject': 'Action needed: confirm your Zendesk email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using Zendesk.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Zendesk',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
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
        'is_read': False,
        'days_ago': 31,
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
