import random
import functools

suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self,aRandomGenerator,aSortedlistOfCards):
        self.cards = aSortedlistOfCards
        # for suit in range(4):
        #     for rank in range(1, 14):
        #         self.cards.append(Card(suits[suit],ranks[rank]))
        self.__randomGenerator = aRandomGenerator
    def print_deck(self):
        for card in self.cards:
            print(card)
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s
    def deal(self):
        return self.cards.pop()
    def is_empty(self):
        return self.cards == []
    def shuffle(self):
        self.__randomGenerator.shuffle(self.cards)      # uUse its shuffle method

class BlackJackHand:
    def __init__(self,initialCardOne,initialCardTwo):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.__value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        self.values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
        self.addCard(initialCardOne)
        self.addCard(initialCardTwo)
        
    def getCards(self):
        return self.cards

    def addCard(self,card):
        self.cards.append(card)
        self.__value += self.values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()
    
    def adjust_for_ace(self):
        while self.__value > 21 and self.aces:
            self.__value -= 10
            self.aces -= 1
    def value(self):
        return self.__value

class BlackJackDealerHand:
    def __init__(self,initialDealerCard):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.__value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        self.values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
        self.cards.append(initialDealerCard)
        self.__value += self.values[initialDealerCard.rank]
        if initialDealerCard.rank == 'Ace':
            self.aces += 1

    def getCards(self):
        return self.cards
        
    def addCard(self,card):
        self.cards.append(card)
        self.__value += self.values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        self.adjust_for_ace()
    
    def adjust_for_ace(self):
        while self.__value > 21 and self.aces:
            self.__value -= 10
            self.aces -= 1
    def value(self):
        return self.__value


class Dealer:
    def __init__(self,deck,dealerHand):
        self.__deck = deck
        self.__dealerHand = dealerHand
    def deal(self):
        return self.__deck.deal()

class Player:
    def __init__(self,id,playerHand,aDealer):
        self.__id = id
        self.__playerHand = playerHand
        self.__dealer = aDealer
    def playerHand(self):
        return self.__playerHand
    def id(self):
        return self.__id
    def takeHit(self):
        card = self.__dealer.deal()
        self.__playerHand.addCard(card)
    def getCards(self):
        return self.__playerHand.getCards()
    def handValue(self):
        return self.__playerHand.value()
class BlackJackGame:
    def __init__(self,deck,dealer,players):
        self.__deck = deck
        self.__dealer = dealer
        self.__players = players
        self.__finished = False
        # for p in players:
        #     self.__playersAndHands[p] = BlackJackHand(self.__deck.deal(),self.__deck.deal())
        self.__currentPlayer = players[0]
    def currentPlayer(self):
        return self.__currentPlayer
    def currentPlayerStand(self):
        if self.__currentPlayer == self.__dealer :
            self.__finished = True
        else:
            for i in range(len(self.__players)):
                if i == (len(self.__players) -1):
                    self.__currentPlayer = self.__dealer
                    break
                elif self.__players[i] == self.__currentPlayer:
                    self.__currentPlayer = self.__players[i+1]
                    break
        
    def isCurrentPlayer(self,playerId):
        return (self.__currentPlayer != self.__dealer) and (self.__currentPlayer.id() == playerId)
    def isPlaying(self,playerId):
        return any(p.id() == playerId for p in self.__players)
    def currentPlayerTakeHit(self):
        self.__currentPlayer.takeHit()
        if self.__currentPlayer.handValue() > 21:
            self.currentPlayerStand()
    
    def cardsOf(self,playerId):
        for p in self.__players:
            if p.id() == playerId:
                return p.getCards()

    def isFinished(self):
        return self.__finished
    def currentPlayers(self):
        return self.__players

class Bender:

    def __init__(self):
        self.__games = []
    def createGame(self,aDeck,playersId):
        self.validateIfPlayersAreNotPlaying(playersId)
        aDealerHand = BlackJackDealerHand(aDeck.deal())
        aDealer = Dealer(aDeck,aDealerHand)
        players = []
        for pId in playersId:
            aPlayerHand = BlackJackHand(aDeck.deal(),aDeck.deal())
            players.append(Player(pId,aPlayerHand,aDealer))
        aBlackJackGame = BlackJackGame(aDeck,aDealer,players)
        self.__games.append(aBlackJackGame)
    
    @staticmethod
    def playerCanNotBeInMultipleGamesErrorMessage():
        return 'A player can not be in multiple games'
    def validateIfPlayersAreNotPlaying(self,playersId):
        if any(self.isPlayingInSomeGame(p,self.__games) for p in playersId):
            raise PlayerCanNotBeInMultipleGamesException(Bender.playerCanNotBeInMultipleGamesErrorMessage())
    def isPlayingInSomeGame(self,aPlayerId, games):
        return any(g.isPlaying(aPlayerId) for g in games)
    def getBlackjGames(self):
        return self.__games
    def takeHitFor(self,ThePlayerIdWhohWantToTakeHit):
        gameOfThePlayer = list(filter(lambda g: g.isPlaying(ThePlayerIdWhohWantToTakeHit), self.__games))[0]
        if gameOfThePlayer.isCurrentPlayer(ThePlayerIdWhohWantToTakeHit):
            gameOfThePlayer.currentPlayerTakeHit()
        else:
            raise NotPlayerTurnsException('It is not player ' + ThePlayerIdWhohWantToTakeHit + ' turns')
        return gameOfThePlayer

def checkIfItIsPlaying():
    return True
class NotPlayerTurnsException(Exception):
    pass

class PlayerCanNotBeInMultipleGamesException(Exception):
    pass
