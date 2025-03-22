# File where game logs will be stored
LOG_FILE_NAME = "game_log.txt"


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


class Hand:

    def __init__(self, cards):
        """
        Args:
            cards (list[Card]): A list of Card objects representing the hand.
        """
        self.cards = cards

    def add_cards(self, new_cards):
        """
        Add one or more cards to the bottom of the hand.

        Args:
            new_cards (list[Card] or Card): The new cards to be added.
        """
        pass

    def play_card(self):
        """
        Remove and return the top card from the hand.
        """
        pass

    def has_cards(self):
        """
        Return True if the hand has remaining cards, otherwise False.
        """
        pass


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


class GameLogger:
    """
    Logs important game events and saves them for debugging.
    """

    def __init__(self):
        """
        Initialize the logger with an empty log list.
        """
        self.logs = []

    def log(self, message):
        """
        Append a message to the log and print it.

        Args:
            message (str): The message to be logged.
        """
        pass

    def save_to_file(self):
        """
        Write all log messages to the specified log file.
        """
        pass


class Game:
    """
    Manages game flow, rounds, and victory conditions.
    """

    def __init__(self):
        """
        Initialize the game by setting up players and dealing cards.
        """
        pass

    def play_round(self):
        """
        Simulate a single round of play.
        """
        pass

    def is_game_over(self):
        """
        Check if the game is over based on player hands.
        """
        pass

    def declare_winner(self):
        """
        Determine and log the winner based on remaining cards.
        """
        pass


class WarGame:

    def __init__(self):
        self.game = Game()
        self.logger = GameLogger()

    def play_game(self):
        while not self.game.is_game_over():
            self.logger.log("WarGame: starting round")
            self.game.play_round()
            self.logger.log("WarGame: round completed")

        self.game.declare_winner()
        self.logger.log("WarGame: declared winner")
        self.logger.save_to_file(LOG_FILE_NAME)


def main():
    deck = Deck()
    deck.shuffle()
    print(deck)
    '''
    war_game = WarGame()
    war_game.play_game()
    '''

if __name__ == "__main__":
    main()
