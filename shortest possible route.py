from itertools import permutations

# Define cities and distances between each pair (symmetric matrix)
cities = ['A', 'B', 'C', 'D']
distances = {
    ('A', 'B'): 10, ('A', 'C'): 15, ('A', 'D'): 20,
    ('B', 'A'): 10, ('B', 'C'): 35, ('B', 'D'): 25,
    ('C', 'A'): 15, ('C', 'B'): 35, ('C', 'D'): 30,
    ('D', 'A'): 20, ('D', 'B'): 25, ('D', 'C'): 30
}

def total_distance(route):
    total = 0
    for i in range(len(route) - 1):
        total += distances[(route[i], route[i + 1])]
    total += distances[(route[-1], route[0])]  # return to start
    return total

def traveling_salesman(cities):
    shortest_path = None
    min_cost = float('inf')
    for perm in permutations(cities):
        cost = total_distance(perm)
        if cost < min_cost:
            min_cost = cost
            shortest_path = perm
    return shortest_path, min_cost

# ---- Run TSP ----
path, cost = traveling_salesman(cities)

print("Cities:", cities)
print("Shortest Path:", " → ".join(path) + f" → {path[0]}")
print("Total Distance:", cost)
