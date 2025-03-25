import os
import platform

from models.card import Card

def input_player_name(prompt: str) -> str:
    while True:
        clear_screen()
        try:
            respond = input(prompt).strip().capitalize()
            if respond:
                return respond
        except EOFError:
            input("\n\nExiting. Press enter to continue...")
            raise EOFError
        
        input("\n\nPress enter to continue...")


def input_players_number(prompt: str) -> str:
    while True:
        clear_screen()
        try:
            respond = int(input(prompt).strip())
            if respond > 1:
                if (len(Card.RANKS) * len(Card.SUITS)) % respond == 0:
                    return respond
                else:
                    print("Number of cards does not split.")
            else:
                print("Must be positive integer higher than 1.")
        except ValueError:
            print("Must be integer.")
        except EOFError:
            input("\n\nExiting. Press enter to continue...")
            raise EOFError
        
        input("\n\nPress enter to continue...")


def clear_screen() -> None:
    if platform.system().lower() == "windows":
        os.system("cls")
    else:
        os.system("clear")