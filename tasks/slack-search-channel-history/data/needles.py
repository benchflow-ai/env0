"""Seed data for slack-search-channel-history task.

Scenario:
  A #product-archive channel contains an ongoing backlog of product discussions.
  The channel is active — 190 recent messages bury an older thread from ~60 days ago.
  With a page size of 20 the agent must page through ~10 pages before reaching
  the buried thread.

  The thread has 20 replies. Only reply #14 (zero-indexed) contains the answer:
  the confirmed rate-limit figure for the Enterprise tier agreed during planning.

  Task: find the Enterprise API rate limit that was agreed in #product-archive.
  Answer: 2000 requests/minute.
"""

# ---------------------------------------------------------------------------
# Filler messages — 190 recent messages that bury the needle.
# Spread across the last 30 days (days_ago 1..30, ~6-7 per day).
# Content is realistic product-discussion noise.
# ---------------------------------------------------------------------------

_SENDERS = ["priya", "marcus", "alex", "nina", "james", "sarah", "tom", "rachel"]

_FILLER_TEXTS = [
    "Quick update: the mobile onboarding redesign passed design review. Moving to eng handoff.",
    "Heads-up — the A/B test on the new pricing page ends Friday. Priya has the dashboard link.",
    "Anyone have bandwidth to review the draft spec for the batch-export feature?",
    "Retro notes from last sprint are in Notion. Action items pinned in #engineering.",
    "The customer success team flagged two enterprise accounts hitting quota limits. Tracking in Linear.",
    "FYI: staging is down for a schema migration — ETA 30 min.",
    "Reminder: product roadmap review is Thursday at 2 PM PT. Bring your Q3 asks.",
    "The user research report for the embedding playground is ready for review.",
    "Updated the milestone tracker — Fine-tuning UI is at 80% completion.",
    "New NPS results in: score is 47, up from 41 last quarter. Full breakdown shared in email.",
    "PR #902 adds the new usage dashboard. Would love a second pair of eyes before merging.",
    "Closed out the TypeScript strict-mode migration on the dashboard. Zero type errors now.",
    "The integration partner (Salesforce) confirmed the webhook format. Spec updated in Notion.",
    "Reminder to update your OKR progress in Lattice before end of month.",
    "Just shipped the dark-mode toggle to 10% of users. Monitoring for regressions.",
    "We need to decide on pagination style for the new history endpoint. Options doc in thread.",
    "The Figma prototype for the new onboarding flow is ready — link in #design.",
    "Infra alert: p99 latency on /v1/completions spiked to 420 ms this morning. Dan is investigating.",
    "Marketing wants a one-pager on our enterprise security posture. Who owns this?",
    "Reminder: SOC 2 evidence collection ends next week. Check your assigned controls.",
    "The Android app v2.1.0 passed QA — releasing to production tomorrow morning.",
    "Switching the error tracking from Sentry to Datadog APM starting next sprint.",
    "Customer request: bulk-delete endpoint for completions. Added to backlog as P2.",
    "The load test results for the new inference cluster are in. Handles 3k RPS sustained.",
    "Documentation site is getting a redesign — Nina has mockups ready.",
]


