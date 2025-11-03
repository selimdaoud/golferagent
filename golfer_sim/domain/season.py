"""Season metadata."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Season:
    year: int
    total_weeks: int
