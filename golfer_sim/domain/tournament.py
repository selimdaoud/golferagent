"""Tournament models."""
from __future__ import annotations

from dataclasses import dataclass

from ..core.randoms import DEFAULT_RANDOM
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
        rng = DEFAULT_RANDOM
        base_rating = state.golfer.overall_rating()
        form_factor = state.golfer.form / 100
        fatigue_penalty = state.golfer.fatigue / 2
        difficulty_penalty = self.difficulty * 0.6
        variance = (rng.roll() - 0.5) * 25
        performance = base_rating * form_factor - fatigue_penalty - difficulty_penalty + variance

        finish_brackets = [
            (85, "win", 1, 0.18, 6, 6),
            (70, "top5", 4, 0.08, 4, 4),
            (55, "top10", 9, 0.04, 2, 3),
            (40, "cut", 45, 0.01, 1, 1),
        ]
        finish_label = "mc"
        position = 90
        payout_ratio = 0.0
        confidence_gain = -3
        reputation_gain = 0

        for threshold, label, pos, ratio, confidence, reputation in finish_brackets:
            if performance >= threshold:
                finish_label = label
                position = pos
                payout_ratio = ratio
                confidence_gain = confidence
                reputation_gain = reputation
                break

        ranking = RankingSystem.for_tier(self.tier)
        points = ranking.points_for_finish(finish_label)
        prize = int(self.purse * payout_ratio)

        if prize:
            state.ledger.record_income(prize, category="Prize", memo=f"{self.name} {finish_label}")

        if finish_label != "mc":
            state.golfer.adjust_confidence(confidence_gain)
            state.golfer.adjust_reputation(reputation_gain)
        else:
            state.golfer.adjust_confidence(-6)

        state.golfer.adjust_fatigue(16)
        state.golfer.adjust_form(-5)

        state.ranking.record_result(self.tier, finish_label, points)

        event = Event(
            event_type="tournament_result",
            payload={
                "tournament": self.name,
                "tier": self.tier,
                "points": points,
                "finish": finish_label,
                "prize": prize,
                "position": position,
            },
        )

        return TournamentResult(
            position=position,
            made_cut=finish_label != "mc",
            points_earned=points,
            prize_money=prize,
            events=[event],
        )
