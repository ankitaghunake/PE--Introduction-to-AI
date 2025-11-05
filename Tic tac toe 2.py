def evaluate(board):
    score = 0
    lines = []

    # Rows, Cols, Diags
    lines.extend(board)
    for c in range(3):
        lines.append([board[0][c], board[1][c], board[2][c]])
    lines.append([board[0][0], board[1][1], board[2][2]])
    lines.append([board[0][2], board[1][1], board[2][0]])

    for line in lines:
        if line.count('O') == 2 and line.count('_') == 1: score += 5
        if line.count('X') == 2 and line.count('_') == 1: score -= 5
    return score

def heuristic_move(board):
    best, move = -99, None
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = 'O'
                score = evaluate(board)
                board[i][j] = '_'
                if score > best:
                    best, move = score, (i, j)
    return move

# Example board
board = [['X','O','X'],
         ['_','O','_'],
         ['_','_','_']]

print("Before Move (Heuristic):")
for row in board: print(row)

i,j = heuristic_move(board)
board[i][j] = 'O'

print("\nAfter AI Move (Heuristic):")
for row in board: print(row)
