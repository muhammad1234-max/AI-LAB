import copy

EMPTY, WHITE, BLACK = '.', 'W', 'B'

def init_board():
    return [
        ['.', 'B', '.', 'B'],
        ['B', '.', 'B', '.'],
        ['.', 'W', '.', 'W'],
        ['W', '.', 'W', '.']
    ]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def get_all_moves(board, player):
    direction = -1 if player == WHITE else 1
    opponent = BLACK if player == WHITE else WHITE
    moves = []
    for r in range(4):
        for c in range(4):
            if board[r][c] == player:
                for dc in [-1, 1]:
                    nr, nc = r + direction, c + dc
                    if 0 <= nr < 4 and 0 <= nc < 4 and board[nr][nc] == EMPTY:
                        new_board = copy.deepcopy(board)
                        new_board[nr][nc] = player
                        new_board[r][c] = EMPTY
                        moves.append(new_board)
                    # capture
                    nr2, nc2 = r + direction*2, c + dc*2
                    if 0 <= nr2 < 4 and 0 <= nc2 < 4 and board[nr+direction][c+dc] == opponent and board[nr2][nc2] == EMPTY:
                        new_board = copy.deepcopy(board)
                        new_board[nr2][nc2] = player
                        new_board[r][c] = EMPTY
                        new_board[nr+direction][c+dc] = EMPTY
                        moves.append(new_board)
    return moves

def evaluate(board):
    score = sum(row.count(BLACK) - row.count(WHITE) for row in board)
    return score

def alpha_beta(board, depth, alpha, beta, maximizing):
    if depth == 0:
        return evaluate(board), board
    player = BLACK if maximizing else WHITE
    moves = get_all_moves(board, player)
    if not moves:
        return evaluate(board), board
    best = None
    if maximizing:
        max_eval = float('-inf')
        for move in moves:
            eval, _ = alpha_beta(move, depth-1, alpha, beta, False)
            if eval > max_eval:
                max_eval = eval
                best = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best
    else:
        min_eval = float('inf')
        for move in moves:
            eval, _ = alpha_beta(move, depth-1, alpha, beta, True)
            if eval < min_eval:
                min_eval = eval
                best = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best

def play_game():
    board = init_board()
    while True:
        print_board(board)
        move = input("Enter move (e.g., 2 1 1 2): ").split()
        if len(move) != 4:
            print("Invalid format.")
            continue
        r1, c1, r2, c2 = map(int, move)
        if board[r1][c1] != WHITE or board[r2][c2] != EMPTY:
            print("Invalid move.")
            continue
        board[r1][c1] = EMPTY
        board[r2][c2] = WHITE
        _, board = alpha_beta(board, 3, float('-inf'), float('inf'), True)
        if not get_all_moves(board, WHITE) or not get_all_moves(board, BLACK):
            break

    print("Game Over!")
    print_board(board)

play_game() 
