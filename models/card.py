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

    def __init__(self, rank: str, suit: str):
        self.rank = rank
        self.suit = suit
        self.value = Card.VALUES[self.rank]

    def __str__(self):
        return f"Card: {self.rank} of {self.suit} valued '{self.value}'"

    def __eq__(self, other: int) -> bool:
        return self.value == other.value

    def __gt__(self, other: int) -> bool:
        return self.value > other.value

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value: str):
        if isinstance(value, str):
            value = value.capitalize()
            if value in Card.RANKS:
                self._rank = value
                return
        raise ValueError(f"Invalid rank '{value}' of type '{type(value).__name__}'")

    @property
    def suit(self):
        return self._suit

    @suit.setter
    def suit(self, value: str) -> None:
        if isinstance(value, str):
            value = value.capitalize()
            if value in Card.SUITS:
                self._suit = value
                return
        raise ValueError(f"Invalid suit '{value}' of type '{type(value).__name__}'")
