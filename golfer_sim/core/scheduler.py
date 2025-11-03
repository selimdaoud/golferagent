"""Season scheduler and eligibility helpers."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import List, Optional

from ..domain.calendar import Calendar
from ..domain.events import Event
from ..domain.state import GameState
from ..domain.training import get_training_plan, default_training_key
from . import rules


@dataclass
class Scheduler:
    calendar: Calendar
    ruleset: dict

    def resolve_week(self, state: GameState) -> List[Event]:
        tournament = self.calendar.current_tournament
        events: List[Event] = []

        if state.planned_activity == "play_tournament" and tournament:
            events.extend(self._play_tournament(state, tournament))
        elif state.planned_activity == "train":
            events.append(self._run_training(state))
        else:
            events.append(self._handle_rest(state, tournament))

        return [event for event in events if event is not None]

    def _play_tournament(self, state: GameState, tournament) -> List[Event]:
        travel_cost = self.ruleset.get("travel_cost", 450)
        state.ledger.record_expense(travel_cost, category="Travel", memo=f"Travel to {tournament.name}")
        result = tournament.play(state)
        state.journal.append(
            f"Finished {tournament.name} in position {result.position} (points +{result.points_earned})"
        )
        return result.events

    def _run_training(self, state: GameState) -> Event:
        key = state.plan_payload.get("plan") or default_training_key()
        plan = get_training_plan(key)
        event = plan.apply(state.golfer)
        state.journal.append(f"Completed training plan {plan.name}")
        return event

    def _handle_rest(self, state: GameState, tournament) -> Event:
        state.golfer.adjust_fatigue(-18 if tournament is None else -12)
        state.golfer.adjust_form(4)
        state.golfer.adjust_confidence(1)
        memo = "Strategic rest week" if tournament is None else "Skipped event for recovery"
        state.journal.append(memo)
        return Event(event_type="rest", payload={"tournament_available": tournament is not None})

    @classmethod
    def from_ruleset(cls, ruleset_name: Optional[str]) -> "Scheduler":
        config = rules.load_ruleset(ruleset_name)
        calendar = Calendar.from_file(Path(config["calendar_file"]))
        return cls(calendar=calendar, ruleset=config)
