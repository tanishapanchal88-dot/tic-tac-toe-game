
# Tic-Tac-Toe Game: Algorithm

## 1. Problem Statement

Design a Tic-Tac-Toe game played between a human user and a computer on a 3 x 3 board. The game has two versions: random move strategy and intelligent move strategy.

## 2. Inputs

- The user enters a cell number from 1 to 9.
- The computer selects an available cell automatically.

## 3. Outputs

- The current game board.
- Messages for invalid moves.
- The winner or a draw message.

## 4. Rules

1. The human plays as X.
2. The computer plays as O.
3. Players take alternate turns.
4. A player wins by marking three cells in a row, column, or diagonal.
5. An occupied cell cannot be selected.
6. If all nine cells are filled without a winner, the game is a draw.

## 5. Algorithm: Random Move Strategy

1. Start the game.
2. Create an empty 3 x 3 board.
3. Display the board and ask the user to enter a cell number.
4. Validate the input.
5. If the input is invalid or the cell is occupied, ask again.
6. Place X in the selected cell.
7. Check whether the user has won. If yes, end the game.
8. Check whether the board is full. If yes, declare a draw.
9. Select a random available cell for the computer.
10. Place O in that cell.
11. Check whether the computer has won. If yes, end the game.
12. Check whether the board is full. If yes, declare a draw.
13. Repeat until the game ends.

## 6. Algorithm: Intelligent Move Strategy

1. Start the game with an empty board.
2. Display the board and accept the user's move.
3. Validate the input and reject invalid or occupied cells.
4. Place X in the selected cell.
5. Check whether the user has won or the game is a draw.
6. Check whether the computer can win in its next move. If possible, take that move.
7. Otherwise, check whether the user can win in the next move. If possible, block it.
8. Otherwise, choose the centre if available.
9. Otherwise, choose an available corner.
10. If no corner is available, select another empty cell randomly.
11. Place O and check for a computer win or draw.
12. Repeat until the game ends.

## 7. Flow of the Game

Start -> Initialize Board -> User Move -> Validate Input -> Check Result -> Computer Move -> Check Result -> Repeat or End
