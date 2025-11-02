"""Training plan blueprints."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class TrainingPlan:
    name: str
    focus: str
    fatigue_cost: int
    expected_gain: int

    def describe(self) -> str:
        return f"{self.name}: +{self.expected_gain} {self.focus} / fatigue {self.fatigue_cost}"
