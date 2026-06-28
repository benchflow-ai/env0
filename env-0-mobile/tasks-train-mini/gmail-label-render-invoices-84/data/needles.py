"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Render"
VENDOR_EMAIL = "billing@render.com"
TARGET_LABEL = "Render Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Apr 2026",
    "Jun 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Render',
        'sender_email': 'billing@render.com',
        'subject': 'Render invoice — Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Render services have been invoiced.\n'
                      '\n'
                      'Billing period: Apr 2026\n'
                      'Services: 2 web, 1 db\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://dashboard.render.com/billing\n'
                      '\n'
                      '— Render',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Render',
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
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Render',
        'sender_email': 'billing@render.com',
        'subject': 'Render invoice — Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Render services have been invoiced.\n'
                      '\n'
                      'Billing period: Mar 2026\n'
                      'Services: 2 web, 1 db\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://dashboard.render.com/billing\n'
                      '\n'
                      '— Render',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
    {   'sender_name': 'Render',
        'sender_email': 'billing@render.com',
        'subject': "Render product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Render this month. Check out the changelog '
                      "to see what's new.\n"
                      '\n'
                      '— The Render Team',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 11,
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
