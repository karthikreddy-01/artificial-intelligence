import heapq

# Define the goal state
GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  # 0 represents the empty space

# Function to find the position of the blank tile (0)
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                target_x = (val - 1) // 3
                target_y = (val - 1) % 3
                distance += abs(target_x - i) + abs(target_y - j)
    return distance

# Function to generate possible next states
def get_neighbors(state):
    x, y = find_blank(state)
    moves = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    neighbors = []

    for nx, ny in moves:
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Function to convert state to tuple (for hashing)
def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

# A* search algorithm
def solve_puzzle(start):
    open_set = []
    heapq.heappush(open_set, (manhattan_distance(start), 0, start, []))
    visited = set()

    while open_set:
        _, cost, current, path = heapq.heappop(open_set)
        if current == GOAL_STATE:
            return path + [current]

        visited.add(state_to_tuple(current))

        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                heapq.heappush(open_set, (cost + 1 + manhattan_distance(neighbor),
                                          cost + 1,
                                          neighbor,
                                          path + [current]))
    return None

# Example usage
if __name__ == "__main__":
    start_state = [[1, 2, 3],
                   [4, 0, 6],
                   [7, 5, 8]]  # Example scrambled puzzle

    print("Initial State:")
    for row in start_state:
        print(row)

    solution = solve_puzzle(start_state)

    if solution:
        print("\nSteps to reach goal:")
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            for row in state:
                print(row)
            print()
    else:
        print("No solution found.")
