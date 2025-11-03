"""JSON save/load helpers."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

from ..core.scheduler import Scheduler
from ..domain.state import GameState

SCHEMA_VERSION = 1


def save_state(path: Path, payload: Dict[str, Any]) -> None:
    data = {"schema_version": SCHEMA_VERSION, **payload}
    path.write_text(json.dumps(data, indent=2, sort_keys=True))


def load_state(path: Path) -> Dict[str, Any]:
    data = json.loads(path.read_text())
    version = data.get("schema_version", 0)
    if version != SCHEMA_VERSION:
        raise ValueError(f"Unsupported save version {version}")
    return data


def save_game_state(path: Path, state: GameState) -> None:
    payload = state.to_payload()
    save_state(path, payload)


def load_game_state(path: Path, scheduler: Scheduler) -> GameState:
    payload = load_state(path)
    return GameState.from_payload(payload, scheduler.calendar)
