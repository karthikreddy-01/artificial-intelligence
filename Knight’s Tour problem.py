# Knight's Tour Problem using Backtracking

N = 8  # You can change N for different board sizes

# All possible moves of a knight
moves_x = [2, 1, -1, -2, -2, -1, 1, 2]
moves_y = [1, 2, 2, 1, -1, -2, -2, -1]

def print_board(board):
    for row in board:
        print(' '.join(str(cell).rjust(2, '0') for cell in row))
    print()

def is_safe(x, y, board):
    return 0 <= x < N and 0 <= y < N and board[x][y] == -1

def solve_knight_tour():
    board = [[-1 for _ in range(N)] for _ in range(N)]
    board[0][0] = 0  # starting position

    if not solve(0, 0, 1, board):
        print("No solution exists.")
    else:
        print("Knight's Tour Path:")
        print_board(board)

def solve(x, y, move_i, board):
    if move_i == N * N:
        return True

    for k in range(8):
        next_x = x + moves_x[k]
        next_y = y + moves_y[k]
        if is_safe(next_x, next_y, board):
            board[next_x][next_y] = move_i
            if solve(next_x, next_y, move_i + 1, board):
                return True
            # Backtrack
            board[next_x][next_y] = -1
    return False

# Run the program
solve_knight_tour()
