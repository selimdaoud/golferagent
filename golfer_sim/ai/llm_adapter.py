"""LLM integration point (stub)."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Dict

from ..domain.state import GameState


@dataclass
class LLMAdapter:
    """Interface used to communicate with external LLM services."""

    model_name: str = "gpt-4o"

    def suggest_schedule(self, state: GameState) -> str:
        return "LLM schedule suggestions are not available in the stub."

    def negotiate(self, context: Dict[str, str]) -> str:
        return "Negotiation stub response."

    def media_coach(self, context: Dict[str, str]) -> str:
        return "Media coaching stub response."
