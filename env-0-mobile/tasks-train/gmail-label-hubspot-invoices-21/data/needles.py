"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "HubSpot"
VENDOR_EMAIL = "billing@hubspot.com"
TARGET_LABEL = "HubSpot Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Dec 2025",
    "Jun 2026",
    "May 2026",
    "Mar 2026",
    "Jan 2026"
]

NEEDLES = [   {   'sender_name': 'HubSpot',
        'sender_email': 'billing@hubspot.com',
        'subject': 'Your HubSpot invoice for Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your HubSpot subscription has been invoiced.\n'
                      '\n'
                      'Hub: Marketing Starter\n'
                      'Period: Dec 2025\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://app.hubspot.com/billing\n'
                      '\n'
                      '— HubSpot',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'HubSpot',
        'sender_email': 'billing@hubspot.com',
        'subject': 'Your HubSpot invoice for Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your HubSpot subscription has been invoiced.\n'
                      '\n'
                      'Hub: Marketing Starter\n'
                      'Period: Jun 2026\n'
                      'Amount: $18.00\n'
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
        'subject': 'Your HubSpot invoice for May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your HubSpot subscription has been invoiced.\n'
                      '\n'
                      'Hub: Marketing Starter\n'
                      'Period: May 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://app.hubspot.com/billing\n'
                      '\n'
                      '— HubSpot',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'HubSpot',
        'sender_email': 'billing@hubspot.com',
        'subject': 'Your HubSpot invoice for Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your HubSpot subscription has been invoiced.\n'
                      '\n'
                      'Hub: Marketing Starter\n'
                      'Period: Mar 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://app.hubspot.com/billing\n'
                      '\n'
                      '— HubSpot',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 34,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'HubSpot',
        'sender_email': 'billing@hubspot.com',
        'subject': 'Your HubSpot invoice for Jan 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your HubSpot subscription has been invoiced.\n'
                      '\n'
                      'Hub: Marketing Starter\n'
                      'Period: Jan 2026\n'
                      'Amount: $24.00\n'
                      '\n'
                      'Billing: https://app.hubspot.com/billing\n'
                      '\n'
                      '— HubSpot',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 43,
        'role': 'needle',
        'params': {'marker': 'Jan 2026'}},
    {   'sender_name': 'HubSpot',
        'sender_email': 'billing@hubspot.com',
        'subject': 'A new sign-in to your HubSpot account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your HubSpot account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— HubSpot Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
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
