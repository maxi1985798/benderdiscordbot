from benderBotLogic import *
import unittest
import random

class BenderBotTest(unittest.TestCase):
    
    def test_001_a_player_hand_has_only_2_cards_when_it_starts(self):
        rng = random.Random()        # Create a random generator
        aDeck = Deck(rng)
        playerHand = BlackJackHand(aDeck.deal(),aDeck.deal())
        self.assertEqual(2,len(playerHand.getCards()))

    def test_002_a_player_hand_has_only_3_cards(self):
        rng = random.Random()        # Create a random generator
        aDeck = Deck(rng)
        playerHand = BlackJackHand(aDeck.deal(),aDeck.deal())
        playerHand.addCard(aDeck.deal())
        self.assertEqual(3,len(playerHand.getCards()))

    def test_003_a_player_hand_has_only_4_cards(self):
        rng = random.Random()        # Create a random generator
        aDeck = Deck(rng)
        playerHand = BlackJackHand(aDeck.deal(),aDeck.deal())
        playerHand.addCard(aDeck.deal())
        playerHand.addCard(aDeck.deal())
        self.assertEqual(4,len(playerHand.getCards()))
    
    def test_004_a_player_hand_value_with_jack_queen_king_is_greater_tahn_21(self):
        jackCard = Card("Clubs","Jack")
        queenCard = Card("Clubs","Queen")
        kingCard = Card("Clubs","King")
        playerHand = BlackJackHand(jackCard,queenCard)
        playerHand.addCard(kingCard)
        self.assertEquals(playerHand.value(),30)

    def test_005_a_player_hand_value_with_jack_queen_is_20(self):
        jackCard = Card("Clubs","Jack")
        queenCard = Card("Clubs","Queen")
        playerHand = BlackJackHand(jackCard,queenCard)
        self.assertEquals(playerHand.value(),20)
    
    def test_006_dealer_hand_start_with_one_card(self):
        initialDealerCard = Card("Clubs","Jack")
        dealerHand = BlackJackDealerHand(initialDealerCard)
        self.assertEquals(len(dealerHand.getCards()),1)
    
    def test_007_dealer_hand_start_with_one_card(self):
        initialDealerCard = Card("Clubs","Jack")
        dealerHand = BlackJackDealerHand(initialDealerCard)
        self.assertEquals(len(dealerHand.getCards()),1)
    
    def test_008_dealer_must_add_a_card_when_he_takes_hit(self):
        rng = random.Random()        # Create a random generator
        aDeck = Deck(rng)
        aDealerHand = BlackJackDealerHand(aDeck.deal())
        aDealer = Dealer(aDeck,aDealerHand)
        playerHand01 = BlackJackHand(aDeck.deal(),aDeck.deal())
        playerHand02 = BlackJackHand(aDeck.deal(),aDeck.deal())
        playerHand03 = BlackJackHand(aDeck.deal(),aDeck.deal())
        player01 = Player("player01 name",playerHand01,aDealer)
        player02 = Player("player02 name",playerHand02,aDealer)
        player03 = Player("player03 name",playerHand03,aDealer)
        players = [player01,player02,player03]
        aBlackJackGame = BlackJackGame(aDeck,aDealer,players)
        self.assertTrue(aBlackJackGame.isPlaying(player01))
        # aDealer.deal()
        # # self.assertEquals(aDealer.currentPlayer(),1)
        # self.assertEquals(len(playerHand01.getCards()),3)
        # self.assertEquals(len(playerHand02.getCards()),2)
        # self.assertEquals(len(playerHand03.getCards()),2)
        # self.assertEquals(len(aDealerHand.getCards()),1)
        # aDealer.deal()
        # # aDealer.playerStand()
        # self.assertEquals(len(playerHand01.getCards()),3)
        # self.assertEquals(len(playerHand02.getCards()),3)
        # self.assertEquals(len(playerHand03.getCards()),2)
        # self.assertEquals(len(aDealerHand.getCards()),1)
        # aDealer.playerStand()
        # self.assertEquals(len(playerHand01.getCards()),3)
        # self.assertEquals(len(playerHand02.getCards()),3)
        # self.assertEquals(len(playerHand03.getCards()),2)
        # self.assertEquals(len(aDealerHand.getCards()),1)
        # aDealer.deal()
        # self.assertEquals(len(playerHand01.getCards()),3)
        # self.assertEquals(len(playerHand02.getCards()),3)
        # self.assertEquals(len(playerHand03.getCards()),2)
        # self.assertEquals(len(aDealerHand.getCards()),2)

    # def test_009_when_a_player_has_more_than_21_dealer_must_pass(self):
    #     rng = random.Random()        # Create a random generator
    #     aDeck = Deck(rng)
        # aDealerHand = BlackJackDealerHand(aDeck.deal())
        # playerHand01 = BlackJackHand(aDeck.deal(),aDeck.deal())
        # playerHand02 = BlackJackHand(aDeck.deal(),aDeck.deal())
        # playerHands = [playerHand01,playerHand02]
        # aDealer = Dealer(aDeck,aDealerHand,playerHands)
        # self.assertEquals(aDealer.currentPlayer(),0)
        # while playerHand01.value() <= 21 :
        #     aDealer.deal()
        # self.assertEquals(aDealer.currentPlayer(),1)
    # def test_010_when_a_player_has_more_than_dealer_player_wins(self):
    #     rng = random.Random()        # Create a random generator
        # aDeck = Deck(rng)
        # jackCard = Card("Clubs","Jack")
        # queenCard = Card("Clubs","Queen")
        # sevenCard = Card("Clubs","7")
        # playerHand01 = BlackJackHand(queenCard,jackCard)
        # aDealerHand = BlackJackDealerHand(sevenCard)
        # playerHands = [playerHand01]
        # aDealer = Dealer(aDeck,aDealerHand)
        # player01 = Player("player01 name",playerHand01,aDealer)
        # players = [player01]
        # aBlackJackGame = BlackJackGame(aDeck,aDealer,players)
        # aBlackJackGame.currentPlayerStand()
        # aBlackJackGame.currentPlayerStand()
        # self.assertEquals(aBlackJackGame,1)


if __name__ == '__main__':
    unittest.main()