"""Season scheduler and eligibility helpers."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from ..domain.calendar import Calendar
from ..domain.state import GameState
from ..domain.events import Event
from . import rules


@dataclass
class Scheduler:
    calendar: Calendar
    ruleset: dict

    def resolve_week(self, state: GameState) -> List[Event]:
        tournament = self.calendar.current_tournament
        events: List[Event] = []
        if tournament:
            result = tournament.play(state)
            events.extend(result.events)
        events.extend(self.calendar.update_training(state))
        return events

    @classmethod
    def from_ruleset(cls, ruleset_name: Optional[str]) -> "Scheduler":
        config = rules.load_ruleset(ruleset_name)
        calendar = Calendar.from_file(Path(config["calendar_file"]))
        return cls(calendar=calendar, ruleset=config)
