"""Terminal dashboard showcasing the MVP loop."""
from __future__ import annotations

import curses
from typing import List

from ..ai.policies import BasicPolicy
from ..core.engine import SimulationEngine, create_default_engine
from ..domain.agent import AgentCoach
from ..domain.finance import FinanceLedger
from ..domain.golfer import Golfer
from ..domain.state import GameState


def build_initial_state(engine: SimulationEngine) -> GameState:
    golfer = Golfer(name="Alex Martin", age=18, nationality="FR")
    agent = AgentCoach(name="Sophie Dubois")
    return GameState(
        golfer=golfer,
        agent=agent,
        calendar=engine.scheduler.calendar,
        ledger=FinanceLedger(),
    )


def draw_dashboard(stdscr: "curses._CursesWindow", state: GameState, decisions: List[str], message: str) -> None:
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
    stdscr.addstr(7, 4, f"Form: {state.golfer.form}")
    stdscr.addstr(8, 4, f"Fatigue: {state.golfer.fatigue}")
    stdscr.addstr(9, 4, f"Confidence: {state.golfer.confidence}")
    stdscr.addstr(10, 4, f"Reputation: {state.golfer.reputation}")
    stdscr.addstr(11, 4, f"Bankroll: €{state.ledger.balance}")

    stdscr.addstr(13, 2, "Agent Suggestions", curses.A_UNDERLINE)
    for idx, desc in enumerate(decisions):
        stdscr.addstr(14 + idx, 4, f"• {desc}")

    stdscr.addstr(height - 3, 2, "Press Enter to advance week • q to quit")
    if message:
        stdscr.addstr(height - 2, 2, message[: width - 4], curses.A_DIM)

    stdscr.refresh()


def run(stdscr: "curses._CursesWindow") -> None:
    engine = create_default_engine()
    state = build_initial_state(engine)
    policy = BasicPolicy()
    message = ""

    while True:
        proposals = [d.description for d in policy.propose_actions(state)]
        draw_dashboard(stdscr, state, proposals, message)
        key = stdscr.getch()
        if key in (ord("q"), ord("Q")):
            break
        if key in (10, 13, curses.KEY_ENTER):
            decisions = policy.propose_actions(state)
            engine.advance_week(state, decisions)
            message = f"Advanced to week {state.current_week + 1}"
        else:
            message = ""


def main() -> None:
    curses.wrapper(run)


if __name__ == "__main__":
    main()
