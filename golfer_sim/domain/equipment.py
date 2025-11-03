"""Equipment modifiers."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Equipment:
    slot: str
    name: str
    bonus: int
    adaptation_weeks: int = 0

    def modifier(self) -> float:
        return 1.0 + self.bonus / 100.0
