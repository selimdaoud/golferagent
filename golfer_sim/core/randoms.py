"""Centralised random number helpers."""
from __future__ import annotations

import random
from dataclasses import dataclass
from typing import Optional


@dataclass
class RandomSource:
    seed: Optional[int] = None

    def __post_init__(self) -> None:
        self._rng = random.Random(self.seed)

    def roll(self) -> float:
        return self._rng.random()

    def choice(self, population):
        return self._rng.choice(population)


DEFAULT_RANDOM = RandomSource(seed=42)
