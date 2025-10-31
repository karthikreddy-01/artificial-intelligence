# Map Coloring using Backtracking

def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def map_coloring(graph, colors, assignment={}, node=0):
    # If all nodes are colored, return solution
    if node == len(graph):
        return assignment

    for color in colors:
        if is_safe(node, color, assignment, graph):
            assignment[node] = color
            result = map_coloring(graph, colors, assignment, node + 1)
            if result:
                return result
            assignment.pop(node)  # backtrack
    return None

# ---- Example Graph ----
# Adjacency list (Map)
graph = {
    0: [1, 2],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [1, 2]
}

# Available colors
colors = ["Red", "Green", "Blue"]

solution = map_coloring(graph, colors)

print("Map Coloring Solution:")
if solution:
    for region, color in solution.items():
        print(f"Region {region} → {color}")
else:
    print("No valid coloring found.")
