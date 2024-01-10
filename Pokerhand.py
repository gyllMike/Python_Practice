from card import Hand, Deck

class PokerHand(Hand):
    """Represents a poker hand."""
#=======================================================================================================================
    def make_histograms(self):
        """Builds histograms for suits and ranks."""
        self.suits = {}
        self.ranks = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1

    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise."""
        self.make_histograms()
        for val in self.ranks.values():
            if val == 2:
                return True
        return False

    def has_twopair(self):
        """Returns True if the hand has two pair, False otherwise."""
        self.make_histograms()
        count = 0
        for val in self.ranks.values():
            if val == 2:
                count += 1
        return count == 2

    def has_three_of_a_kind(self):
        """Returns True if the hand has three of a kind, False otherwise."""
        self.make_histograms()
        for val in self.ranks.values():
            if val == 3:
                return True
        return False

    def has_straight(self):
        """Returns True if the hand has a straight, False otherwise."""
        self.make_histograms()
        ranks = list(self.ranks.keys())
        ranks.sort()

        # Check for Ace, 2, 3, 4, 5 straight
        if ranks == [1, 2, 3, 4, 5]:
            return True

        # Check for other straights
        for i in range(len(ranks) - 4):
            if ranks[i:i + 5] == list(range(ranks[i], ranks[i] + 5)):
                return True

    def has_straight_flush(self):
        """Returns True if the hand has a straight flush, False otherwise."""
        self.make_histograms()

        # Check for straight flush in each suit
        for suit in self.suits:
            if self.has_straight_flush_in_suit(suit):
                return True
        return False

    def has_straight_flush_in_suit(self, suit):
        """Returns True if the hand has a straight flush in the given suit, False otherwise."""
        ranks_in_suit = [card.rank for card in self.cards if card.suit == suit]
        ranks_in_suit.sort()

        # Check for Ace, 2, 3, 4, 5 straight flush
        if ranks_in_suit == [1, 2, 3, 4, 5]:
            return True

        # Check for other straight flushes
        for i in range(len(ranks_in_suit) - 4):
            if ranks_in_suit[i:i + 5] == list(range(ranks_in_suit[i], ranks_in_suit[i] + 5)):
                return True

        return False

    def has_four_of_a_kind(self):
        """Returns True if the hand has four of a kind, False otherwise."""
        self.make_histograms()
        for val in self.ranks.values():
            if val == 4:
                return True
        return False

    def has_full_house(self):
        """Returns True if the hand has a full house, False otherwise."""
        self.make_histograms()
        return 3 in self.ranks.values() and 2 in self.ranks.values()

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.
        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False

#=======================================================================================================================

    def classify(self):
        """Sets the label attribute to the highest-value classification."""
        if self.has_straight_flush():
            self.label = "Straight Flush"
        elif self.has_four_of_a_kind():
            self.label = "Four of a Kind"
        elif self.has_full_house():
            self.label = "Full House"
        elif self.has_flush():
            self.label = "Flush"
        elif self.has_straight():
            self.label = "Straight"
        elif self.has_three_of_a_kind():
            self.label = "Three of a Kind"
        elif self.has_twopair():
            self.label = "Two Pair"
        elif self.has_pair():
            self.label = "Pair"
        else:
            self.label = "High Card"

    def classify_probability(self, num_trials=1000000):
        """Estimates the probabilities of different hands based on simulation."""
        hand_counts = {"Pair": 0, "Two Pair": 0, "Three of a Kind": 0, "Straight": 0,
                       "Flush": 0, "Full House": 0, "Four of a Kind": 0, "Straight Flush": 0, "High Card": 0}

        for _ in range(num_trials):
            deck = Deck()
            deck.shuffle()

            self.move_cards(Hand(), 7)  # Assume `Hand` has a `move_cards` method
            self.sort_card()

            self.classify()
            label = self.label
            hand_counts[label] += 1

        probabilities = {label: count / num_trials for label, count in hand_counts.items()}

        for label, probability in probabilities.items():
            print(f"{label}: Probability = {probability}")

        return probabilities

#=======================================================================================================================
deck = Deck()
deck.shuffle()

# deal the cards and classify the hands
for i in range(7):
    hand = PokerHand()
    deck.move_cards(hand, 5)
    hand.sort_card()
    print(hand)
    print(hand.classify()) #you can change any method of class in here, if you want
    print('')

#hand = PokerHand()
#hand.classify_probability(num_trials=1000000) #if you want to run, please delete #
#=======================================================================================================================

#In this code, there are some methods is not come from my idea, I use another' mind to help me finish this work.
#But I can make sure there are some of my own ideas in this code. Because time is not enough to let me think a lot, I choose
#quick way to let me finish this project first, and later, maybe after this semester I will look at project 5 again. At present
#I am very busy on another courses and I also have another project(Chapter 13) need to do, so I think I can finish Chapter 13
#by myself with my own idea first and then consider about the project 5. However, I find I may donot have enough time to do the
#project 5 after I finished Chapter 13 by my self. This is the reason why I choose a efficient way to finish project 5.
#It is my own problem, please understand, thank you.