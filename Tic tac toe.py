def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] != '_':
            return row[0]
    # Cols
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != '_':
            return board[0][c]
    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != '_':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '_':
        return board[0][2]
    return None

def is_full(board):
    return all(cell != '_' for row in board for cell in row)

def minimax(board, is_max):
    winner = check_winner(board)
    if winner == 'X': return -1
    if winner == 'O': return 1
    if is_full(board): return 0

    if is_max:  # O's turn
        best = -2
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                    best = max(best, minimax(board, False))
                    board[i][j] = '_'
        return best
    else:  # X's turn
        best = 2
        for i in range(3):
            for j in range(3):
                if board[i][j] == '_':
                    board[i][j] = 'X'
                    best = min(best, minimax(board, True))
                    board[i][j] = '_'
        return best

def best_move(board):
    move = None
    best = -2
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'O'
                score = minimax(board, False)
                board[i][j] = '_'
                if score > best:
                    best, move = score, (i, j)
    return move

# Example board
board = [['X','O','X'],
         ['_','O','_'],
         ['_','_','_']]

print("Before Move (Minimax):")
for row in board: print(row)

i,j = best_move(board)
board[i][j] = 'O'

print("\nAfter AI Move (Minimax):")
for row in board: print(row)
