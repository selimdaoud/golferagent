"""Aggregate mutable game state."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List

from .golfer import Golfer
from .agent import AgentCoach
from .calendar import Calendar
from .finance import FinanceLedger


@dataclass
class GameState:
    golfer: Golfer
    agent: AgentCoach
    calendar: Calendar
    ledger: FinanceLedger
    journal: List[str] = field(default_factory=list)

    @property
    def current_week(self) -> int:
        return self.calendar.current_week

    def snapshot(self) -> "GameState":
        return GameState(
            golfer=self.golfer.copy(),
            agent=self.agent.copy(),
            calendar=self.calendar.copy(),
            ledger=self.ledger.copy(),
            journal=list(self.journal),
        )
