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

class Player :

    def __init__(self, name) :
        self.name = name
        self._bankroll = 0
        self._bet = 0
        self._blackjack = 0

    def get_name(self):
        return self.name

    def _get_bankroll(self):
        return self._bankroll

    def _get_bet(self):
        return self._bet

    def _get_blackjack(self):
        return self._blackjack

    def _set_bet(self, n_bet):
        self._bet = n_bet

    def _set_bankroll(self, n_bankroll):
        self._bankroll = n_bankroll


    def _set_blackjack(self, n_blackjack):
        self._blackjack = n_blackjack


    bankroll = property(_get_bankroll, _set_bankroll)
    bet = property(_get_bet, _set_bet)
    bj = property(_get_blackjack, _set_blackjack)



p1 = Player("Joe")
p1.bankroll = 20
p1.bet = 2
print(p1.bankroll)
print(p1.bet)

n = 1
p_list = blackjack.init_players(n)
deck = blackjack.generate_final_deck()
mains = blackjack.creer_mains(n, p_list, deck)
player_issue = blackjack.comparer_scores(mains, n)
print player_issue

for i in range(n):
        assert len( player_issue[i] ) == 1

print( blackjack.pay(n, player_issue, p_list) )

print "pas d'erreur jusqu'ici"


 

if __name__ == '__main__':
    unittest.main()
