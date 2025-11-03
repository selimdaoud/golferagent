"""Event primitives shared across modules."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Event:
    """Represents something noteworthy that happened during the week."""

    event_type: str
    payload: Dict[str, Any]


@dataclass
class TournamentResult:
    """Outcome of a played tournament."""

    position: int
    made_cut: bool
    points_earned: int
    prize_money: int
    events: list[Event]
