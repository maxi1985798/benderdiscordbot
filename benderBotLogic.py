suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    # def cmp(self, other):
    #     # Check the suits
    #     if self.suit > other.suit: return 1
    #     if self.suit < other.suit: return -1
    #     # Suits are the same... check ranks
    #     if self.rank > other.rank: return 1
    #     if self.rank < other.rank: return -1
    #     # Ranks are the same... it's a tie
    #     return 0
    
    # def __str__(self):
    #     return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    # def __eq__(self, other):
    #     return self.cmp(other) == 0

    # def __le__(self, other):
    #     return self.cmp(other) <= 0

    # def __ge__(self, other):
    #     return self.cmp(other) >= 0

    # def __gt__(self, other):
    #     return self.cmp(other) > 0

    # def __lt__(self, other):
    #     return self.cmp(other) < 0

    # def __ne__(self, other):
    #     return self.cmp(other) != 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suits[suit],ranks[rank]))
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
        import random
        rng = random.Random()        # Create a random generator
        rng.shuffle(self.cards)      # uUse its shuffle method

class BlackJackHand:
    def __init__(self,deckToTakeCards):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
        self.values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
        self.deck = deckToTakeCards
        self.addCard()
        self.addCard()
        # initialCardOne = deckToTakeCards.deal()
        # initialCardTwo = deckToTakeCards.deal()
        # self.deck = deckToTakeCards
        # self.cards.append(initialCardOne)
        # if initialCardOne.rank == 'Ace':
        #     self.aces += 1
        # self.cards.append(initialCardTwo)
        # if initialCardTwo.rank == 'Ace':
        #     self.aces += 1
        
    def getCards(self):
        return self.cards
    def addCard(self):
        card = self.deck.deal()
        self.cards.append(card)
        self.value += self.values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1



class Chips:
    
    def __init__(self,initialChips):
        self.total = initialChips  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -+ self.bet

class Player:
    def __init__(self,playerChips,playerHand):
        self.__chips = playerChips
        self.__hand = playerHand
    


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
        self.deck = Deck()

d = Deck()
print(d)