from random import shuffle

from models.card import Card
from models.hand import Hand
from models.player import Player


class Deck:

    def __init__(self):
        self.cards: list = [
            Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS
        ]

    def __str__(self):
        return f"Deck:\n- {'\n- '.join(str(card) for card in self.cards)}"

    def __contains__(self, card):
        return card in self.cards

    @property
    def capacity(self):
        return len(Card.RANKS) * len(Card.SUITS)

    @property
    def cards_left(self):
        return len(self.cards)

    def shuffle(self) -> None:
        shuffle(self.cards)

    def deal(self, quantity: int) -> None:
        if len(self.cards) <= 0:
            raise ValueError(
                f"Not enough cards. "
                f"Deck is epmpty"
            )
        if len(self.cards) < quantity:
            raise ValueError(
                f"Not enough cards. "
                f"Deck has '{len(self.cards)}', "
                f"but requested '{quantity}' cards"
        )
        dealt_cards = self.cards[:quantity]
        self.cards = self.cards[quantity:]
        return dealt_cards