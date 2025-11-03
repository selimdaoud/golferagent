# Milestone 1 Feature Overview

Milestone 1 (M1) delivers the first playable slice of the golf career
simulator. It focuses on a tight, data-driven weekly loop that can be extended
across later milestones. The features included in this drop are summarised
below.

## Simulation Core

- **Weekly engine** that advances the season, applies training, rest, or
  tournament decisions, and resolves outcomes deterministically so replays are
  reproducible with the same seed.
- **Scheduler** that enforces tournament timing, availability, and travel costs.
- **Centralised rules and randomness** helpers that read simulation knobs from
  configurable data files.

## Domain Model

- **Golfer state tracking** for skills, form, fatigue, confidence, reputation,
  and health signals.
- **Ranking ledger** that applies tier-specific point tables and records season
  progression toward tour cards.
- **Finance subsystem** using a double-entry ledger to track cash flow for
  prizes, travel, coaching, and equipment expenses.
- **Tournaments, calendar, and season** entities that contextualise the weekly
  decisions and results.
- **Training plan catalog** defining baseline drills, fatigue trade-offs, and
  skill gains so the engine can rotate recommendations.

## AI & Decision Support

- **Rule-based agent policy** that proposes weekly plans (play, rest, train)
  based on the golfer's form, fatigue, and upcoming events.
- **LLM integration stubs** (adapter, prompts, memory) prepared for the future
  AI milestones without impacting the deterministic baseline.

## User Interface

- **Curses dashboard** that displays golfer metrics, weekly suggestions, and the
  latest journal entry while letting players accept or override the agent's
  plan.
- **Legacy menu script** retained for lightweight environments, offering
  keyboard-driven navigation through the same weekly choices.

## Persistence & Data

- **Save/load helpers** that serialise the current season snapshot to JSON and
  reload it safely with version markers.
- **Configuration assets** (calendar, ranking rules, economy baselines) that
  drive simulation outcomes without hard-coded constants.

## Quality & Tooling

- **Pytest suite** exercising the policy, engine weekly flow, and persistence
  round-trips to keep the foundation stable.
- **Packaging metadata** (`pyproject.toml`, package exports) enabling editable
  installs and future PyPI releases.
