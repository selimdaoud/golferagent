"""Smoke tests for the rule-based policy."""
from golfer_sim.ai.policies import BasicPolicy
from golfer_sim.core.engine import create_default_engine
from golfer_sim.domain.agent import AgentCoach
from golfer_sim.domain.finance import FinanceLedger
from golfer_sim.domain.golfer import Golfer
from golfer_sim.domain.ranking import PlayerRanking
from golfer_sim.domain.state import GameState


def build_state() -> GameState:
    engine = create_default_engine()
    return GameState(
        golfer=Golfer(name="Alex Martin", age=19, nationality="FR"),
        agent=AgentCoach(name="Sophie"),
        calendar=engine.scheduler.calendar,
        ledger=FinanceLedger(),
        ranking=PlayerRanking(),
    )


def test_basic_policy_returns_decision():
    state = build_state()
    policy = BasicPolicy()
    decisions = policy.propose_actions(state)
    assert decisions, "Policy should return at least one decision"
    assert decisions[0].description
