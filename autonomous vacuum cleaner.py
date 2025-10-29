
import random

grid = [[random.choice(['Clean','Dirty']) for _ in range(3)] for _ in range(3)]

def show():
    for r in grid: print(r)
    print()

def clean():
    moves = 0
    for i in range(3):
        for j in range(3):
            moves += 1
            if grid[i][j] == 'Dirty':
                grid[i][j] = 'Clean'
                print(f"Cleaned cell ({i},{j})")
    return moves

print("Initial Grid:")
show()
m = clean()
print("Final Grid:")
show()
print("Total Moves:", m)
