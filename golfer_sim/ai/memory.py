"""Short-term conversational memory."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class MemoryBuffer:
    entries: List[str] = field(default_factory=list)
    max_entries: int = 12

    def add(self, message: str) -> None:
        self.entries.append(message)
        if len(self.entries) > self.max_entries:
            self.entries.pop(0)

    def summary(self) -> str:
        return "\n".join(self.entries)
