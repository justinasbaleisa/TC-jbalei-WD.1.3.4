from models.card import Card
from models.player import Player

from managers.war import War

from utils.cli_prompts import clear_screen


class Round:

    def __init__(self, players: list[Player], rounds_count: int):
        self.players = players
        self.rounds_count = rounds_count

    def play_round(self) -> None:
        clear_screen()
        print(f"Simulating a single round of play No. {self.rounds_count}:")

        players_and_cards_on_table = self.play_round_cards()
        winners, cards = self.check_round(players_and_cards_on_table)
        if len(winners) == 1:
            winner = winners[0]
            print(f"\nPlayer '{winner.name}' wins the Round and the cards.")
            winner.hand.add_cards([card for card in cards])
        else:
            print(f"\nIt's a tie - WAR !!!")
            self.handle_war(winners, cards)
        
        # input("\nPress enter to continue (next round) or Ctrl+D to break")

    def play_round_cards(self) -> list[tuple[Player, Card]]:
        round_cards = []
        for player in self.players:
            card = player.hand.play_card()[0]
            print(f"  - player '{player.name}' ({len(player.hand.cards)}) {card}")
            round_cards.append((player, card))
        return round_cards

    def check_round(self, table: list[tuple[Player, Card]]) -> tuple[list[Player],list[Card]]:
        highest = max(table, key=lambda item: item[1].value)[1].value
        winners = []
        cards = []
        for player, card in table:
            if card.value == highest:
                winners.append(player)
            cards.append(card)
        return winners, cards

    def handle_war(self, winners: list[Player], cards: list[Card]) -> None:
        war = War(winners, cards, self.rounds_count)
        war.resolve()