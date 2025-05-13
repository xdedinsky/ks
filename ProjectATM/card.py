from dataclasses import dataclass

@dataclass
class Card:
    number: str
    pin: str
    balance: int

    def deposit(self, amount: int) -> None:
        self.balance += amount

    def withdraw(self, amount: int) -> None:
        if amount > self.balance:
            raise ValueError("Nedostatok prostriedkov na karte.")
        self.balance -= amount