# Golfer Career Simulator Skeleton

This repository now hosts a modular foundation for a golf career simulation
game. The focus of this iteration is to provide:

- A **season engine skeleton** with clear module boundaries.
- A **data-driven domain model** defined with Python dataclasses.
- **Configuration files** (calendar, ranking points, economy baseline).
- A lightweight **curses dashboard** showcasing the weekly loop.

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

## Requirements

- Python 3.9+
- `pip install windows-curses` on Windows (Linux/macOS bundle `curses`).

## Running the Dashboard

```bash
python -m golfer_sim.ui.curses_app
```

Use **Enter** to advance to the next week and **q** to exit. The rule-based
agent proposes a single decision per week (play the event or rest).

## Running Tests

```bash
pytest
```

The included test is a smoke test ensuring the default policy returns a valid
decision.
