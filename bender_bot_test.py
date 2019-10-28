import unittest
from benderBotLogic import *

class BenderBotTest(unittest.TestCase):
    
    def test001_a_player_has_only_2_cards_when_it_starts(self):
        aDeck = Deck()
        playerHand = BlackJackHand(aDeck)
        self.assertEqual(2,len(playerHand.getCards()))

if __name__ == '__main__':
    unittest.main()