def _filler(i: int) -> dict:
    """Generate a filler message deterministically."""
    return {
        "sender": _SENDERS[i % len(_SENDERS)],
        "text": _FILLER_TEXTS[i % len(_FILLER_TEXTS)],
        # Spread across last 30 days newest-first (index 0 = most recent)
        "days_ago": max(1, i // 7) + (i % 7) * 0.14,
    }


_FILLER_MESSAGES = [_filler(i) for i in range(190)]

# ---------------------------------------------------------------------------
# The buried needle — posted ~60 days ago, well below the 190 recent messages.
# With page size=20 the agent must paginate ~10 pages to reach it.
# ---------------------------------------------------------------------------

_NEEDLE_THREAD = [
    # replies 0-5: initial discussion, no answer yet
    {
        "sender": "priya",
        "text": "Opening this thread to settle the Enterprise rate-limit question before we cut the spec.",
    },
    {
        "sender": "james",
        "text": "My vote is 1000 req/min to keep infra costs predictable.",
    },
    {
        "sender": "alex",
        "text": "1000 feels low. Our biggest prospect (Acme) said they hit 800 on a slow day.",
    },
    {
        "sender": "sarah",
        "text": "Benchmarked the new inference cluster — it can handle 4k RPS sustained without autoscaling.",
    },
    {
        "sender": "tom",
        "text": "From a data-science angle, batch jobs alone can spike to 1500. We should leave headroom.",
    },
    {
        "sender": "marcus",
        "text": "What do our closest competitors offer? Checked their docs — most are at 1000-1500.",
    },
    # replies 6-10: continued debate
    {
        "sender": "rachel",
        "text": "I'd lean toward 1500 as a compromise. Easy to enforce in the rate-limit middleware.",
    },
    {
        "sender": "nina",
        "text": "From a UX perspective, users hate hitting limits. Higher limit = fewer frustrated customers.",
    },
    {
        "sender": "priya",
        "text": "Finance flagged that we priced Enterprise with an assumed 1800 req/min cap. Going lower cuts margin.",
    },
    {
        "sender": "james",
        "text": "Good point Priya. Let's at least honour the pricing model.",
    },
    {
        "sender": "alex",
        "text": "Agreed. And 2000 gives us a clean round number that's easy to communicate.",
    },
    # replies 11-13: near-consensus
    {
        "sender": "sarah",
        "text": "2000 is well within what the cluster supports. I'm comfortable with that.",
    },
    {
        "sender": "tom",
        "text": "2000 works for me. We can always ratchet down per-account if an outlier appears.",
    },
    {
        "sender": "rachel",
        "text": "Same. 2000 it is unless James objects.",
    },
    # reply 14 — THE ANSWER
    {
        "sender": "james",
        "text": (
            "No objections. Decision locked: Enterprise tier API rate limit is confirmed at "
            "**2000 requests/minute**. Priya, please update the spec and pricing page."
        ),
    },
    # replies 15-19: follow-up noise after the decision
    {
        "sender": "priya",
        "text": "Done — spec updated and pricing page PR is open for review.",
    },
    {
        "sender": "marcus",
        "text": "Should we add a burst allowance on top? E.g. 3000 for 30-second windows?",
    },
    {
        "sender": "alex",
        "text": "Let's keep it simple for v1. We can add burst in a follow-up if customers ask.",
    },
    {
        "sender": "sarah",
        "text": "Burst support is a two-sprint effort anyway. Agreed — ship the clean version first.",
    },
    {
        "sender": "james",
        "text": "Closing thread. Rate limit: 2000 req/min. Burst: deferred to v2. Thanks everyone.",
    },
]

_NEEDLE_MESSAGE = {
    "sender": "priya",
    "text": (
        "Starting a thread to finalise the Enterprise API rate-limit before the Q2 spec freeze. "
        "Please weigh in below."
    ),
    "days_ago": 60,
    "thread": _NEEDLE_THREAD,
}

# ---------------------------------------------------------------------------
# Public exports
# ---------------------------------------------------------------------------

SEED_CHANNELS = [
    {
        "name": "product-archive",
        "is_private": False,
        "creator": "priya",
        "members": ["priya", "alex", "marcus", "sarah", "tom", "rachel", "nina", "james"],
        "purpose": "Archived product discussions and historical decisions",
        "topic": "Read-only archive of past product threads",
    },
]

SEED_MESSAGES = {
    # 190 recent filler messages first (newest), then the buried needle (oldest)
    "product-archive": _FILLER_MESSAGES + [_NEEDLE_MESSAGE],
}

FILL_CONFIG = {
    "base_scenario": "default",
}
