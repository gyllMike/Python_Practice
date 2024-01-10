import random

class Card:
    """Represents a standard playing card."""

    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank

    suit_names = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "Queen", "King"]

    def __str__(self):  # can return string
        return "%s of % s" % (Card.rank_names[self.rank], Card.suit_names[self.suit])

    def __lt__(self, other):
        # check the suits
        if self.suit < other.suit:
            return True
        if self.suit > other.suit:
            return False
        # suits are the same... check ranks
        return self.rank < other.rank

class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return "\n".join(res)

    def pop_card(self):
         return self.cards.pop()

    def add_card(self, card):
         self.cards.append(card)

    def shuffle(self):
         random.shuffle(self.cards)

    def sort_card(self):
        self.cards.sort()

    def move_cards(self, hand, num):
        for i in range(num):
            hand.add_card(self.pop_card())


class Hand(Deck):
    """Represents a hand of playing cards."""

    #small and big in programming are parent cards(big) and child cards(small)

    def __init__(self, label=""):
        self.cards = []
        self.label = label
        #lable is for giving a name, distinguishing who is play the game,can rename the lable whatever u want


deck = Deck()
deck.shuffle()

hand = Hand()

deck.move_cards(hand,5)
hand.sort_card()