import heapq

# Define the graph (adjacency list with weights)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'D': 3, 'E': 5},
    'C': {'F': 2},
    'D': {'F': 1, 'E': 1},
    'E': {'F': 2},
    'F': {}
}

# Heuristic values (straight-line or estimated distance to goal)
heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 3,
    'F': 0
}

def astar(start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], 0, start, [start]))  # (f, g, node, path)
    visited = set()
    order_of_expansion = []

    while open_list:
        f, g, node, path = heapq.heappop(open_list)
        if node in visited:
            continue
        visited.add(node)
        order_of_expansion.append(node)

        # Goal check
        if node == goal:
            print("Order of node expansion:", " → ".join(order_of_expansion))
            print("Optimal Path:", " → ".join(path))
            print("Total Cost:", g)
            return

        for neighbor, cost in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(open_list, (g + cost + heuristic[neighbor], g + cost, neighbor, path + [neighbor]))

    print("No path found!")

# ---- Run A* ----
astar('A', 'F')
