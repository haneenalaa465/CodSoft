import random

# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if the game is over
def is_game_over(board):
    # Check rows, columns, and diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    # Check if the board is full (draw)
    for row in board:
        if ' ' in row:
            return False
    return True

# Function to evaluate the current state of the board
def evaluate_board(board):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return 10
            elif board[i][0] == 'O':
                return -10
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return 10
            elif board[0][i] == 'O':
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 10
        elif board[0][0] == 'O':
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 10
        elif board[0][2] == 'O':
            return -10
    return 0

# Minimax algorithm
def minimax(board, depth, is_maximizer):
    score = evaluate_board(board)

    if score == 10:
        return score - depth
    if score == -10:
        return score + depth
    if is_game_over(board):
        return 0

    if is_maximizer:
        best = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_maximizer))
                    board[i][j] = ' '
        return best
    else:
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_maximizer))
                    board[i][j] = ' '
        return best

# Function to find the best move for the AI using the Minimax algorithm
def find_best_move(board):
    best_move = (-1, -1)
    best_score = -float('inf')

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                score = minimax(board, 0, False)
                board[i][j] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move

# Main game loop
def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player_turn = True  # True for player, False for AI

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while not is_game_over(board):
        if player_turn:
            row, col = map(int, input("Enter your move (row and column): ").split())
            if board[row][col] == ' ':
                board[row][col] = 'O'
                player_turn = False
            else:
                print("Invalid move. Try again.")
        else:
            print("AI is thinking...")
            ai_move = find_best_move(board)
            board[ai_move[0]][ai_move[1]] = 'X'
            player_turn = True

        print_board(board)

    score = evaluate_board(board)
    if score == 10:
        print("AI wins!")
    elif score == -10:
        print("You win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()
