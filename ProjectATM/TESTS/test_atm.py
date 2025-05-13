import unittest
from atm import ATM
from card import Card

class TestATM(unittest.TestCase):

    def setUp(self):
        """Iniciujeme ATM s niekoľkými bankovkami a testovacími kartami."""
        self.atm = ATM({500: 5, 200: 2, 100: 3, 50: 4, 20: 10, 10: 10, 5: 20, 2: 50, 1: 0})
        self.card1 = Card("1111222233334444", "1234", 1000)
        self.card2 = Card("5555666677778888", "0000", 50)
        self.card3 = Card("9999000011112222", "4321", 200)
        self.atm.add_card(self.card1)
        self.atm.add_card(self.card2)
        self.atm.add_card(self.card3)

    def test_authenticate_valid(self):
        """Testujeme správnu autentifikáciu s platným PIN-om."""
        card = self.atm.authenticate("1111222233334444", "1234")
        self.assertIsNotNone(card)
        self.assertEqual(card.number, "1111222233334444")

    def test_authenticate_invalid_pin(self):
        """Testujeme nesprávny PIN."""
        card = self.atm.authenticate("1111222233334444", "0000")
        self.assertIsNone(card)

    def test_withdraw_cash_success(self):
        """Testujeme výber peňazí z bankomatu (validná suma)."""
        combo = self.atm.withdraw_cash(500)
        self.assertEqual(self.atm.banknotes[500], 4)
        self.assertIn(500, combo)

    def test_withdraw_cash_failure(self):
        """Testujeme výber peňazí, ktorú bankomat nemôže spracovať (napr. neexistujúca suma)."""
        with self.assertRaises(ValueError):
            self.atm.withdraw_cash(6) 

    def test_deposit_cash(self):
        """Testujeme vklad peňazí do bankomatu."""
        combo = self.atm.deposit_cash(600)
        self.assertEqual(self.atm.banknotes[500], 6)
        self.assertIn(500, combo)

if __name__ == "__main__":
    unittest.main()