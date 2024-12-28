# 2048 - Terminal Edition

A minimalist terminal-based version of the popular game 2048. The game is played in the terminal using the arrow keys, with colorful output for a clean and dynamic experience.

## Features
- Fully functional 2048 game.
- Uses `blessed` for terminal UI.
- Supports smooth navigation with arrow keys.
- Displays score and game-over status.
- Easy-to-read and extendable Python code.

## Requirements
- Python 3.7+
- `blessed` library

To install the required dependencies, run:
```bash
pip install blessed
```

## How to Play
1. Clone this repository or download the game files.
2. Ensure all required modules are installed.
3. Run the game:
   ```bash
   python main.py
   ```
4. Use the following keys to play:
   - **Arrow keys:** Move tiles in the corresponding direction.
   - **Q:** Quit the game.

## Folder Structure
```
project-root/
├── main.py   # Entry point of the game
├── game.py   # Game logic (handling board, tiles, and rules)
├── ui.py     # Terminal-based UI using blessed
└── README.md # Game documentation
```

## Code Overview

### `game.py`
Handles the core logic of the 2048 game:
- Initializes the game board.
- Implements tile movements (left, right, up, down).
- Merges tiles and spawns new tiles after valid moves.
- Checks for game-over condition.

### `ui.py`
Manages the terminal UI:
- Displays the game board in a clean and colorful layout.
- Captures user input for gameplay.

### `main.py`
The main entry point:
- Links game logic with UI.
- Contains the game loop, listening for player actions and updating the game state.

## Example Gameplay
After starting the game, you will see a terminal output like this:

```
2048 - Terminal Edition

Score: 0

    2     0     0     0
    0     0     0     0
    0     2     0     0
    0     0     0     0

Use arrow keys to play. Press 'q' to quit.
```

### Example: After a few moves
```
2048 - Terminal Edition

Score: 12

    4     0     0     0
    4     0     0     0
    2     0     0     0
    0     0     0     0
```

## Game Over
If no moves are possible:
```
Game Over!
Your final score: 128
Press 'q' to quit.
```

## Extending the Game
Feel free to contribute or extend the game! Ideas for enhancements include:
- Adding a scoring leaderboard.
- Customizing grid size (e.g., 5x5).
- Adding animations for movements and merges.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

Enjoy playing 2048 in your terminal!
