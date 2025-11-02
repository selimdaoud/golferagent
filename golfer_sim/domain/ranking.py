"""Ranking calculation helpers."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from ..core import rules


@dataclass
class RankingSystem:
    tier: str
    points_table: Dict[str, int]

    def points_for_finish(self, finish: str) -> int:
        return self.points_table.get(finish, 0)

    @classmethod
    def for_tier(cls, tier: str) -> "RankingSystem":
        data = rules.load_ruleset(None)
        points = data["ranking_points"][tier]
        return cls(tier=tier, points_table=points)
