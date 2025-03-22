class Deck:

    def __init__(self):
        self.cards = [
            Card(rank, suit) for rank in Card.RANKS for suit in Card.SUITS
        ]

    def __str__(self):
        return f"Deck:\n- {'\n- '.join(str(card) for card in self.cards)}"

    def shuffle(self):
        from random import shuffle
        shuffle(self.cards)

    def deal(self):
        first_hand = []
        second_hand = []
        shift = True
        for card in self.cards:
            if shift:
                first_hand.append(card)
            else:
                second_hand.append(card)
            shift = not shift
        return first_hand, second_hand
