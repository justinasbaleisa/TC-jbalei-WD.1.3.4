from models.card import Card


class Hand:

    def __init__(self, cards: Card | list[Card]):
        self.cards = cards

    def __str__(self):
        return f"Hand:\n- {'\n- '.join(str(card) for card in self.cards)}"

    def __contains__(self, card):
        return card in self.cards

    @property
    def cards(self):
        return self._cards

    @cards.setter
    def cards(self, value: Card | list[Card]):
        if isinstance(value, Card):
            value = [value]
        elif not isinstance(value, list):
            raise ValueError(
                f"Invalid card '{value}' " f"of type '{type(value).__name__}'"
            )

        seen_cards = set()
        for card in value:
            if not isinstance(card, Card):
                raise ValueError(
                    f"Invalid card '{card}' "
                    f"of type '{type(card).__name__}' "
                    f"not added into the Hand"
                )
            key = (card.rank, card.suit)
            if key in seen_cards:
                raise ValueError(f"Duplicate card '{card}' found")
            seen_cards.add(key)

        max_deck_count = len(Card.RANKS) * len(Card.SUITS)
        # HACK avoid Getter recursion
        present_cards_count = len(getattr(self, "_cards", []))
        new_cards_count = len(value)
        if present_cards_count + new_cards_count > max_deck_count:
            raise ValueError(
                f"Not enough Hand of '{max_deck_count}' "
                f"to add '{new_cards_count}' more, "
                f"already '{present_cards_count}' are in"
            )

        self._cards = value

    def add_cards(self, new_cards: Card | list[Card]) -> None:
        if isinstance(new_cards, Card):
            new_cards = [new_cards]

        if not isinstance(new_cards, list):
            raise ValueError(
                f"Invalid card '{new_cards}' " f"of type '{type(new_cards).__name__}'"
            )

        # HACK This way to assign for Setter to be called and validate
        self.cards = self.cards + new_cards

    def play_card(self) -> Card:
        if self.cards:
            return self.cards.pop(0)
        else:
            raise ValueError("Cannot play a card from an empty hand")
