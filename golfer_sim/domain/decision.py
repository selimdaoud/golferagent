"""Decision layer abstractions."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from .state import GameState


class Decision(Protocol):
    def apply(self, state: GameState) -> None:
        ...


@dataclass
class WeeklyDecision:
    """Base representation of a weekly action chosen by the player."""

    description: str

    def apply(self, state: GameState) -> None:
        state.journal.append(f"Decision applied: {self.description}")
