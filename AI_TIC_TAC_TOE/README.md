# Tic-Tac-Toe AI

This project is a simple implementation of the classic game Tic-Tac-Toe with an AI opponent that uses the Minimax algorithm. The AI player is designed to be unbeatable, making it a challenging opponent for human players.

## Table of Contents

- [Getting Started](#getting_started)
- [How to Play](#how_to_play)
- [Implementation Details](#implementation_details)
- [Contributing](#contributing)

## Getting Started

To get started with the Tic-Tac-Toe AI, follow these steps:

1- Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/tic-tac-toe-ai.git
```
2- Navigate to the project directory:

```bash
cd tic-tac-toe-ai
```
3- Run the Python script:

```bash
python tic_tac_toe.py
```
This will start the game, allowing you to play against the AI.

## How to Play
- The game is played on a 3x3 grid.
- You are 'O', and the AI is 'X'.
- To make your move, enter the row and column numbers separated by a space, e.g., 0 1.
- The AI player uses the Minimax algorithm to determine its moves.
- The game ends when one player wins, or it's a draw (tie).


## Implementation Details
- The AI player uses the Minimax algorithm to find the best move.
- The evaluate_board function assigns scores to board positions, with 'X' winning positions having a score of 10, 'O' winning positions having a score of -10, and draws having a score of 0.
- The AI explores all possible moves and selects the one with the highest score (for 'X') or the lowest score (for 'O').
- The game checks for a win or a draw after each move to determine the game's outcome.

## Contributing
Contributions to this project are welcome. If you have ideas for improvements, bug fixes, or new features, please open an issue or submit a pull request. For major changes, please discuss them in the issue before implementing.