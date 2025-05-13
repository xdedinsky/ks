from typing import Dict, List, Optional
from card import Card

class ATM:
    DENOMS: List[int] = [500, 200, 100, 50, 20, 10, 5, 2, 1]

    def __init__(self, banknotes: Dict[int, int]):
        self.banknotes: Dict[int, int] = {d: banknotes.get(d, 0) for d in self.DENOMS}
        self.cards: Dict[str, Card] = {}

    def add_card(self, card: Card) -> None:
        self.cards[card.number] = card

    def authenticate(self, number: str, pin: str) -> Optional[Card]:
        card = self.cards.get(number)
        return card if card and card.pin == pin else None

    def _can_make_amount(self, amount: int):
        remaining = amount
        combo: Dict[int, int] = {}
        for d in self.DENOMS:
            take = min(remaining // d, self.banknotes.get(d, 0))
            if take:
                combo[d] = take
                remaining -= take * d
            if remaining == 0:
                break
        return combo if remaining == 0 else None

    def withdraw_cash(self, amount: int):
        combo = self._can_make_amount(amount)
        if combo is None:
            raise ValueError("Bankomat nevie vydať danú sumu.")
        for d, c in combo.items():
            self.banknotes[d] -= c
        return combo

    def deposit_cash(self, amount: int):
        remaining = amount
        combo: Dict[int, int] = {}
        for d in self.DENOMS:
            cnt = remaining // d
            if cnt:
                combo[d] = cnt
                remaining -= cnt * d
                self.banknotes[d] += cnt
        if remaining:
            raise ValueError(f"Zvyšok {remaining} € sa nedá spracovať.")
        return combo