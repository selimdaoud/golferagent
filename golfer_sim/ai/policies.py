"""Rule-based agent policies."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List

from ..domain.decision import WeeklyDecision
from ..domain.state import GameState


@dataclass
class BasicPolicy:
    """A deterministic policy used by the MVP."""

    def propose_actions(self, state: GameState) -> List[WeeklyDecision]:
        if state.calendar.current_tournament:
            action = WeeklyDecision(description=f"Play {state.calendar.current_tournament.name}")
        else:
            action = WeeklyDecision(description="Rest and recover")
        return [action]
