"""Terminal dashboard showcasing the MVP loop."""
from __future__ import annotations

import curses
from typing import List

from ..ai.policies import BasicPolicy
from ..core.engine import SimulationEngine, create_default_engine
from ..domain.agent import AgentCoach
from ..domain.finance import FinanceLedger
from ..domain.golfer import Golfer
from ..domain.ranking import PlayerRanking
from ..domain.state import GameState
from ..domain.decision import WeeklyDecision


def build_initial_state(engine: SimulationEngine) -> GameState:
    golfer = Golfer(name="Alex Martin", age=18, nationality="FR")
    agent = AgentCoach(name="Sophie Dubois")
    return GameState(
        golfer=golfer,
        agent=agent,
        calendar=engine.scheduler.calendar,
        ledger=FinanceLedger(),
        ranking=PlayerRanking(),
    )


def draw_dashboard(
    stdscr: "curses._CursesWindow",
    state: GameState,
    decisions: List[WeeklyDecision],
    selected_index: int,
    message: str,
) -> None:
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    stdscr.addstr(1, 2, "Golf Career Dashboard", curses.A_BOLD)
    stdscr.addstr(3, 2, f"Week: {state.current_week + 1}")
    upcoming = state.calendar.current_tournament
    if upcoming:
        stdscr.addstr(4, 2, f"Upcoming: {upcoming.name} ({upcoming.tier})")
    else:
        stdscr.addstr(4, 2, "Upcoming: Training / Rest")

    stdscr.addstr(6, 2, "Player Stats", curses.A_UNDERLINE)
    stdscr.addstr(7, 4, f"Ranking points: {state.ranking.points}")
    stdscr.addstr(8, 4, f"Form: {state.golfer.form}")
    stdscr.addstr(9, 4, f"Fatigue: {state.golfer.fatigue}")
    stdscr.addstr(10, 4, f"Confidence: {state.golfer.confidence}")
    stdscr.addstr(11, 4, f"Reputation: {state.golfer.reputation}")
    stdscr.addstr(12, 4, f"Bankroll: €{state.ledger.balance}")

    last_note = state.journal[-1] if state.journal else ""

    stdscr.addstr(14, 2, "Agent Suggestions", curses.A_UNDERLINE)
    if decisions:
        for idx, decision in enumerate(decisions):
            attr = curses.A_REVERSE if idx == selected_index else curses.A_NORMAL
            stdscr.addstr(15 + idx, 4, f"• {decision.description[: width - 6]}", attr)
    else:
        stdscr.addstr(15, 4, "No available actions", curses.A_DIM)

    last_line = 15 + max(len(decisions), 1)
    if last_note:
        stdscr.addstr(last_line, 2, f"Last week: {last_note[: width - 4]}")

    stdscr.addstr(height - 4, 2, "Use ↑/↓ to choose • Enter to confirm • q to quit")
    if message:
        stdscr.addstr(height - 2, 2, message[: width - 4], curses.A_DIM)

    stdscr.refresh()


def run(stdscr: "curses._CursesWindow") -> None:
    engine = create_default_engine()
    state = build_initial_state(engine)
    policy = BasicPolicy()
    message = ""
    decisions = policy.propose_actions(state)
    selected_index = 0

    while True:
        draw_dashboard(stdscr, state, decisions, selected_index, message)
        key = stdscr.getch()
        if key in (ord("q"), ord("Q")):
            break
        if key in (curses.KEY_UP, ord("k")):
            selected_index = max(0, selected_index - 1)
            message = ""
            continue
        if key in (curses.KEY_DOWN, ord("j")):
            if decisions:
                selected_index = min(len(decisions) - 1, selected_index + 1)
            message = ""
            continue
        if key in (10, 13, curses.KEY_ENTER):
            if not decisions:
                message = "No actions available this week"
                continue
            chosen = decisions[selected_index]
            engine.advance_week(state, [chosen])
            decisions = policy.propose_actions(state)
            selected_index = 0
            message = f"Applied: {chosen.description}"
        else:
            message = ""


def main() -> None:
    curses.wrapper(run)


if __name__ == "__main__":
    main()
