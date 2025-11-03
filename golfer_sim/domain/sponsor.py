"""Sponsor contracts."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict


@dataclass
class SponsorContract:
    brand: str
    fixed_fee: int
    bonuses: Dict[str, int]
    obligations: Dict[str, int]
    min_reputation: int
    seasons_remaining: int = 1
