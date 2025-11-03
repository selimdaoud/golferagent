"""Rule-based agent policies."""
from __future__ import annotations

from dataclasses import dataclass, field
from itertools import cycle
from typing import Iterable, List

from ..domain.decision import WeeklyDecision
from ..domain.state import GameState
from ..domain.training import TRAINING_LIBRARY, default_training_key


@dataclass
class BasicPolicy:
    """A deterministic policy used by the MVP."""

    _training_rotation: Iterable[str] = field(
        default_factory=lambda: cycle(list(TRAINING_LIBRARY.keys()))
    )

    def propose_actions(self, state: GameState) -> List[WeeklyDecision]:
        tournament = state.calendar.current_tournament
        if tournament:
            return [
                WeeklyDecision(
                    action="play_tournament",
                    description=f"Play {tournament.name} ({tournament.tier})",
                    payload={"tournament": tournament.name},
                )
            ]

        if state.golfer.fatigue >= 65:
            return [
                WeeklyDecision(
                    action="rest",
                    description="Schedule a full rest week to recover",
                )
            ]

        try:
            next_plan = next(self._training_rotation)
        except StopIteration:  # pragma: no cover - cycle never exhausts
            next_plan = default_training_key()

        return [
            WeeklyDecision(
                action="train",
                description=f"Run training plan: {TRAINING_LIBRARY[next_plan].name}",
                payload={"plan": next_plan},
            )
        ]
