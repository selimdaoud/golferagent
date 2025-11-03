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
        self._append(amount, "PrizePool", "Cash", category, memo)

    def record_expense(self, amount: int, category: str, memo: str) -> None:
        self._append(amount, "Cash", f"Expense:{category}", category, memo, negate=True)

    def _append(
        self,
        amount: int,
        account_from: str,
        account_to: str,
        category: str,
        memo: str,
        negate: bool = False,
    ) -> None:
        signed_amount = -abs(amount) if negate else abs(amount)
        self.balance += signed_amount
        self.transactions.append(
            Transaction(
                timestamp=date.today(),
                account_from=account_from,
                account_to=account_to,
                category=category,
                amount=signed_amount,
                memo=memo,
            )
        )

    def copy(self) -> "FinanceLedger":
        return replace(self, transactions=list(self.transactions))
