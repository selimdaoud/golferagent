"""Media appearances and reputation tracking."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class MediaEngagement:
    name: str
    reputation_delta: int
    stress_delta: int
    description: str
