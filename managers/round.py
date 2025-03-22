class Round:
    """
    Simulates a single round of the War card game.
    """

    def __init__(self, player1, player2):
        """
        Initialize a round with two players.

        Args:
            player1 (Player): The first player.
            player2 (Player): The second player.
        """
        self.player1 = player1
        self.player2 = player2

    def play(self):
        """
        Simulate one round of play.

        Each player plays a card. Compare card values to determine
        a winner. If tied, initiate a War.
        """
        pass

    def handle_war(self):
        """
        Invoke War resolution if the played cards are tied.
        """
        pass
