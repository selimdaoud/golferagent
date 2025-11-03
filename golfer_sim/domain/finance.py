"""Finance ledger primitives."""
from __future__ import annotations

from dataclasses import dataclass, field, replace
from datetime import date
from typing import List


@dataclass
class Transaction:
    timestamp: date
    account_from: str
    account_to: str
    category: str
    amount: int
    memo: str


@dataclass
class FinanceLedger:
    balance: int = 0
    transactions: List[Transaction] = field(default_factory=list)

    def record_income(self, amount: int, category: str, memo: str) -> None:
        self.balance += amount
        self.transactions.append(
            Transaction(
                timestamp=date.today(),
                account_from="PrizePool",
                account_to="Cash",
                category=category,
                amount=amount,
                memo=memo,
            )
        )

    def copy(self) -> "FinanceLedger":
        return replace(self, transactions=list(self.transactions))
