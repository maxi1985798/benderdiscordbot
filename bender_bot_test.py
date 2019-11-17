from benderBotLogic import *
import unittest
import random

class FakeRandomGenerator:
    def shuffle(self,aList):
        pass

class BenderBotTest(unittest.TestCase):

    def getListOfSortedCards(self):
        cards = []
        for suit in range(4):
            for rank in range(1, 14):
                cards.append(Card(suits[suit],ranks[rank]))
        return cards
    
    def test_001_a_player_hand_has_only_2_cards_when_it_starts(self):
        cards = self.getListOfSortedCards()
        rng = FakeRandomGenerator()        # Create a random generator
        aDeck = Deck(rng,cards)
        playerHand = BlackJackHand(aDeck.deal(),aDeck.deal())
        self.assertEqual(2,len(playerHand.getCards()))

    def test_002_a_player_hand_has_only_3_cards(self):
        cards = self.getListOfSortedCards()
        rng = FakeRandomGenerator()        # Create a random generator
        aDeck = Deck(rng,cards)
        playerHand = BlackJackHand(aDeck.deal(),aDeck.deal())
        playerHand.addCard(aDeck.deal())
        self.assertEqual(3,len(playerHand.getCards()))

    def test_003_a_player_hand_has_only_4_cards(self):
        cards = self.getListOfSortedCards()
        rng = FakeRandomGenerator()        # Create a random generator
        aDeck = Deck(rng,cards)
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
        cards = self.getListOfSortedCards()
        rng = FakeRandomGenerator()        # Create a random generator
        aDeck = Deck(rng,cards)
        aDealerHand = BlackJackDealerHand(aDeck.deal())
        aDealer = Dealer(aDeck,aDealerHand)
        twoCard = Card("Clubs","2")
        threeCard = Card("Clubs","3")
        playerHand01 = BlackJackHand(twoCard,threeCard)
        playerHand02 = BlackJackHand(aDeck.deal(),aDeck.deal())
        playerHand03 = BlackJackHand(aDeck.deal(),aDeck.deal())
        player01 = Player("player01id",playerHand01,aDealer)
        player02 = Player("player02id",playerHand02,aDealer)
        player03 = Player("player03id",playerHand03,aDealer)
        players = [player01,player02,player03]
        aBlackJackGame = BlackJackGame(aDeck,aDealer,players)
        aBlackJackGame.currentPlayerTakeHit()
        self.assertTrue(aBlackJackGame.isCurrentPlayer("player01id"))
        self.assertEqual(3,len(aBlackJackGame.cardsOf("player01id")))

    def test_009_when_a_player_has_more_than_21_dealer_must_pass(self):
        cards = self.getListOfSortedCards()
        rng = FakeRandomGenerator()        # Create a random generator
        aDeck = Deck(rng,cards)
        aDealerHand = BlackJackDealerHand(aDeck.deal())
        aDealer = Dealer(aDeck,aDealerHand)
        playerHand01 = BlackJackHand(aDeck.deal(),aDeck.deal())
        playerHand02 = BlackJackHand(aDeck.deal(),aDeck.deal())
        playerHand03 = BlackJackHand(aDeck.deal(),aDeck.deal())
        player01 = Player("player01id",playerHand01,aDealer)
        player02 = Player("player02id",playerHand02,aDealer)
        player03 = Player("player03id",playerHand03,aDealer)
        players = [player01,player02,player03]
        aBlackJackGame = BlackJackGame(aDeck,aDealer,players)
        aBlackJackGame.currentPlayerTakeHit()
        self.assertTrue(aBlackJackGame.isCurrentPlayer("player02id"))
        self.assertEqual(3,len(aBlackJackGame.cardsOf("player01id")))
        self.assertEqual(2,len(aBlackJackGame.cardsOf("player02id")))
        self.assertTrue(player01.handValue()>21)

    def test_010_game_is_finished_when_dealer_stand(self):
        cards = self.getListOfSortedCards()
        rng = FakeRandomGenerator()        # Create a random generator
        aDeck = Deck(rng,cards)
        jackCard = Card("Clubs","Jack")
        queenCard = Card("Clubs","Queen")
        sevenCard = Card("Clubs","7")
        playerHand01 = BlackJackHand(queenCard,jackCard)
        aDealerHand = BlackJackDealerHand(sevenCard)
        aDealer = Dealer(aDeck,aDealerHand)
        player01 = Player("player01 name",playerHand01,aDealer)
        players = [player01]
        aBlackJackGame = BlackJackGame(aDeck,aDealer,players)
        aBlackJackGame.currentPlayerStand()
        aBlackJackGame.currentPlayerStand()
        self.assertTrue(aBlackJackGame.isFinished())

    def test_011_game_is_not_finished_when_game_starts(self):
        cards = self.getListOfSortedCards()
        rng = FakeRandomGenerator()        # Create a random generator
        aDeck = Deck(rng,cards)
        jackCard = Card("Clubs","Jack")
        queenCard = Card("Clubs","Queen")
        sevenCard = Card("Clubs","7")
        playerHand01 = BlackJackHand(queenCard,jackCard)
        aDealerHand = BlackJackDealerHand(sevenCard)
        aDealer = Dealer(aDeck,aDealerHand)
        player01 = Player("player01 name",playerHand01,aDealer)
        players = [player01]
        aBlackJackGame = BlackJackGame(aDeck,aDealer,players)
        self.assertFalse(aBlackJackGame.isFinished())

    def test_012_bender_can_starts_a_BlackJackGame_with_one_player(self):
        cards = self.getListOfSortedCards()
        player01Id = "111111"
        benderBot = Bender()
        aDeck = Deck(FakeRandomGenerator(),cards)
        benderBot.createGame(aDeck,[player01Id])
        blackjGames = benderBot.getBlackjGames()
        self.assertTrue(len(blackjGames) == 1)
    
    def test_013_bender_can_starts_a_BlackJackGame_with_two_player(self):
        cards = self.getListOfSortedCards()
        player01Id = "111111"
        player02Id = "222222"
        benderBot = Bender()
        aDeck = Deck(FakeRandomGenerator(),cards)
        benderBot.createGame(aDeck,[player01Id,player02Id])
        blackjGames = benderBot.getBlackjGames()
        self.assertTrue(len(blackjGames) == 1)
        self.assertTrue(len(blackjGames[0].currentPlayers()) == 2)

    def test_014_when_the_current_player_take_hit_should_have_3_cards(self):
        cards = self.getListOfSortedCards()
        player01Id = "111111"
        player02Id = "222222"
        benderBot = Bender()
        aDeck = Deck(FakeRandomGenerator(),cards)
        benderBot.createGame(aDeck,[player01Id,player02Id])
        benderBot.takeHitFor(player01Id)
        blackjGames = benderBot.getBlackjGames()
        self.assertTrue(len(blackjGames[0].cardsOf(player01Id)) == 3)
        self.assertTrue(len(blackjGames[0].cardsOf(player02Id)) == 2)
        
    def test_015_when_not_a_current_player_take_hit_should_inform_an_error(self):
        cards = self.getListOfSortedCards()
        player01Id = "111111"
        player02Id = "222222"
        benderBot = Bender()
        aDeck = Deck(FakeRandomGenerator(),cards)
        benderBot.createGame(aDeck,[player01Id,player02Id])
        with self.assertRaises(NotPlayerTurnsException) as cm:
            benderBot.takeHitFor(player02Id)
        
        self.assertEqual('It is not player '+player02Id+' turns',str(cm.exception))

    def test_016_a_player_can_not_be_in_two_games(self):
        cards = self.getListOfSortedCards()
        player01Id = "111111"
        player02Id = "222222"
        player03Id = "222222"
        benderBot = Bender()
        aDeck = Deck(FakeRandomGenerator(),cards)
        benderBot.createGame(aDeck,[player01Id,player02Id])
        with self.assertRaises(PlayerCanNotBeInMultipleGamesException) as cm:
            benderBot.createGame(aDeck,[player03Id,player02Id])
        
        self.assertEqual(Bender.playerCanNotBeInMultipleGamesErrorMessage(),str(cm.exception))
    def test_017_different_player_can_play_in_different_games(self):
        cards0 = self.getListOfSortedCards()
        cards1 = self.getListOfSortedCards()
        cards2 = self.getListOfSortedCards()
        player01Id = "111111"
        player02Id = "222222"
        player03Id = "333333"
        benderBot = Bender()
        aDeck0 = Deck(FakeRandomGenerator(),cards0)
        aDeck1 = Deck(FakeRandomGenerator(),cards1)
        aDeck2 = Deck(FakeRandomGenerator(),cards2)
        benderBot.createGame(aDeck0,[player01Id])
        benderBot.createGame(aDeck1,[player02Id])
        benderBot.createGame(aDeck2,[player03Id])
        benderBot.takeHitFor(player01Id)
        benderBot.takeHitFor(player02Id)
        benderBot.takeHitFor(player03Id)
        blackjGames = benderBot.getBlackjGames()
        self.assertTrue(len(blackjGames) == 3)
        self.assertTrue(len(blackjGames[0].currentPlayers()) == 1)
        self.assertTrue(len(blackjGames[1].currentPlayers()) == 1)
        self.assertTrue(len(blackjGames[2].currentPlayers()) == 1)
        

if __name__ == '__main__':
    unittest.main()