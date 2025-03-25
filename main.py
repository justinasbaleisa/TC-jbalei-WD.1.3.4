import sys

from managers.game import Game


def main() -> None:
    try:
        game = Game()
        game.play_game()

    except EOFError:
        print(f"\nFINISHED.")
        if input("Do you want to restart? (y/n): ").lower() == "y":
            main()
        else:
            sys.exit(0)
        
    except Exception as e:
        print(f"WarGame error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
