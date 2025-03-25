from models.deck import Deck
from models.deck import Hand
from models.player import Player

from managers.round import Round

from utils.cli_prompts import input_player_name
from utils.cli_prompts import input_players_number

class Game:
    def __init__(self):
        players_quantity = self.get_number_of_players()
        players_names = self.get_players_names(players_quantity)
        self.deck = Deck()
        self.deck.shuffle()
        self.players = self.create_players_with_hands(players_quantity, players_names)

    def play_game(self) -> None:
        rounds_count = 0
        while not self.is_over():
            rounds_count += 1
            round = Round(self.players, rounds_count)
            round.play_round()
        self.declare_winner()

    def is_over(self):
        count = sum(1 for item in self.players if len(item.hand.cards) > 0)
        return count <= 1

    def get_number_of_players(self) -> int:
        return input_players_number("Enter number of players: ")

    def get_players_names(self, quantity: int) -> list[str]:
        players_names = []
        for i in range(1, quantity+1):
            name = input_player_name(f"Enter player No. {i} name: ")
            players_names.append(name)
        return players_names
    
    def create_players_with_hands(self, quantity: int, names: list) -> list[Player]:
        players = []
        for i in range(quantity):
            cards_quantity = int(self.deck.capacity / quantity)
            hand_cards = self.deck.deal(cards_quantity)
            hand = Hand(hand_cards)
            player = Player(names[i], hand)
            players.append(player)
        return players

    def declare_winner(self):
        player = next(player for player in self.players if len(player.hand.cards) > 0)
        print(f"\nPlayer '{player.name}' has won the game! Exiting.")