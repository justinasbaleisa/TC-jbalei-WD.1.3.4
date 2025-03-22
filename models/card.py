class Card:

    RANKS = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    VALUES = {rank: index + 2 for index, rank in enumerate(RANKS)}

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = Card.VALUES[rank]

    def __str__(self):
        return f"Card: {self.rank} of {self.suit} valued '{self.value}'"

    def __eq__(self, other):
        return self.value == other.value

    def __gt__(self, other):
        return self.value > other.value
