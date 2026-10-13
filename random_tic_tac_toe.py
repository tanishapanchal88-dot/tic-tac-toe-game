
import random

board = [" "] * 9

def display_board():
    print()
    for i in range(0, 9, 3):
        print(" | ".join(board[i:i + 3]))
        if i < 6:
            print("--+---+--")
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in winning_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

print("TIC-TAC-TOE")
print("You are X. Computer is O.")
print("Choose a cell number from 1 to 9.")
print("Cell positions:")
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

    available = [i for i in range(9) if board[i] == " "]
    computer_move = random.choice(available)
    board[computer_move] = "O"
    print("Computer chose cell", computer_move + 1)

    if check_winner("O"):
        display_board()
        print("Computer wins!")
        break

    if " " not in board:
        display_board()
        print("The game is a draw!")
        break
