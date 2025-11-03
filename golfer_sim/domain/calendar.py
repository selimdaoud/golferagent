"""Calendar and scheduling primitives."""
from __future__ import annotations

from dataclasses import dataclass, replace
from pathlib import Path
from typing import List, Optional

import json

from .tournament import Tournament
from .events import Event


@dataclass
class WeekSchedule:
    """Represents a single week in the calendar."""

    week: int
    label: str
    tournament: Optional[Tournament] = None


@dataclass
class Calendar:
    weeks: List[WeekSchedule]
    current_week: int = 0

    @property
    def current_tournament(self) -> Optional[Tournament]:
        if self.current_week >= len(self.weeks):
            return None
        return self.weeks[self.current_week].tournament

    def advance(self) -> None:
        self.current_week = min(self.current_week + 1, len(self.weeks))

    def update_training(self, state: "GameState") -> List[Event]:
        return []

    def copy(self) -> "Calendar":
        return replace(self, weeks=list(self.weeks))

    @classmethod
    def from_file(cls, path: Path) -> "Calendar":
        data = json.loads(path.read_text())
        weeks: List[WeekSchedule] = []
        for entry in data["weeks"]:
            tournament = None
            if "tournament" in entry and entry["tournament"]:
                tournament = Tournament(**entry["tournament"])
            weeks.append(
                WeekSchedule(
                    week=entry["week"],
                    label=entry["label"],
                    tournament=tournament,
                )
            )
        return cls(weeks=weeks)
