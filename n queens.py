import random

def random_state(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def cost(state):
    attacks = 0
    n = len(state)
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_neighbors(state):
    n = len(state)
    neighbors = []
    for col in range(n):
        for row in range(n):
            if state[col] != row:
                neighbor = state.copy()
                neighbor[col] = row
                neighbors.append(neighbor)
    return neighbors

def hill_climb(n, max_restarts=50):
    for restart in range(max_restarts):
        current = random_state(n)
        current_cost = cost(current)
        while True:
            neighbors = get_neighbors(current)
            best = min(neighbors, key=cost)
            best_cost = cost(best)
            if best_cost >= current_cost:
                break
            current, current_cost = best, best_cost
        if current_cost == 0:
            return current, current_cost, restart
    return current, current_cost, max_restarts

def print_board(state):
    n = len(state)
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if state[col] == row else ". "
        print(line)
    print()

# ---- Main ----
n = int(input("Enter N: "))
solution, final_cost, restarts = hill_climb(n)
print("\nFinal Board:")
print_board(solution)
print("Final Cost:", final_cost)
print("Restarts Used:", restarts)
print("Solution Found!" if final_cost == 0 else "Local Optimum Reached (not valid solution).")
