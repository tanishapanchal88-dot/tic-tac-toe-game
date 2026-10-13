
# Tic-Tac-Toe Game Using Python

## Problem Statement
Design and implement a Tic-Tac-Toe game between a human player and a computer on a 3 x 3 board. The project contains two versions: a random move strategy and an intelligent move strategy.

## Inputs
- The human player enters a cell number from 1 to 9.
- The computer selects an available cell automatically.

## Outputs
- The updated game board after each move.
- Messages for invalid moves.
- The final result: human wins, computer wins, or draw.

## Game Rules
1. The human plays as X and the computer plays as O.
2. Players take turns.
3. Three matching symbols in a row, column, or diagonal result in a win.
4. A move in an occupied cell is not allowed.
5. If all cells are filled without a winner, the game ends in a draw.

## Versions

### 1. Random Move Strategy
The computer randomly selects one of the available cells.

File: `random_tic_tac_toe.py`

### 2. Intelligent Move Strategy
The computer attempts to win, blocks the user's winning move, prefers the centre and corners, and otherwise selects an available cell.

File: `intelligent_tic_tac_toe.py`

## Algorithm
The algorithms for both versions are provided in `algorithm.md`.

## Requirements
- Python 3

## How to Run
Open a terminal in the project folder and run:

For the random version:
`python random_tic_tac_toe.py`

For the intelligent version:
`python intelligent_tic_tac_toe.py`

## Author
Tanisha Panchal

