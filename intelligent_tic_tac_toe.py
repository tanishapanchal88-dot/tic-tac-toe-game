
import random

board = [" "] * 9

WINNING_POSITIONS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

def display_board():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")
    print()

def check_winner(player):
    for a, b, c in WINNING_POSITIONS:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def find_winning_move(player):
    for a, b, c in WINNING_POSITIONS:
        cells = [a, b, c]
        values = [board[i] for i in cells]

        if values.count(player) == 2 and values.count(" ") == 1:
            return cells[values.index(" ")]

    return None

def computer_move():
    # Win if possible
    move = find_winning_move("O")
    if move is not None:
        return move

    # Block the user's winning move
    move = find_winning_move("X")
    if move is not None:
        return move

    # Take the centre if available
    if board[4] == " ":
        return 4

    # Prefer a corner
    corners = [i for i in [0, 2, 6, 8] if board[i] == " "]
    if corners:
        return random.choice(corners)

    # Otherwise, choose any available cell
    available = [i for i in range(9) if board[i] == " "]
    return random.choice(available)

print("INTELLIGENT TIC-TAC-TOE")
print("You are X. Computer is O.")
print("Enter a cell number from 1 to 9.")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    display_board()

    try:
        move = int(input("Enter your move (1-9): ")) - 1
    except ValueError:
        print("Invalid input. Enter a number from 1 to 9.")
        continue

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid or occupied cell. Try again.")
        continue

    board[move] = "X"

    if check_winner("X"):
        display_board()
        print("Congratulations! You win!")
        break

    if " " not in board:
        display_board()
        print("The game is a draw!")
        break

    move = computer_move()
    board[move] = "O"
    print("Computer chose cell", move + 1)

    if check_winner("O"):
        display_board()
        print("Computer wins!")
        break

    if " " not in board:
        display_board()
        print("The game is a draw!")
        break
