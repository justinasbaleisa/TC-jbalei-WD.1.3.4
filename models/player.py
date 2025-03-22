class Player:
    """
    Represents a player in the game.
    """

    def __init__(self, name, hand):
        """
        Initialize a player with a name and a hand of cards.

        Args:
            name (str): The player's name.
            hand (Hand): The player's initial collection of cards.
        """
        self.name = name
        self.hand = hand

    def play_card(self):
        """
        Draw and play the top card from the player's hand.
        """
        pass

    def add_cards(self, new_cards):
        """
        Add won cards to the player's hand.

        Args:
            new_cards (list[Card]): The new cards to be added.
        """
        pass

    def has_cards(self):
        """
        Check if the player still has cards left to play.
        """
        pass

    def __str__(self):
        """
        Return the player's name.
        """
        pass
