from atm import ATM
from card import Card
from cli import run_cli


def main() -> None:
    atm = ATM({500: 5, 200: 2, 100: 3, 50: 4, 20: 10, 10: 10, 5: 20, 2: 50, 1: 100})
    atm.add_card(Card("1111222233334444", "1234", 1000))
    atm.add_card(Card("5555666677778888", "0000", 50))
    atm.add_card(Card("9999000011112222", "4321", 200))
    run_cli(atm)


if __name__ == "__main__":
    main()
