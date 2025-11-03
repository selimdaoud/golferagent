"""Golfer entity definition."""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Dict, List


def _clamp(value: int, lower: int = 0, upper: int = 100) -> int:
    return max(lower, min(upper, value))


@dataclass
class SkillSet:
    """Individual skill buckets for the golfer."""

    long_game: int = 50
    approach: int = 50
    short_game: int = 50
    putting: int = 50
    strategy: int = 50
    mental: int = 50

    def as_dict(self) -> Dict[str, int]:
        return {
            "long_game": self.long_game,
            "approach": self.approach,
            "short_game": self.short_game,
            "putting": self.putting,
            "strategy": self.strategy,
            "mental": self.mental,
        }

    def improve(self, focus: str, delta: int) -> int:
        current = getattr(self, focus, None)
        if current is None:
            raise ValueError(f"Unknown skill focus '{focus}'")
        setattr(self, focus, _clamp(current + delta))
        return getattr(self, focus)

    def overall_rating(self) -> float:
        values = list(self.as_dict().values())
        return sum(values) / len(values)


@dataclass
class Golfer:
    """Represents the player character and their evolving attributes."""

    name: str
    age: int
    nationality: str
    reputation: int = 10
    form: int = 60
    fatigue: int = 20
    confidence: int = 55
    health: int = 90
    skills: SkillSet = field(default_factory=SkillSet)
    inventory: List[str] = field(default_factory=list)

    def copy(self) -> "Golfer":
        return replace(
            self,
            skills=SkillSet(**self.skills.as_dict()),
            inventory=list(self.inventory),
        )

    def adjust_form(self, delta: int) -> int:
        self.form = _clamp(self.form + delta)
        return self.form

    def adjust_fatigue(self, delta: int) -> int:
        self.fatigue = _clamp(self.fatigue + delta)
        return self.fatigue

    def adjust_confidence(self, delta: int) -> int:
        self.confidence = _clamp(self.confidence + delta)
        return self.confidence

    def adjust_reputation(self, delta: int) -> int:
        self.reputation = _clamp(self.reputation + delta, lower=0, upper=200)
        return self.reputation

    def improve_skill(self, focus: str, delta: int) -> int:
        return self.skills.improve(focus, delta)

    def overall_rating(self) -> float:
        return self.skills.overall_rating()
