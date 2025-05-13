import unittest
from card import Card

class TestCard(unittest.TestCase):

    def setUp(self):
        """Iniciujeme karty s rôznymi zostatkami."""
        self.card1 = Card("1111222233334444", "1234", 1000)
        self.card2 = Card("5555666677778888", "0000", 50)
        self.card3 = Card("9999000011112222", "4321", 200)

    def test_deposit(self):
        """Testujeme vklad peňazí na kartu."""
        self.card1.deposit(500)
        self.assertEqual(self.card1.balance, 1500)

    def test_withdraw_success(self):
        """Testujeme výber peňazí z karty, keď je dostatok prostriedkov."""
        self.card1.withdraw(500)
        self.assertEqual(self.card1.balance, 500)

    def test_withdraw_insufficient_funds(self):
        """Testujeme výber peňazí, keď nie je dostatok prostriedkov na karte."""
        with self.assertRaises(ValueError):
            self.card2.withdraw(100)  # Karta má len 50 €

    def test_withdraw_more_than_balance(self):
        """Testujeme výber peňazí väčší ako je zostatok na karte."""
        with self.assertRaises(ValueError):
            self.card3.withdraw(300)  # Zostatok na karte je len 200 €

if __name__ == "__main__":
    unittest.main()