"""Training plan blueprints."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from .events import Event


@dataclass
class TrainingPlan:
    """Represents a structured training block."""

    key: str
    name: str
    focus: str
    fatigue_cost: int
    expected_gain: int

    def describe(self) -> str:
        return f"{self.name}: +{self.expected_gain} {self.focus} / fatigue {self.fatigue_cost}"

    def apply(self, golfer: "Golfer") -> Event:
        new_skill = golfer.improve_skill(self.focus, self.expected_gain)
        golfer.adjust_fatigue(self.fatigue_cost)
        golfer.adjust_form(-max(1, self.fatigue_cost // 2))
        golfer.adjust_confidence(1)
        return Event(
            event_type="training",
            payload={
                "plan": self.key,
                "focus": self.focus,
                "new_skill_level": new_skill,
            },
        )


TRAINING_LIBRARY: Dict[str, TrainingPlan] = {
    "ball_striking": TrainingPlan(
        key="ball_striking",
        name="Ball-Striking Block",
        focus="long_game",
        fatigue_cost=12,
        expected_gain=2,
    ),
    "short_game": TrainingPlan(
        key="short_game",
        name="Short-Game Intensive",
        focus="short_game",
        fatigue_cost=10,
        expected_gain=2,
    ),
    "putting_lab": TrainingPlan(
        key="putting_lab",
        name="Putting Lab",
        focus="putting",
        fatigue_cost=8,
        expected_gain=1,
    ),
}


def get_training_plan(key: str) -> TrainingPlan:
    try:
        return TRAINING_LIBRARY[key]
    except KeyError as exc:
        raise ValueError(f"Unknown training plan '{key}'") from exc


def default_training_key() -> str:
    return "ball_striking"
