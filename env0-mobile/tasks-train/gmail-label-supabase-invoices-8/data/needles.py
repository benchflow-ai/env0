"""Auto-generated env-0 tasks-lite needle data (gmail label vendor).
Dependency-free; consumed by the gmail seeder and the evaluator."""

VENDOR_NAME = "Supabase"
VENDOR_EMAIL = "billing@supabase.io"
TARGET_LABEL = "Supabase Invoices"

# Stable subject markers identifying the needle (receipt/report) emails.
NEEDLE_MARKERS = [
    "Feb 2026",
    "Apr 2026",
    "Mar 2026"
]

NEEDLES = [   {   'sender_name': 'Supabase',
        'sender_email': 'billing@supabase.io',
        'subject': 'Your Supabase invoice for Feb 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Supabase project has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Feb 2026\n'
                      'Amount: $96.00\n'
                      '\n'
                      'Billing: https://supabase.com/dashboard/org/billing\n'
                      '\n'
                      '— Supabase',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 7,
        'role': 'needle',
        'params': {'marker': 'Feb 2026'}},
    {   'sender_name': 'Supabase',
        'sender_email': 'billing@supabase.io',
        'subject': 'Your Supabase invoice for Apr 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Supabase project has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Apr 2026\n'
                      'Amount: $15.00\n'
                      '\n'
                      'Billing: https://supabase.com/dashboard/org/billing\n'
                      '\n'
                      '— Supabase',
        'labels': ['INBOX'],
        'is_read': True,
        'days_ago': 16,
        'role': 'needle',
        'params': {'marker': 'Apr 2026'}},
    {   'sender_name': 'Supabase',
        'sender_email': 'billing@supabase.io',
        'subject': 'Your Supabase invoice for Mar 2026',
        'body_plain': 'Hi there,\n'
                      '\n'
                      'Your Supabase project has been invoiced.\n'
                      '\n'
                      'Plan: Pro\n'
                      'Billing period: Mar 2026\n'
                      'Amount: $18.00\n'
                      '\n'
                      'Billing: https://supabase.com/dashboard/org/billing\n'
                      '\n'
                      '— Supabase',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 25,
        'role': 'needle',
        'params': {'marker': 'Mar 2026'}},
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
    {   'sender_name': 'Dropbox',
        'sender_email': 'no-reply@dropbox.com',
        'subject': 'Your Dropbox receipt',
        'body_plain': 'Hi there,\n\nThanks for your Dropbox Plus payment of $11.99.\n\n— Dropbox',
        'labels': ['INBOX'],
        'is_read': False,
        'days_ago': 22,
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
