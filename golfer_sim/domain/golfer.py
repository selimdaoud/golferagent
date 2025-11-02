"""Golfer entity definition."""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from typing import Dict, List


@dataclass
class SkillSet:
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


@dataclass
class Golfer:
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
