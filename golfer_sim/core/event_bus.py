"""Simple publish/subscribe event bus used within the simulation."""
from __future__ import annotations

from collections import defaultdict
from typing import Callable, DefaultDict, Iterable, List, Protocol

from ..domain.events import Event
from ..domain.state import GameState


class EventHandler(Protocol):
    def __call__(self, event: Event, state: GameState) -> None:
        ...


class EventBus:
    """A lightweight synchronous event bus."""

    def __init__(self) -> None:
        self._subscribers: DefaultDict[str, List[EventHandler]] = defaultdict(list)

    def subscribe(self, event_type: str, handler: EventHandler) -> None:
        self._subscribers[event_type].append(handler)

    def publish(self, event: Event, state: GameState) -> None:
        for handler in self._subscribers[event.event_type]:
            handler(event, state)
        for handler in self._subscribers["*"]:
            handler(event, state)
