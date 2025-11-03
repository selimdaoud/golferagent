"""Negotiation scaffolding."""
from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Offer:
    value: int
    reputation_impact: int
    notes: str


@dataclass
class NegotiationContext:
    counterpart: str
    offers: List[Offer]
    status: str = "pending"
