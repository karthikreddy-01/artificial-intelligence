import random

board = [' '] * 9

def print_board():
    for i in range(0, 9, 3):
        print(board[i], '|', board[i+1], '|', board[i+2])
    print()

def check_winner(b, p):
    win = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(b[a]==b[b1]==b[c]==p for a,b1,c in win)

def ai_move():
    empty = [i for i in range(9) if board[i] == ' ']
    return random.choice(empty)

def play():
    print("Tic Tac Toe! You are X, AI is O")
    for turn in range(9):
        print_board()
        if turn % 2 == 0:
            move = int(input("Enter position (0-8): "))
            if board[move] != ' ': continue
            board[move] = 'X'
            if check_winner(board, 'X'):
                print_board(); print("You win!"); return
        else:
            move = ai_move()
            board[move] = 'O'
            if check_winner(board, 'O'):
                print_board(); print("AI wins!"); return
    print_board()
    print("It's a draw!")

play()
