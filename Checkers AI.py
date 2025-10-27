import math
import copy

# ----- Board Initialization -----
def create_board():
    board = [[' ' for _ in range(8)] for _ in range(8)]
    for row in range(3):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = 'b'  # Black pieces
    for row in range(5, 8):
        for col in range(8):
            if (row + col) % 2 == 1:
                board[row][col] = 'r'  # Red pieces
    return board

# ----- Display Board -----
def print_board(board):
    print("\n   0 1 2 3 4 5 6 7")
    print("  -----------------")
    for i, row in enumerate(board):
        print(f"{i}| " + " ".join(row))
    print()

# ----- Get all possible moves for a player -----
def get_valid_moves(board, player):
    moves = []
    direction = -1 if player == 'r' else 1  # Red moves up, Black moves down

    for r in range(8):
        for c in range(8):
            if board[r][c] == player:
                # Normal moves
                for dc in [-1, 1]:
                    nr, nc = r + direction, c + dc
                    if 0 <= nr < 8 and 0 <= nc < 8 and board[nr][nc] == ' ':
                        moves.append(((r, c), (nr, nc)))

                # Capture moves
                for dc in [-1, 1]:
                    nr, nc = r + direction, c + dc
                    jump_r, jump_c = r + 2 * direction, c + 2 * dc
                    if (0 <= jump_r < 8 and 0 <= jump_c < 8 and
                        board[nr][nc] != ' ' and board[nr][nc] != player and
                        board[jump_r][jump_c] == ' '):
                        moves.append(((r, c), (jump_r, jump_c)))

    return moves

# ----- Apply a move -----
def make_move(board, move):
    new_board = copy.deepcopy(board)
    (r1, c1), (r2, c2) = move
    player = new_board[r1][c1]
    new_board[r1][c1] = ' '
    new_board[r2][c2] = player

    # Check for capture
    if abs(r1 - r2) == 2:
        new_board[(r1 + r2) // 2][(c1 + c2) // 2] = ' '

    return new_board

# ----- Evaluate board -----
def evaluate(board):
    red = sum(row.count('r') for row in board)
    black = sum(row.count('b') for row in board)
    return red - black  # positive if red is winning, negative if black

# ----- Minimax with Alpha–Beta Pruning -----
def minimax(board, depth, alpha, beta, maximizing, player):
    opponent = 'b' if player == 'r' else 'r'
    valid_moves = get_valid_moves(board, player if maximizing else opponent)

    if depth == 0 or not valid_moves:
        return evaluate(board), board

    if maximizing:
        max_eval = -math.inf
        best_move = None
        for move in valid_moves:
            new_board = make_move(board, move)
            eval, _ = minimax(new_board, depth - 1, alpha, beta, False, player)
            if eval > max_eval:
                max_eval = eval
                best_move = new_board
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval, best_move
    else:
        min_eval = math.inf
        best_move = None
        for move in valid_moves:
            new_board = make_move(board, move)
            eval, _ = minimax(new_board, depth - 1, alpha, beta, True, player)
            if eval < min_eval:
                min_eval = eval
                best_move = new_board
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval, best_move

# ----- Check for Winner -----
def check_winner(board):
    reds = sum(row.count('r') for row in board)
    blacks = sum(row.count('b') for row in board)
    if reds == 0:
        return "Black wins!"
    elif blacks == 0:
        return "Red wins!"
    return None

# ----- Main Game Loop -----
def play_game():
    board = create_board()
    print_board(board)
    turn = 'r'  # Red starts first (Human)

    while True:
        winner = check_winner(board)
        if winner:
            print(winner)
            break

        moves = get_valid_moves(board, turn)
        if not moves:
            print(f"No moves left for {turn}. Game over.")
            break

        if turn == 'r':
            print("Your turn (Red). Enter move as: row_from col_from row_to col_to")
            move_input = input("Move: ").split()
            if len(move_input) != 4:
                print("Invalid input. Try again.")
                continue
            r1, c1, r2, c2 = map(int, move_input)
            move = ((r1, c1), (r2, c2))
            if move not in moves:
                print("Illegal move. Try again.")
                continue
            board = make_move(board, move)
        else:
            print("AI (Black) is thinking...")
            _, board = minimax(board, 3, -math.inf, math.inf, True, 'b')

        print_board(board)
        turn = 'b' if turn == 'r' else 'r'

# ----- Start the Game -----
if __name__ == "__main__":
    play_game()
