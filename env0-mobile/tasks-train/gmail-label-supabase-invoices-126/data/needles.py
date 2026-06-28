"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Supabase"
VENDOR_EMAIL = "billing@supabase.io"
TARGET_LABEL = "Supabase Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Jun 2026",
    "Feb 2026",
    "Dec 2025"
]

NEEDLES = [   {   'sender_name': 'Supabase',
        'sender_email': 'billing@supabase.io',
        'subject': 'Your Supabase invoice for Jun 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Supabase project has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Jun 2026\n'
                      'Amount: $12.00\n'
                      '\n'
                      'Billing: https://supabase.com/dashboard/org/billing\n'
                      '\n'
                      '— Supabase',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Jun 2026'}},
    {   'sender_name': 'Supabase',
        'sender_email': 'billing@supabase.io',
        'subject': 'Your Supabase invoice for Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Supabase project has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://supabase.com/dashboard/org/billing\n'
                      '\n'
                      '— Supabase',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Supabase',
        'sender_email': 'billing@supabase.io',
        'subject': 'Your Supabase invoice for Dec 2025',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Supabase project has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Dec 2025\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://supabase.com/dashboard/org/billing\n'
                      '\n'
                      '— Supabase',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Dec 2025'}},
    {   'sender_name': 'Supabase',
        'sender_email': 'billing@supabase.io',
        'subject': 'A new sign-in to your Supabase account',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We noticed a new sign-in to your Supabase account from a new device. If '
                      'this was you, you can ignore this email.\n'
                      '\n'
                      '— Supabase Security',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 28,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Supabase',
        'sender_email': 'billing@supabase.io',
        'subject': "Supabase product update: what's new this month",
        'body_plain': 'Hi there,\n'
                      '\n'
                      'We shipped some new features in Supabase this month. Check out the '
                      "changelog to see what's new.\n"
                      '\n'
                      '— The Supabase Team',
        'labels': ['INBOX'],
        'is_read': False,
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
        'days_ago': 22,
        'role': 'decoy',
        'params': {}},
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
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
