"""Aggregate mutable game state."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List

from .agent import AgentCoach
from .calendar import Calendar
from .finance import FinanceLedger
from .golfer import Golfer
from .ranking import PlayerRanking


@dataclass
class GameState:
    golfer: Golfer
    agent: AgentCoach
    calendar: Calendar
    ledger: FinanceLedger
    ranking: PlayerRanking
    journal: List[str] = field(default_factory=list)
    planned_activity: str = "rest"
    plan_payload: Dict[str, Any] = field(default_factory=dict)

    @property
    def current_week(self) -> int:
        return self.calendar.current_week

    def snapshot(self) -> "GameState":
        return GameState(
            golfer=self.golfer.copy(),
            agent=self.agent.copy(),
            calendar=self.calendar.copy(),
            ledger=self.ledger.copy(),
            ranking=self.ranking.copy(),
            journal=list(self.journal),
            planned_activity=self.planned_activity,
            plan_payload=dict(self.plan_payload),
        )

    def clear_plan(self) -> None:
        self.planned_activity = "rest"
        self.plan_payload.clear()

    def to_payload(self) -> Dict[str, Any]:
        return {
            "golfer": {
                "name": self.golfer.name,
                "age": self.golfer.age,
                "nationality": self.golfer.nationality,
                "reputation": self.golfer.reputation,
                "form": self.golfer.form,
                "fatigue": self.golfer.fatigue,
                "confidence": self.golfer.confidence,
                "health": self.golfer.health,
                "skills": self.golfer.skills.as_dict(),
                "inventory": list(self.golfer.inventory),
            },
            "agent": dict(self.agent.__dict__),
            "calendar": {
                "current_week": self.calendar.current_week,
            },
            "ledger": {
                "balance": self.ledger.balance,
            },
            "ranking": {
                "points": self.ranking.points,
                "history": list(self.ranking.history),
            },
            "journal": list(self.journal),
            "planned_activity": self.planned_activity,
            "plan_payload": dict(self.plan_payload),
        }

    @classmethod
    def from_payload(cls, payload: Dict[str, Any], calendar: Calendar) -> "GameState":
        golfer_data = payload["golfer"]
        golfer = Golfer(
            name=golfer_data["name"],
            age=golfer_data["age"],
            nationality=golfer_data["nationality"],
            reputation=golfer_data["reputation"],
            form=golfer_data["form"],
            fatigue=golfer_data["fatigue"],
            confidence=golfer_data["confidence"],
            health=golfer_data.get("health", 90),
        )
        for skill, value in golfer_data["skills"].items():
            golfer.improve_skill(skill, value - getattr(golfer.skills, skill))
        golfer.inventory = list(golfer_data.get("inventory", []))

        agent = AgentCoach(**payload["agent"])
        ledger = FinanceLedger(balance=payload["ledger"]["balance"])
        ranking = PlayerRanking(
            points=payload["ranking"]["points"],
            history=list(payload["ranking"].get("history", [])),
        )
        calendar.current_week = payload["calendar"]["current_week"]

        return cls(
            golfer=golfer,
            agent=agent,
            calendar=calendar,
            ledger=ledger,
            ranking=ranking,
            journal=list(payload.get("journal", [])),
            planned_activity=payload.get("planned_activity", "rest"),
            plan_payload=dict(payload.get("plan_payload", {})),
        )
