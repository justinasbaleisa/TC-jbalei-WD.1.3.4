from random import shuffle

from models.card import Card


class Deck:

    def __init__(self):
        self.cards = [
            Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS
        ]

    def __str__(self):
        return f"Deck:\n- {'\n- '.join(str(card) for card in self.cards)}"

    def __contains__(self, card):
        return card in self.cards
    
    def shuffle(self):
        shuffle(self.cards)

    def deal(self):
        first_hand = []
        second_hand = []
        shift = True
        if len(self.cards) <= 0:
            raise ValueError(f"Not enough '{len(self.cards)}' cards in Deck to deal.")
        while self.cards:
            card = self.cards.pop(0)
            if shift:
                first_hand.append(card)
            else:
                second_hand.append(card)
            shift = not shift
        return first_hand, second_hand
