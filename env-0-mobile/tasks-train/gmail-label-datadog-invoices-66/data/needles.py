"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Datadog"
VENDOR_EMAIL = "invoices@datadoghq.com"
TARGET_LABEL = "Datadog Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "May 2026",
    "Nov 2025"
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
                      'Amount due: $15.00\n'
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
        'subject': 'Datadog invoice for May 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Datadog usage has been invoiced.\n'
                      '\n'
                      'Billing period: May 2026\n'
                      'Hosts monitored: included\n'
                      'Amount due: $18.00\n'
                      '\n'
                      'View invoice: https://app.datadoghq.com/billing\n'
                      '\n'
                      '— Datadog',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'May 2026'}},
    {   'sender_name': 'Datadog',
        'sender_email': 'invoices@datadoghq.com',
        'subject': 'Datadog invoice for Nov 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Datadog usage has been invoiced.\n'
                      '\n'
                      'Billing period: Nov 2025\n'
                      'Hosts monitored: included\n'
                      'Amount due: $96.00\n'
                      '\n'
                      'View invoice: https://app.datadoghq.com/billing\n'
                      '\n'
                      '— Datadog',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Nov 2025'}},
    {   'sender_name': 'Datadog',
        'sender_email': 'invoices@datadoghq.com',
        'subject': 'A new sign-in to your Datadog account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Datadog account from a new device. If this '
                      'was you, you can ignore this email.\n'
                      '\n'
                      '— Datadog Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Datadog',
        'sender_email': 'invoices@datadoghq.com',
        'subject': "Datadog product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Datadog this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Datadog Team',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 3,
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
        'is_read': False,
        'days_ago': 31,
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
        'is_read': False,
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
