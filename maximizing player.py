# Minimax Algorithm for a perfect binary tree

def minimax(depth, node_index, is_max, values, max_depth):
    # Base case: if leaf node reached
    if depth == max_depth:
        return values[node_index]

    if is_max:
        return max(
            minimax(depth + 1, node_index * 2, False, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, False, values, max_depth)
        )
    else:
        return min(
            minimax(depth + 1, node_index * 2, True, values, max_depth),
            minimax(depth + 1, node_index * 2 + 1, True, values, max_depth)
        )

# ---- Example ----
# 4 final (leaf) states in a perfect binary tree
values = [3, 5, 2, 9]  # utility values at leaf nodes
max_depth = 2  # since 2 levels from root to leaves

optimal_value = minimax(0, 0, True, values, max_depth)

print("Leaf node values:", values)
print("The optimal value for the maximizing player is:", optimal_value)
