import curses
from dataclasses import dataclass, field
from typing import List, Optional, Tuple


@dataclass
class MenuNode:
    """Represents a menu screen in the Golf Agent simulator."""

    title: str
    options: List[Tuple[str, Optional["MenuNode"]]] = field(default_factory=list)
    parent: Optional["MenuNode"] = None

    def add_option(self, label: str, child: Optional["MenuNode"] = None) -> None:
        if child is not None:
            child.parent = self
        self.options.append((label, child))


def build_menu() -> MenuNode:
    main_menu = MenuNode("🏁 Main Menu\n(Golf Agent Simulator)")

    player_profile = MenuNode("🧑‍💼 Player Profile")
    season_calendar = MenuNode("📅 Season Calendar")
    conversation_room = MenuNode("💬 Conversation Room")
    sponsorship_contracts = MenuNode("💰 Sponsorship & Contracts")
    training_coaching = MenuNode("🏋️ Training & Coaching")
    travel_logistics = MenuNode("✈️ Travel & Logistics")
    reports_analytics = MenuNode("🧾 Reports & Analytics")
    settings = MenuNode("⚙️ Settings / Save Game")

    main_menu.options = [
        ("🧑‍💼 Player Profile", player_profile),
        ("📅 Season Calendar", season_calendar),
        ("💬 Conversation Room", conversation_room),
        ("💰 Sponsorship & Contracts", sponsorship_contracts),
        ("🏋️ Training & Coaching", training_coaching),
        ("✈️ Travel & Logistics", travel_logistics),
        ("🧾 Reports & Analytics", reports_analytics),
        ("⚙️ Settings / Save Game", settings),
    ]

    for _, child in main_menu.options:
        if child is not None:
            child.parent = main_menu

    player_profile.options = [
        ("View Career Stats\nRanking, Wins, Earnings", None),
        ("View Personality Traits\nTemperament, Confidence, Motivation", None),
        ("Edit Personal Data\nCoach, Caddie, Equipment", None),
        ("🏁 Main Menu", main_menu),
    ]

    season_calendar.options = [
        ("Select Tournaments\nEnter or Skip Events", None),
        ("Plan Rest Weeks", None),
        ("Check Eligibility & Ranking Points", None),
        ("Discuss Schedule → Conversation Room", conversation_room),
        ("🏁 Main Menu", main_menu),
    ]

    conversation_room.options = [
        ("Talk About Performance", None),
        ("Discuss Motivation or Fatigue", None),
        ("Negotiate Tournament Choices", None),
        ("Handle Conflicts / Emotions", None),
        ("Return to Main Menu", main_menu),
        ("🏁 Main Menu", main_menu),
    ]

    sponsorship_contracts.options = [
        ("View Active Deals", None),
        ("Negotiate New Offers", None),
        ("Review Sponsor Expectations", None),
        ("Check Media Appearances", None),
        ("🏁 Main Menu", main_menu),
    ]

    training_coaching.options = [
        ("Plan Weekly Training\n(Driving, Putting, Fitness)", None),
        ("Monitor Progress", None),
        ("Hire/Replace Coach", None),
        ("Review Fatigue & Confidence Impact", None),
        ("🏁 Main Menu", main_menu),
    ]

    travel_logistics.options = [
        ("Plan Travel Routes", None),
        ("Estimate Costs", None),
        ("Rest & Recovery Planning", None),
        ("🏁 Main Menu", main_menu),
    ]

    reports_analytics.options = [
        ("View Tournament Results", None),
        ("Performance Charts", None),
        ("Season Summary\nConfidence vs. Fatigue", None),
        ("🏁 Main Menu", main_menu),
    ]

    settings.options = [
        ("Save / Load Game", None),
        ("Language / Audio / Difficulty", None),
        ("Exit", None),
        ("🏁 Main Menu", main_menu),
    ]

    return main_menu


def draw_menu(
    stdscr: "curses._CursesWindow",
    node: MenuNode,
    selected: int,
    message: Optional[str],
) -> None:
    stdscr.clear()

    try:
        curses.curs_set(0)
    except curses.error:
        pass

    height, width = stdscr.getmaxyx()

    title_lines = node.title.splitlines()
    for idx, line in enumerate(title_lines):
        stdscr.addstr(1 + idx, 2, line[: width - 4], curses.A_BOLD)

    y = 3 + len(title_lines)

    for idx, (label, _) in enumerate(node.options):
        lines = label.splitlines()
        style = curses.A_REVERSE if idx == selected else curses.A_NORMAL
        prefix = "➤ " if idx == selected else "  "

        for offset, line in enumerate(lines):
            display_prefix = prefix if offset == 0 else "  "
            stdscr.addstr(y + offset, 4, f"{display_prefix}{line}"[: width - 8], style)
        y += len(lines) + 1

    instructions = "Use ↑/↓ to navigate • Enter to select • b to go back • q to quit"
    stdscr.addstr(max(height - 3, y + 1), 2, instructions[: width - 4], curses.A_DIM)

    if message:
        stdscr.addstr(height - 2, 2, message[: width - 4], curses.A_DIM)

    stdscr.refresh()


def navigate_menu(stdscr: "curses._CursesWindow", root: MenuNode) -> None:
    current = root
    selected = 0
    message: Optional[str] = None

    while True:
        if selected >= len(current.options):
            selected = max(0, len(current.options) - 1)

        draw_menu(stdscr, current, selected, message)
        message = None

        key = stdscr.getch()

        if key in (curses.KEY_UP, ord("k")):
            selected = (selected - 1) % len(current.options)
        elif key in (curses.KEY_DOWN, ord("j")):
            selected = (selected + 1) % len(current.options)
        elif key in (curses.KEY_ENTER, 10, 13):
            label, child = current.options[selected]
            if child is not None:
                current = child
                selected = 0
            else:
                message = f"Selected: {label.replace(chr(10), ' ')}"
        elif key in (ord("b"), ord("B")):
            if current.parent is not None:
                current = current.parent
                selected = 0
            else:
                message = "Already at the top-level menu."
        elif key in (ord("q"), ord("Q")):
            break


def main(stdscr: "curses._CursesWindow") -> None:
    menu = build_menu()
    navigate_menu(stdscr, menu)


if __name__ == "__main__":
    curses.wrapper(main)
