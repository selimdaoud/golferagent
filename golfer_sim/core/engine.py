"""Core simulation loop for the golfer career simulator."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional

from ..domain.state import GameState
from ..domain.decision import WeeklyDecision
from .scheduler import Scheduler
from .event_bus import EventBus


@dataclass
class SimulationEngine:
    """Runs the weekly season loop.

    The engine is intentionally lightweight so it can be reused by different
    front-ends (CLI, curses, web) and AI integrations. Decisions are collected
    externally and passed to :meth:`advance_week`.
    """

    scheduler: Scheduler
    event_bus: EventBus

    def advance_week(self, state: GameState, decisions: Iterable[WeeklyDecision]) -> GameState:
        """Advance the simulation by a week.

        Args:
            state: Current mutable snapshot of the game.
            decisions: Decisions accepted for the upcoming week.

        Returns:
            The updated state after applying weekly effects and resolving the
            tournament/training outcomes.
        """

        self._apply_decisions(state, list(decisions))
        weekly_events = self.scheduler.resolve_week(state)
        for event in weekly_events:
            self.event_bus.publish(event, state)
        state.calendar.advance()
        return state

    def _apply_decisions(self, state: GameState, decisions: List[WeeklyDecision]) -> None:
        for decision in decisions:
            decision.apply(state)


def create_default_engine(ruleset: Optional[str] = None) -> SimulationEngine:
    """Factory helper used by the CLI/Tests to wire a default engine."""

    scheduler = Scheduler.from_ruleset(ruleset)
    event_bus = EventBus()
    return SimulationEngine(scheduler=scheduler, event_bus=event_bus)
