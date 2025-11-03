"""Ranking calculation helpers."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List

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


@dataclass
class PlayerRanking:
    """Tracks the player ranking points across tiers."""

    points: int = 0
    history: List[Dict[str, object]] = field(default_factory=list)

    def record_result(self, tier: str, finish: str, points: int) -> None:
        self.points += points
        self.history.append({"points": points, "tier": tier, "finish": finish})

    def copy(self) -> "PlayerRanking":
        return PlayerRanking(points=self.points, history=list(self.history))
