#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there's a winner in the current board state.

    Parameters:
    board (list): 2D list representing the Tic Tac Toe board.

    Returns:
    bool: True if a player has won, otherwise False.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Check if the board is full (no empty spaces).

    Parameters:
    board (list): 2D list representing the Tic Tac Toe board.

    Returns:
    bool: True if the board is full, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play a two-player game of Tic Tac Toe.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"

    while True:
        print_board(board)
        try:
            row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
            col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))

            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue

            # Update the board
            board[row][col] = player

            # Check if the current move wins the game
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break

            # Check if the board is full (tie)
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break

            # Switch players
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except IndexError:
            print("Invalid input. Please enter numbers between 0 and 2.")

if __name__ == "__main__":
    tic_tac_toe()
