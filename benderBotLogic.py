class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank=0):
        self.suit = suit
        self.rank = rank
    
    def cmp(self, other):
        # Check the suits
        if self.suit > other.suit: return 1
        if self.suit < other.suit: return -1
        # Suits are the same... check ranks
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        # Ranks are the same... it's a tie
        return 0
    
    def __str__(self):
        return (self.ranks[self.rank] + " of " + self.suits[self.suit])

    def __eq__(self, other):
        return self.cmp(other) == 0

    def __le__(self, other):
        return self.cmp(other) <= 0

    def __ge__(self, other):
        return self.cmp(other) >= 0

    def __gt__(self, other):
        return self.cmp(other) > 0

    def __lt__(self, other):
        return self.cmp(other) < 0

    def __ne__(self, other):
        return self.cmp(other) != 0


class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank))
    def print_deck(self):
        for card in self.cards:
            print(card)
    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s = s + " " * i + str(self.cards[i]) + "\n"
        return s
    def pop(self):
        return self.cards.pop()
    def is_empty(self):
        return self.cards == []
    def shuffle(self):
        import random
        rng = random.Random()        # Create a random generator
        rng.shuffle(self.cards)      # uUse its shuffle method


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