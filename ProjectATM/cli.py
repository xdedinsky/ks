def _help_main() -> None:
    print("""
    Príkazy:
      help               - nápoveda
      show_cards         - zoznam kariet
      select <cislo>     - práca s kartou
      quit               - koniec
    """)


def _help_card() -> None:
    print("""
    Príkazy karty:
      balance            - zostatok
      deposit <suma>     - vklad
      withdraw <suma>    - výber
      done               - späť
      help               - nápoveda
    """)


def run_cli(atm) -> None:
    print("\n===== Vitajte v ATM =====")
    _help_main()

    while True:
        cmd = input("ATM> ").strip().split()
        if not cmd:
            continue
        action = cmd[0].lower()

        if action == "help":
            _help_main()

        elif action == "show_cards":
            print("\nKarty:")
            for c in atm.cards.values():
                print(f"  {c.number}  pin:{c.pin}  balance:{c.balance} €")
            print()

        elif action == "select":
            if len(cmd) < 2:
                print("Použi: select <cislo_karty>")
                continue
            number = cmd[1]
            pin = input("Zadaj PIN: ").strip()
            card = atm.authenticate(number, pin)
            if not card:
                print("Nesprávny PIN alebo karta neexistuje.\n")
                continue
            print(f"\nPracuješ s kartou {number}.")
            _help_card()

            while True:
                sub_cmd = input("CARD> ").strip().split()
                if not sub_cmd:
                    continue
                sub_action = sub_cmd[0].lower()

                if sub_action == "balance":
                    print(f"Zostatok: {card.balance} €")

                elif sub_action == "deposit":
                    if len(sub_cmd) < 2 or not sub_cmd[1].isdigit():
                        print("Použi: deposit <suma>")
                        continue
                    amount = int(sub_cmd[1])
                    try:
                        combo = atm.deposit_cash(amount)
                        card.deposit(amount)
                        print(f"Vložené {amount} € v: {combo}")
                    except ValueError as e:
                        print("Chyba:", e)

                elif sub_action == "withdraw":
                    if len(sub_cmd) < 2 or not sub_cmd[1].isdigit():
                        print("Použi: withdraw <suma>")
                        continue
                    amount = int(sub_cmd[1])
                    try:
                        combo = atm.withdraw_cash(amount)
                        card.withdraw(amount)
                        print(f"Vydané {amount} € v: {combo}")
                    except ValueError as e:
                        print("Chyba:", e)

                elif sub_action == "done":
                    print("\nKarta odhlásená.\n")
                    break

                elif sub_action == "help":
                    _help_card()

                else:
                    print("Neznámy príkaz. napíš 'help'.")

        elif action == "quit":
            print("\nĎakujeme. Dovidenia!")
            break

        else:
            print("Neznámy príkaz. napíš 'help'.")
