import math

# Initialize the board
def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check if there are moves left
def is_moves_left(board):
    return any(" " in row for row in board)

# Check the winner
def evaluate(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return 10 if board[i][0] == "X" else -10
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != " ":
            return 10 if board[0][i] == "X" else -10

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return 10 if board[0][0] == "X" else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return 10 if board[0][2] == "X" else -10

    return 0

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    # Terminal states
    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if not is_moves_left(board):
        return 0

    if is_max:  # Maximizer's move (AI - X)
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = " "
                    alpha = max(alpha, best)
                    if beta <= alpha:
                        break
        return best
    else:  # Minimizer's move (Human - O)
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = " "
                    beta = min(beta, best)
                    if beta <= alpha:
                        break
        return best

# Find the best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = " "
                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val
    return best_move

# Main game loop
def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O'. AI is 'X'.")
    print_board(board)

    while True:
        if not is_moves_left(board):
            print("It's a draw!")
            break

        # Human move
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] != " ":
            print("Invalid move. Try again.")
            continue
        board[row][col] = "O"
        print_board(board)

        if evaluate(board) == -10:
            print("Congratulations! You win!")
            break

        if not is_moves_left(board):
            print("It's a draw!")
            break

        # AI move
        print("AI is making its move...")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = "X"
        print_board(board)

        if evaluate(board) == 10:
            print("AI wins! Better luck next time.")
            break

play_game()