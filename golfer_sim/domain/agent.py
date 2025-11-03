"""Agent-coach metadata."""
from __future__ import annotations

from dataclasses import dataclass, replace


@dataclass
class AgentCoach:
    name: str
    personality: str = "balanced"
    negotiation_style: str = "standard"
    risk_tolerance: int = 50

    def copy(self) -> "AgentCoach":
        return replace(self)
