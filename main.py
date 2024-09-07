import random


def draw_move(board):
    # The function draws the computer's move and updates the board.
    valid_move = False

    while not valid_move:  # Loop until a valid move is made
        auto_move = random.randint(1, 9)  # Use 1-9 to match the board's range
        for row in board.values():  # Loop through the rows of the board
            if auto_move in row:  # Check if the move is valid
                row[row.index(auto_move)] = 'X'  # Replace the chosen move with 'X'
                valid_move = True
                break  # Exit the loop once a valid move is made


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    move = int(input("Enter your move: "))  # Get user input for the move
    valid_move = False

    for row in board.values():  # Loop through the values (rows) of the board
        if move in row:  # Check if the move is valid
            row[row.index(move)] = 'O'  # Replace the chosen move with 'O'
            valid_move = True
            break  # Exit the loop once the move is found and replaced

    if not valid_move:
        print("Invalid move. Please try again.")
        enter_move(board)  # Ask for the move again if invalid


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    for i in board:
        print("+---------+---------+---------+")
        for j in board[i]:
            print(f"|    {j}    ", end="")
        print("|")
    print("+---------+---------+---------+")


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, each tuple is a pair of row and column numbers.
    free_fields = []

    for row in board:
        for col_index, value in enumerate(board[row]):
            if value != 'O' and value != 'X':  # Check if the position is free
                free_fields.append((row, col_index + 1))  # Append row and column (1-indexed)

    return free_fields


def victory_for(board, sign):
    # The function analyzes the board's status to check if
    # the player using 'O's or 'X's has won the game.

    # Check rows for victory
    for row in board.values():
        if all(s == sign for s in row):
            return True

    # Check columns for victory
    for col_index in range(3):
        if all(board[row][col_index] == sign for row in board):
            return True

    # Check diagonals for victory
    if board[1][0] == board[2][1] == board[3][2] == sign:
        return True
    if board[1][2] == board[2][1] == board[3][0] == sign:
        return True

    return False


# Example of how the game might be played:
board = {
    1: [1, 2, 3],
    2: [4, 'X', 6],
    3: [7, 8, 9]
}

# Corrected loop condition
while not (victory_for(board, 'O') or victory_for(board, 'X')):
    display_board(board)
    enter_move(board)
    if victory_for(board, 'O'):
        break
    draw_move(board)
    if victory_for(board, 'X'):
        break

display_board(board)

# Victory checks after the loop:
if victory_for(board, 'O'):
    print("Congratulations, you won!")
elif victory_for(board, 'X'):
    print("Computer won!")
else:
    print("It's a tie!")
