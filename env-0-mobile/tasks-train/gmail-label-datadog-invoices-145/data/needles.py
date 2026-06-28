"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Datadog"
VENDOR_EMAIL = "invoices@datadoghq.com"
TARGET_LABEL = "Datadog Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Apr 2026",
    "Feb 2026"
]

NEEDLES = [   {   'sender_name': 'Datadog',
        'sender_email': 'invoices@datadoghq.com',
        'subject': 'Datadog invoice for Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Datadog usage has been invoiced.\n'
                      '\n'
                      'Billing period: Jun 2026\n'
                      'Hosts monitored: included\n'
                      'Amount due: $12.00\n'
                      '\n'
                      'View invoice: https://app.datadoghq.com/billing\n'
                      '\n'
                      '— Datadog',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Datadog',
        'sender_email': 'invoices@datadoghq.com',
        'subject': 'Datadog invoice for Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Datadog usage has been invoiced.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Hosts monitored: included\n'
                      'Amount due: $12.00\n'
                      '\n'
                      'View invoice: https://app.datadoghq.com/billing\n'
                      '\n'
                      '— Datadog',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Datadog',
        'sender_email': 'invoices@datadoghq.com',
        'subject': 'Datadog invoice for Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Datadog usage has been invoiced.\n'
                      '\n'
                      'Billing period: Feb 2026\n'
                      'Hosts monitored: included\n'
                      'Amount due: $24.00\n'
                      '\n'
                      'View invoice: https://app.datadoghq.com/billing\n'
                      '\n'
                      '— Datadog',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Datadog',
        'sender_email': 'invoices@datadoghq.com',
        'subject': 'Action needed: confirm your Datadog email address',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Please confirm your email address to keep using Datadog.\n'
                      '\n'
                      'Confirm: https://example.com/confirm\n'
                      '\n'
                      '— Datadog',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 4,
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
