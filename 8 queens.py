N = 8

def print_board(b):
    for row in b:
        print(" ".join("Q" if x else "." for x in row))
    print()

def safe(b, r, c):
    for i in range(c):
        if b[r][i]: return False
    for i,j in zip(range(r,-1,-1), range(c,-1,-1)):
        if b[i][j]: return False
    for i,j in zip(range(r,N), range(c,-1,-1)):
        if b[i][j]: return False
    return True

def solve(b, c):
    if c>=N: print_board(b); return True
    for r in range(N):
        if safe(b,r,c):
            b[r][c]=1
            if solve(b,c+1): return True
            b[r][c]=0
    return False

solve([[0]*N for _ in range(N)],0)


