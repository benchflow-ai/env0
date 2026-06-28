"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "HubSpot"
VENDOR_EMAIL = "billing@hubspot.com"
TARGET_LABEL = "HubSpot Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Nov 2025",
    "Jun 2026",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'HubSpot',
        'sender_email': 'billing@hubspot.com',
        'subject': 'Your HubSpot invoice for Nov 2025',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your HubSpot subscription has been invoiced.\n'
                      '\n'
                      'Hub: Marketing Starter\n'
                      'Period: Nov 2025\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://app.hubspot.com/billing\n'
                      '\n'
                      '— HubSpot',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'HubSpot',
        'sender_email': 'billing@hubspot.com',
        'subject': 'Your HubSpot invoice for Jun 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your HubSpot subscription has been invoiced.\n'
                      '\n'
                      'Hub: Marketing Starter\n'
                      'Period: Jun 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://app.hubspot.com/billing\n'
                      '\n'
                      '— HubSpot',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'HubSpot',
        'sender_email': 'billing@hubspot.com',
        'subject': 'Your HubSpot invoice for Jan 2026',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Your HubSpot subscription has been invoiced.\n'
                      '\n'
                      'Hub: Marketing Starter\n'
                      'Period: Jan 2026\n'
                      'Amount: $45.00\n'
                      '\n'
                      'Billing: https://app.hubspot.com/billing\n'
                      '\n'
                      '— HubSpot',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'HubSpot',
        'sender_email': 'billing@hubspot.com',
        'subject': 'Action needed: confirm your HubSpot email address',
        'body_plain': 'Hi Alex,\n'
                      '\n'
                      'Please confirm your email address to keep using HubSpot.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— HubSpot',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi Alex,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 22,
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
        'days_ago': 31,
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
