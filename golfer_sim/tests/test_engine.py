"""Integration-style checks for the MVP season loop."""
from __future__ import annotations

from pathlib import Path

from golfer_sim.core.engine import create_default_engine
from golfer_sim.domain.agent import AgentCoach
from golfer_sim.domain.decision import WeeklyDecision
from golfer_sim.domain.finance import FinanceLedger
from golfer_sim.domain.golfer import Golfer
from golfer_sim.domain.ranking import PlayerRanking
from golfer_sim.domain.state import GameState
from golfer_sim.persistence.save_load import load_game_state, save_game_state


def build_state():
    engine = create_default_engine()
    state = GameState(
        golfer=Golfer(name="Alex", age=19, nationality="FR"),
        agent=AgentCoach(name="Sophie"),
        calendar=engine.scheduler.calendar,
        ledger=FinanceLedger(),
        ranking=PlayerRanking(),
    )
    return engine, state


def advance(engine, state, decision: WeeklyDecision) -> None:
    engine.advance_week(state, [decision])


def test_training_plan_improves_skill_and_increases_fatigue():
    engine, state = build_state()
    baseline_skill = state.golfer.skills.short_game
    baseline_fatigue = state.golfer.fatigue

    decision = WeeklyDecision(
        action="train",
        description="Short game focus",
        payload={"plan": "short_game"},
    )

    advance(engine, state, decision)

    assert state.golfer.skills.short_game > baseline_skill
    assert state.golfer.fatigue > baseline_fatigue


def test_tournament_week_updates_ledger_and_ranking():
    engine, state = build_state()

    advance(engine, state, WeeklyDecision(action="rest", description="Rest"))

    play = WeeklyDecision(
        action="play_tournament",
        description="Play Regional Amateur Classic",
    )
    advance(engine, state, play)

    assert state.current_week == 2
    assert any("Finished Regional Amateur Classic" in entry for entry in state.journal)
    assert state.ledger.balance != 0
    assert len(state.ranking.history) >= 1


def test_save_and_load_round_trip(tmp_path: Path):
    engine, state = build_state()
    advance(
        engine,
        state,
        WeeklyDecision(action="train", description="Ball striking", payload={"plan": "ball_striking"}),
    )
    advance(engine, state, WeeklyDecision(action="rest", description="Rest"))

    save_path = tmp_path / "save.json"
    save_game_state(save_path, state)

    new_engine = create_default_engine()
    restored = load_game_state(save_path, new_engine.scheduler)

    assert restored.golfer.skills.long_game == state.golfer.skills.long_game
    assert restored.ledger.balance == state.ledger.balance
    assert restored.calendar.current_week == state.calendar.current_week
