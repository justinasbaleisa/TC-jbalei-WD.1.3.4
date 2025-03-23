from models.hand import Hand


class Player:

    def __init__(self, name: str, hand: Hand = None):
        self.hand = hand
        self.name = name

    def __str__(self):
        return (
            f"Player: {self.name}, with {len(self.hand.cards)} cards:\n"
            f"- {'\n- '.join(str(card) for card in self.hand.cards)}"
        )

    @property
    def hand(self):
        return self._hand

    @hand.setter
    def hand(self, value: Hand):
        if isinstance(value, Hand):
            self._hand = value
            return
        raise ValueError(f"Invalid hand '{value}' of type '{type(value).__name__}'")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        if isinstance(value, str) and value.strip():
            self._name = value
            return
        raise ValueError(f"Invalid name '{value}' of type '{type(value).__name__}'")
