
# Missionaries and Cannibals Problem using BFS

from collections import deque

# Each state is represented as (M_left, C_left, Boat_side)
# Boat_side = 1 (left), 0 (right)

def is_valid(state):
    M_left, C_left, boat = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    # Conditions for invalid states
    if (M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0):
        return False
    if (M_left > 0 and M_left < C_left):
        return False
    if (M_right > 0 and M_right < C_right):
        return False
    return True

def get_successors(state):
    M_left, C_left, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    successors = []
    
    for m, c in moves:
        if boat == 1:  # boat on left side
            new_state = (M_left - m, C_left - c, 0)
        else:  # boat on right side
            new_state = (M_left + m, C_left + c, 1)
        if is_valid(new_state):
            successors.append(new_state)
    return successors

def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for next_state in get_successors(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
    return None

# Run BFS
solution = bfs()

# Print Result
if solution:
    print("Solution Path (M_left, C_left, Boat_side):")
    for step in solution:
        print(step)
else:
    print("No solution found.")
