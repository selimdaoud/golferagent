# File Overview

This document summarizes the purpose of every file in the repository so future contributors can orient themselves quickly.

## Top-level

| Path | Purpose |
| --- | --- |
| `.gitignore` | Ignores Python caches, virtual environments, and distribution build artifacts. |
| `0` | Placeholder empty file retained from the original project skeleton (no functional impact). |
| `CHANGELOG.md` | Release notes documenting each tagged version of the simulator. |
| `README.md` | High-level introduction explaining how to run the simulator, its structure, and available tooling. |
| `pyproject.toml` | Packaging metadata (name, version, entry points, data files) for building distributable releases. |
| `golf_menu.py` | Backwards-compatible entry point that simply launches the curses dashboard main loop. |
| `docs/FILE_OVERVIEW.md` | This document describing the role of every repository file. |

## `golfer_sim/` package

| Path | Purpose |
| --- | --- |
| `golfer_sim/__init__.py` | Exposes `SimulationEngine`, `create_default_engine`, and the package `__version__`. |
| `golfer_sim/ai/__init__.py` | Marks the AI strategy namespace as a Python package. |
| `golfer_sim/ai/llm_adapter.py` | Dataclass stub describing the interface for hooking an external LLM (schedule, negotiation, media advice). |
| `golfer_sim/ai/memory.py` | Minimal conversation buffer that stores recent AI dialogue snippets with trimming logic. |
| `golfer_sim/ai/policies.py` | Deterministic policy that rotates training plans, recommends rest, or plays tournaments based on calendar context and fatigue. |
| `golfer_sim/ai/prompts.py` | Baseline prompt template used when an LLM adapter is plugged in. |
| `golfer_sim/core/__init__.py` | Declares the simulation core as a package. |
| `golfer_sim/core/engine.py` | Main simulation loop applying player decisions, resolving the week, and emitting events. |
| `golfer_sim/core/event_bus.py` | Lightweight synchronous publish/subscribe bus for distributing simulation events. |
| `golfer_sim/core/randoms.py` | Central random number generator wrapper that keeps the simulation deterministic when seeded. |
| `golfer_sim/core/rules.py` | Helper that loads configurable rulesets and resolves asset paths. |
| `golfer_sim/core/scheduler.py` | Coordinates weekly outcomes (tournament, training, rest), applies travel costs, and instantiates itself from a ruleset. |
| `golfer_sim/data/calendars/__init__.py` | Package marker for calendar assets. |
| `golfer_sim/data/calendars/sample_2026.json` | Example calendar defining four preseason weeks and tournaments for the MVP. |
| `golfer_sim/data/params/__init__.py` | Package marker for parameter assets. |
| `golfer_sim/data/params/base_ruleset.json` | Default ruleset configuring ranking points, travel costs, and the calendar file to load. |
| `golfer_sim/data/params/economy_baseline.json` | Starter economic parameters covering travel, coaching, and equipment costs. |
| `golfer_sim/domain/__init__.py` | Declares the domain model namespace as a package. |
| `golfer_sim/domain/agent.py` | Dataclass describing the player’s agent-coach persona and negotiation attributes. |
| `golfer_sim/domain/calendar.py` | Calendar primitives including weekly schedule definitions and file loading helpers. |
| `golfer_sim/domain/decision.py` | Decision protocol plus the `WeeklyDecision` type that stores the chosen action and payload applied to the game state. |
| `golfer_sim/domain/equipment.py` | Equipment dataclass storing bonuses and adaptation periods with a helper for computing modifiers. |
| `golfer_sim/domain/events.py` | Event primitives such as `Event` and `TournamentResult` that flow through the event bus. |
| `golfer_sim/domain/finance.py` | Finance ledger and transaction records with helpers for prize income and travel/training expenses. |
| `golfer_sim/domain/golfer.py` | Player entity capturing identity, skills, state, deep-copy helpers, and stat adjustment/improvement utilities. |
| `golfer_sim/domain/media.py` | Media engagement dataclass describing reputation and stress impacts. |
| `golfer_sim/domain/negotiation.py` | Negotiation scaffolding with offer representations and shared context metadata. |
| `golfer_sim/domain/ranking.py` | Ranking helpers that load points tables and track the player’s cumulative ranking history. |
| `golfer_sim/domain/season.py` | Season metadata container storing year and total week count. |
| `golfer_sim/domain/sponsor.py` | Sponsor contract dataclass covering fees, bonuses, obligations, and requirements. |
| `golfer_sim/domain/state.py` | Aggregate mutable game state bundling golfer, agent, calendar, ledger, ranking, journal, and weekly planning helpers. |
| `golfer_sim/domain/tournament.py` | Tournament model that simulates performance, awards ranking points, adjusts confidence/reputation, and posts ledger entries. |
| `golfer_sim/domain/training.py` | Training plan definitions with an executable library that applies gains, fatigue, and emits training events. |
| `golfer_sim/persistence/__init__.py` | Marks the persistence helpers module as a package. |
| `golfer_sim/persistence/save_load.py` | JSON serialization utilities and helpers to save/load full `GameState` snapshots with schema versioning. |
| `golfer_sim/plugins/__init__.py` | Placeholder package for future plugin registration hooks. |
| `golfer_sim/tests/__init__.py` | Marks the tests directory as a package for pytest discovery. |
| `golfer_sim/tests/test_policy.py` | Smoke test verifying the basic AI policy produces at least one weekly decision. |
| `golfer_sim/tests/test_engine.py` | Engine integration tests covering training effects, tournament flow, and persistence round-trips. |
| `golfer_sim/ui/curses_app.py` | Curses-driven MVP dashboard with interactive decision selection that visualizes the weekly loop, ranking, bankroll, and last journal entry. |
| `golfer_sim/ui/views/__init__.py` | Placeholder package for future curses sub-views. |

