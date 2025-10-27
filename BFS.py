# Breadth-First Search (BFS) Implementation in Python

from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = set()             # Set to keep track of visited nodes
    queue = deque([start])      # Queue for BFS
    traversal_order = []        # List to store the order of traversal

    while queue:
        node = queue.popleft()  # Remove node from queue

        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            # Add all unvisited neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return traversal_order


# ----------- Main Program -----------
if __name__ == "__main__":
    # Representing graph as an adjacency list
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }

    start_node = 'A'  # Starting node
    print("Graph:", graph)
    print("Starting BFS from node:", start_node)

    order = bfs(graph, start_node)
    print("\nBFS Traversal Order:", " → ".join(order))
