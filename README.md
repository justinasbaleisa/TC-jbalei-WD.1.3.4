# TC 1.3.3 Peer programming exercise: War card game

## Description

This Python project simulates the children's card game called [War](https://en.wikipedia.org/wiki/War_(card_game)). The game is built using Object-Oriented Programming (OOP) principles.

## Features

- **Object-Oriented Design:** Utilizes classes to structure the game components (Card, Deck, Player, Hand, Round, War, Game, GameLogger, WarGame).

## Requirements

- Python 3.x

## Installation

Clone the repository:

```sh
git clone https://github.com/username/war.git
```

Navigate to the project directory:

```sh
cd war
```

## Usage

To run the War card game:

```sh
python war.py
```

## Testing

To test the implemented classes and methods:

```sh
pytest test_war.py
```

## Notes

Task description: [https://intra.turingcollege.com/hardskills/wd-1-3-4](https://intra.turingcollege.com/hardskills/wd-1-3-4)


## Architecture (Classes and Methods)



### Card Class
- **Attributes:**
  - `rank` (str): The rank of the card (e.g., "Ace", "2", "King").
  - `suit` (str): The suit of the card (e.g., "Hearts", "Diamonds").
  - `value` (int): The numerical value of the card for comparison.
  - `ascii_suit` (str): The ASCII representation of the suit.
- **Methods:**
  - `__init__(self, rank, suit)`
  - `__str__(self)`
  - `__eq__(self, other)`
  - `__lt__(self, other)`

### Deck Class
- **Attributes:**
  - `cards` (list): List of Card objects.
- **Methods:**
  - `__init__(self)`
  - `shuffle(self)`
  - `deal(self)`
  - `__str__(self)`

### Hand Class
- **Attributes:**
  - `cards` (list): List of Card objects representing a player's hand.
- **Methods:**
  - `__init__(self, cards)`
  - `add_cards(self, new_cards)`
  - `play_card(self)`
  - `has_cards(self)`

### Player Class
- **Attributes:**
  - `name` (str): The player's name.
  - `hand` (Hand): The player's current hand of cards.
- **Methods:**
  - `__init__(self, name, hand)`
  - `play_card(self)`
  - `add_cards(self, new_cards)`
  - `has_cards(self)`
  - `__str__(self)`

### Round Class
- **Attributes:**
  - `player1` (Player): The first player.
  - `player2` (Player): The second player.
  - `pot` (list): The list of cards at stake in this round.
- **Methods:**
  - `__init__(self, player1, player2)`
  - `play(self)`
  - `handle_war(self)`

### War Class
- **Attributes:**
  - `player1` (Player): The first player.
  - `player2` (Player): The second player.
  - `pot` (list): The current set of cards at stake.
- **Methods:**
  - `__init__(self, player1, player2, pot)`
  - `resolve(self)`
  - `recursive_war(self)`

### GameLogger Class
- **Attributes:**
  - `logs` (list): List storing log messages.
- **Methods:**
  - `__init__(self)`
  - `log(self, message)`
  - `save_to_file(self)`

### Game Class
- **Attributes:**
  - `deck` (Deck): The deck used in the game.
  - `player1` (Player): The first player.
  - `player2` (Player): The second player.
  - `logger` (GameLogger): The logging system.
- **Methods:**
  - `__init__(self)`
  - `play_round(self)`
  - `is_game_over(self)`
  - `declare_winner(self)`

### WarGame Class
- **Attributes:**
  - `game` (Game): The main game instance.
  - `logger` (GameLogger): The logging system.
- **Methods:**
  - `__init__(self)`
  - `play_game(self)`

### Main Function
- **Method:**
  - `main()`: Entry point of the game.

## GitHub Issues (development process)

1. **Initialize Repository and Project Setup**
   - Create initial repository structure.
   - Add a `README.md` file with project description and requirements.
2. **Create Card Class**
   - Define the `Card` class with attributes: rank, suit, value, and ascii_suit.
   - Implement `__init__`, `__str__`, and comparison methods (`__eq__`, `__lt__`).
3. **Create Deck Class**
   - Define the `Deck` class to manage a collection of Card objects.
   - Implement `__init__`, `shuffle`, and `__str__` methods.
4. **Implement Deal Method in Deck Class**
   - Implement the `deal` method to distribute cards evenly between two players.
5. **Create Hand Class**
   - Define the `Hand` class to manage a player's collection of cards.
   - Implement methods `__init__`, `add_cards`, `play_card`, and `has_cards`.
6. **Create Player Class**
   - Define the `Player` class to represent a player in the game.
   - Implement methods `__init__`, `play_card`, `add_cards`, `has_cards`, and `__str__`.
7. **Create Round Class**
   - Define the `Round` class to simulate a single round of the game.
   - Implement methods `__init__`, `play`, and `handle_war`.
8. **Create War Class**
   - Define the `War` class to handle tie situations.
   - Implement methods `__init__`, `resolve`, and `recursive_war`.
9. **Create GameLogger Class**
   - Define the `GameLogger` class for logging game events.
   - Implement methods `__init__`, `log`, and `save_to_file`.
10. **Create Game Class**
    - Define the `Game` class to manage game flow, rounds, and victory conditions.
    - Implement methods `__init__`, `play_round`, `is_game_over`, and `declare_winner`.
11. **Create WarGame Class**
    - Define the `WarGame` class to control game execution.
    - Implement methods `__init__` and `play_game`.
12. **Implement Main Function**
    - Implement `main()` function as the entry point of the game.
13. **Write Test Cases**
    - Write test cases for each class and method.
    - Ensure the game runs without errors and behaves as expected.
14. **Final Code Review**
    - Review code for adherence to PEP 8 standards.
    - Update documentation if necessary.