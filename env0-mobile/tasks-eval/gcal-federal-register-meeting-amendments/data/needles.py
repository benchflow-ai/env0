"""Seed config for gcal-federal-register-meeting-amendments.

The exact Federal Register meeting corpus now lives in an env-owned gcal seed
pack. This task reuses the shared workspace baseline and overlays the precise
public-meeting records through that pack.
"""

GCAL_FILL_CONFIG = {
    "base_scenario": "default",
    "seed_packs": ["federal_register_meeting_amendments"],
    "include_needles": True,
}
