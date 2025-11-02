"""Rule loading utilities."""
from __future__ import annotations

from functools import lru_cache
from pathlib import Path
from typing import Optional

import json

BASE_RULESET = Path(__file__).resolve().parent.parent / "data" / "params" / "base_ruleset.json"


@lru_cache(maxsize=None)
def load_ruleset(name: Optional[str]) -> dict:
    """Load the requested ruleset (currently only a default implementation)."""

    path = BASE_RULESET
    if name:
        candidate = BASE_RULESET.parent / f"{name}.json"
        if candidate.exists():
            path = candidate
    data = json.loads(path.read_text())
    calendar = data.get("calendar", "calendars/sample_2026.json")
    data["calendar_file"] = str(BASE_RULESET.parent.parent / calendar)
    return data
