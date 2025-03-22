class War:
    """
    Handles the resolution of ties in the game.
    """

    def __init__(self, player1, player2, pot):
        """
        Initialize a War with two players and a pot of cards.

        Args:
            player1 (Player): The first player.
            player2 (Player): The second player.
            pot (list[Card]): The current set of cards at stake.
        """
        self.player1 = player1
        self.player2 = player2
        self.pot = pot

    def resolve(self):
        """
        Draw additional cards to resolve the tie.

        Each player adds extra cards. Compare final cards to determine
        a winner. If still tied, initiate recursive war.
        """
        pass

    def recursive_war(self):
        """
        Continue the War process in case of consecutive ties.
        """
        pass