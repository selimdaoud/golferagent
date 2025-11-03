"""Decision layer abstractions."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Protocol

from .state import GameState


class Decision(Protocol):
    def apply(self, state: GameState) -> None:
        ...


@dataclass
class WeeklyDecision:
    """Base representation of a weekly action chosen by the player."""

    action: str
    description: str
    payload: Dict[str, object] = field(default_factory=dict)

    def apply(self, state: GameState) -> None:
        state.planned_activity = self.action
        state.plan_payload = dict(self.payload)
        state.journal.append(f"Decision applied: {self.description}")
