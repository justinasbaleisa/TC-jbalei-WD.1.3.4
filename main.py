from managers.game import Game
from utils.logger import Logger


def main() -> None:
    game = Game()
    logger = Logger()

    while not game.is_game_over():
        logger.log("WarGame: starting round")
        game.play_round()
        logger.log("WarGame: round completed")

    game.declare_winner()
    logger.log("WarGame: declared winner")
    logger.save_to_file()


if __name__ == "__main__":
    main()
