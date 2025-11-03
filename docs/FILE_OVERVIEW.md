# File Overview

This document summarizes the purpose of every file in the repository so future contributors can orient themselves quickly.

## Top-level

| Path | Purpose |
| --- | --- |
| `.gitignore` | Ignores Python caches, virtual environments, and other build artifacts. |
| `0` | Placeholder empty file retained from the original project skeleton (no functional impact). |
| `README.md` | High-level introduction explaining how to run the simulator, its structure, and available tooling. |
| `golf_menu.py` | Backwards-compatible entry point that simply launches the curses dashboard main loop. |
| `docs/FILE_OVERVIEW.md` | This document describing the role of every repository file. |

## `golfer_sim/` package

| Path | Purpose |
| --- | --- |
| `golfer_sim/__init__.py` | Exposes `SimulationEngine` and `create_default_engine` for consumers importing the package. |
| `golfer_sim/ai/__init__.py` | Marks the AI strategy namespace as a Python package. |
| `golfer_sim/ai/llm_adapter.py` | Dataclass stub describing the interface for hooking an external LLM (schedule, negotiation, media advice). |
| `golfer_sim/ai/memory.py` | Minimal conversation buffer that stores recent AI dialogue snippets with trimming logic. |
| `golfer_sim/ai/policies.py` | Deterministic rule-based policy returning weekly actions for the MVP loop. |
| `golfer_sim/ai/prompts.py` | Baseline prompt template used when an LLM adapter is plugged in. |
| `golfer_sim/core/__init__.py` | Declares the simulation core as a package. |
| `golfer_sim/core/engine.py` | Main simulation loop applying player decisions, resolving the week, and emitting events. |
| `golfer_sim/core/event_bus.py` | Lightweight synchronous publish/subscribe bus for distributing simulation events. |
| `golfer_sim/core/randoms.py` | Central random number generator wrapper that keeps the simulation deterministic when seeded. |
| `golfer_sim/core/rules.py` | Helper that loads configurable rulesets and resolves asset paths. |
| `golfer_sim/core/scheduler.py` | Coordinates the season calendar, resolves weekly outcomes, and instantiates itself from a ruleset. |
| `golfer_sim/data/calendars/__init__.py` | Package marker for calendar assets. |
| `golfer_sim/data/calendars/sample_2026.json` | Example calendar defining four preseason weeks and tournaments for the MVP. |
| `golfer_sim/data/params/__init__.py` | Package marker for parameter assets. |
| `golfer_sim/data/params/base_ruleset.json` | Default ruleset configuring ranking points and the calendar file to load. |
| `golfer_sim/data/params/economy_baseline.json` | Starter economic parameters covering travel, coaching, and equipment costs. |
| `golfer_sim/domain/__init__.py` | Declares the domain model namespace as a package. |
| `golfer_sim/domain/agent.py` | Dataclass describing the player’s agent-coach persona and negotiation attributes. |
| `golfer_sim/domain/calendar.py` | Calendar primitives including weekly schedule definitions and file loading helpers. |
| `golfer_sim/domain/decision.py` | Decision protocol plus the base `WeeklyDecision` type used by AI and UI layers. |
| `golfer_sim/domain/equipment.py` | Equipment dataclass storing bonuses and adaptation periods with a helper for computing modifiers. |
| `golfer_sim/domain/events.py` | Event primitives such as `Event` and `TournamentResult` that flow through the event bus. |
| `golfer_sim/domain/finance.py` | Finance ledger and transaction records along with helpers to post prize income. |
| `golfer_sim/domain/golfer.py` | Player entity capturing identity, skills, state, and deep-copy helpers. |
| `golfer_sim/domain/media.py` | Media engagement dataclass describing reputation and stress impacts. |
| `golfer_sim/domain/negotiation.py` | Negotiation scaffolding with offer representations and shared context metadata. |
| `golfer_sim/domain/ranking.py` | Ranking system helper that reads points tables from the loaded ruleset. |
| `golfer_sim/domain/season.py` | Season metadata container storing year and total week count. |
| `golfer_sim/domain/sponsor.py` | Sponsor contract dataclass covering fees, bonuses, obligations, and requirements. |
| `golfer_sim/domain/state.py` | Aggregate mutable game state bundling golfer, agent, calendar, ledger, and journal. |
| `golfer_sim/domain/tournament.py` | Tournament model able to resolve a week, award points, and generate ledger events. |
| `golfer_sim/domain/training.py` | Training plan dataclass with helper text describing gains and fatigue. |
| `golfer_sim/persistence/__init__.py` | Marks the persistence helpers module as a package. |
| `golfer_sim/persistence/save_load.py` | JSON serialization utilities that save/load game state with schema versioning. |
| `golfer_sim/plugins/__init__.py` | Placeholder package for future plugin registration hooks. |
| `golfer_sim/tests/__init__.py` | Marks the tests directory as a package for pytest discovery. |
| `golfer_sim/tests/test_policy.py` | Smoke test verifying the basic AI policy produces at least one weekly decision. |
| `golfer_sim/ui/curses_app.py` | Curses-driven MVP dashboard that visualizes the weekly loop and advances the simulation. |
| `golfer_sim/ui/views/__init__.py` | Placeholder package for future curses sub-views. |

