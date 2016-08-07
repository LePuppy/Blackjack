import unittest
from .context import core
from core import blackjack

class cardnameTests(unittest.TestCase):
    """Tests for cardname() in `blackjack.py`."""

    def test_exceptions(self):
        self.assertEqual(blackjack.cardname(-1), 'carte invalide')
        self.assertEqual(blackjack.cardname(52), 'carte invalide')
        self.assertEqual(blackjack.cardname(31.3), 'carte invalide')

    def test_valid_cards(self):
        self.assertEqual(blackjack.cardname(0), 'as de trefles')
        self.assertEqual(blackjack.cardname(13), 'as de carreaux')
        self.assertEqual(blackjack.cardname(26), 'as de coeurs')
        self.assertEqual(blackjack.cardname(39), 'as de piques')
        self.assertEqual(blackjack.cardname(40), '2 de piques')
        self.assertEqual(blackjack.cardname(48), '10 de piques')
        self.assertEqual(blackjack.cardname(51), 'roi de piques')

class generateDeckTests(unittest.TestCase):
    """Tests for generate_deck() in `blackjack.py`."""

    def setUp(self):
        """generating deck as `self.deck` before running each test"""
        self.deck = blackjack.generate_deck()

    def test_deck_length(self):
        self.assertEqual(len(self.deck), 52)

    def test_all_cards_in_deck(self):
        for i in range(52):
            self.assertIn(i, self.deck)

class evaluerCarteTests(unittest.TestCase):
    """Tests for evaluer_carte() in `blackjack.py`."""

    def test_card_values(self):
        self.assertEqual(blackjack.evaluer_carte(0), 11)
        self.assertEqual(blackjack.evaluer_carte(1), 2)
        self.assertEqual(blackjack.evaluer_carte(2), 3)
        self.assertEqual(blackjack.evaluer_carte(11), 10)
        self.assertEqual(blackjack.evaluer_carte(25), 10)
        self.assertEqual(blackjack.evaluer_carte(40), 2)
        # TODO: ajouter cas as == 1

class evaluerMainTests(unittest.TestCase):
    """Tests for evaluer_main() in `blackjack.py`."""

    def test_hand_values(self):
        self.assertEqual(blackjack.evaluer_main([1]), 2)
        self.assertEqual(blackjack.evaluer_main([1,2]), 5)
        self.assertEqual(blackjack.evaluer_main([]), 0)
        self.assertEqual(blackjack.evaluer_main([14]), 2)

if __name__ == '__main__':
    unittest.main()
