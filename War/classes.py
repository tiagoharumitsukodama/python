from random import shuffle

class Card():
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def getRank(self):
        return self.rank

    def getValue(self):
        RANKS = Deck.RANKS
        return RANKS.index(self.rank)


class Hand():
    def __init__(self):
    	self.array = []

    def addCard(self, card):
        self.array.append(card)

    def releaseCard(self, index=0):
    	return self.array.pop(index)

    def stringCards(self):
        cards = '[ '

        for card in self.array:
            cards = cards + card.rank
            cards = cards + ' '

        return cards+']'

    def __len__(self):
        return len(self.array)


class Player():
    def __init__(self):
        self.hand = Hand()

    def setHand(self, cards):
        for card in cards:
            self.hand.addCard(card)

    def winTurn(self, cards):
        for card in cards:
            self.hand.addCard(card)

    def play(self):
        return self.hand.releaseCard()

    def war(self):
        sequence = []
        sequence.append( self.hand.releaseCard() )
        sequence.append( self.hand.releaseCard() )
        sequence.append( self.hand.releaseCard() )
        return sequence

    def __str__(self):
        return self.hand.stringCards()

    def __len__(self):
        return len(self.hand)

class Deck():

    SUITE = 'H D S C'.split()
    RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

    def __init__(self):

        self.allCards = []

        for suite in Deck.SUITE:
            for rank in Deck.RANKS:
                card = Card(suite, rank)
                self.allCards.append(card)

        shuffle(self.allCards)

    def distribuiteCardsPlayer1(self):
        return self.allCards[0:26]

    def distribuiteCardsPlayer2(self):
        return self.allCards[26:53]
