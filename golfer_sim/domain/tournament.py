"""Tournament models."""
from __future__ import annotations

from dataclasses import dataclass

from .events import Event, TournamentResult
from .ranking import RankingSystem


@dataclass
class Tournament:
    name: str
    tier: str
    purse: int
    difficulty: int
    location: str

    def play(self, state: "GameState") -> TournamentResult:
        ranking = RankingSystem.for_tier(self.tier)
        points = ranking.points_for_finish("win")
        prize = int(self.purse * 0.18)
        event = Event(
            event_type="tournament_result",
            payload={
                "tournament": self.name,
                "tier": self.tier,
                "points": points,
                "prize": prize,
            },
        )
        state.ledger.record_income(prize, category="Prize", memo=f"{self.name} victory")
        state.golfer.reputation += 1
        return TournamentResult(
            position=1,
            made_cut=True,
            points_earned=points,
            prize_money=prize,
            events=[event],
        )
