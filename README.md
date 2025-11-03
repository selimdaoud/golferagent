# Golfer Career Simulator Skeleton

This repository now hosts a modular foundation for a golf career simulation
game. The focus of this iteration is to provide a complete **M1 milestone**
experience:

- A deterministic **season engine** with decision application, tournament
  resolution, and travel/training handling.
- A **data-driven domain model** that tracks golfer state, ranking points,
  ledger balances, and journal entries.
- **Configuration files** (calendar, ranking points, economy baseline) that
  drive simulation behaviour.
- A lightweight **curses dashboard** showcasing the weekly loop and the latest
  agent journal entry.
- **Persistence helpers** to save and restore a season snapshot.

The codebase follows the high-level roadmap shared in the project brief and is
designed to be extended over the next development milestones.

## Project Structure

```
golfer_sim/
  core/          # simulation loop, scheduler, RNG, rules
  domain/        # entities (golfer, tournaments, finance, etc.)
  ai/            # rule-based policy, LLM stubs, memory
  ui/            # curses dashboard MVP
  data/          # JSON parameters (calendars, ranking, economy)
  persistence/   # save/load helpers
  tests/         # initial smoke tests
```

## Installation

Install the published package from PyPI (or a local build artifact) to get the
latest release:

```bash
pip install golfer-sim
```

For development work inside a clone of this repository, install in editable
mode so changes are picked up immediately:

```bash
pip install -e .
```

## Requirements

- Python 3.9+
- `pip install windows-curses` on Windows (Linux/macOS bundle `curses`).

## Running the Dashboard

```bash
python -m golfer_sim.ui.curses_app
```

or via the installed console script when using a packaged release:

```bash
golfer-sim
```

Use **↑/↓** to browse the agent's weekly suggestions, **Enter** to confirm the
highlighted decision, and **q** to exit. The rule-based agent proposes whether
to play, rest, or rotate through training plans. The dashboard displays ranking
points, bankroll, and the most recent journal note summarising last week.

## Running Tests

```bash
pytest
```

The suite covers the policy smoke test, verifies training and tournament flow
through the engine, and exercises the persistence round-trip helpers.
