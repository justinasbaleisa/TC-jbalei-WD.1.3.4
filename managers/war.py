from models.card import Card
from models.player import Player

from utils.cli_prompts import clear_screen


class War:

    def __init__(self, players: list[Player], cards: list[Card], round_count: int = 0) -> None:
        self.players = players
        self.cards = cards
        self.wars_count = 0
        self.round_count = round_count

    def resolve(self, cards: list[Card] = None):
        self.wars_count += 1
        clear_screen()
        if not cards:
            cards = self.cards
        print(
            f"Simulating round No. {self.round_count} war of play No. {self.wars_count}:\n"
            f"\n  PLAYERS:\n"
            + "".join(f"  - player '{player.name}' with '{len(player.hand.cards)}' cards on Hand left\n" for i, player in enumerate(self.players))
            + f"\n  CARDS ALREADY PLAYED:\n"
            + "".join(f"  - card No. {i+1}: {card}\n" for i, card in enumerate(cards))
        )
        players_without_enough_cards = []
        for player in self.players:
            if len(player.hand.cards) < 4:
                print(f"  Player '{player.name}' has not enough cards to play, hence lost, leaving the cards on the table:\n  - " + "\n  - ".join(f"card No. {i+1}: {card}" for i, card in enumerate(player.hand.cards)))
                self.cards.extend(player.hand.cards)
                player.hand.cards = []
                players_without_enough_cards.append(player)
        for player in players_without_enough_cards:
            self.players.remove(player)
        if len(self.players) == 1:
            print(f"\n  Player {self.players[0].name} has won cards on the table:\n"+ "\n".join(f"  - card No. {i+1}: {card}" for i, card in enumerate(self.cards)))
            self.players[0].hand.cards.extend(self.cards)
            return
        
        war_cards_on_table = self.play_war_cards()
        winners, new_cards = self.check_war(war_cards_on_table)
        cards.extend(new_cards)
        if len(winners) == 1:
            winner = winners[0]
            print("  WINNER:")
            print(
                f"\n  - player '{winner.name}' wins the War and all the cards:\n"
                + "".join(f"    - card No. {i+1}: {card}\n" for i, card in enumerate(cards))
            )
            winner.hand.add_cards([card for card in cards])
        else:
            print(f"\nIt's a tie AGAIN, repeat the WAR !!!")
            self.resolve(cards)

        # input("\nPress enter to continue (next round) or Ctrl+D to break")

    def play_war_cards(self) -> list[tuple[Player, list[Card]]]:
        print("  WAR PLAYED:")
        war_cards = []
        for player in self.players:
            cards = player.hand.play_card(4)
            print(f"  - player '{player.name}' with '{len(player.hand.cards)}' card on Hand left, plays:\n    - (folder) {'\n    - (folder) '.join(str(card) for card in cards[:-1])}\n    - (last) {str(cards[-1])}")
            war_cards.append((player, cards))
            print()
        return war_cards

    def check_war(self, table: list[tuple[Player, list[Card]]]) -> tuple[list[Player],list[Card]]:
        highest = max(cards[-1].value for _, cards in table)
        winners = []
        cards = []
        print(f"  The highest card in WAR is valued: {highest}")
        for player, card_list in table:
            if card_list[-1].value == highest:
                winners.append(player)
            cards.extend(card_list)
        return winners, cards