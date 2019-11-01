suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

class Deck:
    def __init__(self,aRandomGenerator):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suits[suit],ranks[rank]))
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
    def __init__(self,name,playerHand,aDealer):
        self.__playerName = name
    def name(self):
        return self.__playerName
class BlackJackGame:
    def __init__(self,deck,dealer,players):
        self.__deck = deck
        self.__dealer = dealer
        self.__players = players
        # for p in players:
        #     self.__playersAndHands[p] = BlackJackHand(self.__deck.deal(),self.__deck.deal())
        self.__currentPlayer = players[0]
    def currentPlayerStand(self):
        self.__dealer.playerStand()
    def isPlaying(self,aPlayer):
        return self.__currentPlayer == aPlayer



# class Chips:
    
#     def __init__(self,initialChips):
#         self.total = initialChips  # This can be set to a default value or supplied by a user input
#         self.bet = 0
        
#     def win_bet(self):
#         self.total += self.bet
    
#     def lose_bet(self):
#         self.total -+ self.bet




class BenderBot:

    def __init__(self,token):
        self.token = token
        self.hookers = ['https://i.imgur.com/VSP8EBp.jpg',
            'https://i.imgur.com/Z5pYMOB.jpg', 
            'https://i.imgur.com/BmAr75a.jpg',
            'https://i.imgur.com/KqKqV0w.jpg',
            'https://i.imgur.com/zg07iek.jpg',
            'https://i.imgur.com/lR6MiJK.jpg',
            'https://i.imgur.com/oulOY.jpg',
            'https://i.imgur.com/bli8Q5c.jpg',
            'https://tenor.com/view/pretty-woman-julia-roberts-richard-gere-gif-5736316'
            ]
        # self.deck = Deck()

# d = Deck()
# print(d)