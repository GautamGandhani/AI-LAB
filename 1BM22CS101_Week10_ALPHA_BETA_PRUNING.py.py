import math
import sys

# Alpha-Beta Pruning function
def alpha_beta_pruning(depth, node_index, is_max, values, alpha, beta, max_depth):
    # Base case: return the value at the leaf node
    if depth == max_depth:
        return values[node_index]

    # If it's a MAX node
    if is_max:
        best = -sys.maxsize  # Initialize best value as -∞
        
        # Explore left and right children
        for i in range(2):
            child = node_index * 2 + i
            val = alpha_beta_pruning(depth + 1, child, False, values, alpha, beta, max_depth)
            best = max(best, val)  # MAX updates its best value
            alpha = max(alpha, best)  # Update alpha

            # Alpha-Beta Pruning
            if beta <= alpha:
                print(f"Pruned subtree at node: {child} (alpha={alpha}, beta={beta})")
                break
        return best

    else:
        best = sys.maxsize  # Initialize best value as +∞
        
        # Explore left and right children
        for i in range(2):
            child = node_index * 2 + i
            val = alpha_beta_pruning(depth + 1, child, True, values, alpha, beta, max_depth)
            best = min(best, val)  # MIN updates its best value
            beta = min(beta, best)  # Update beta

            # Alpha-Beta Pruning
            if beta <= alpha:
                print(f"Pruned subtree at node: {child} (alpha={alpha}, beta={beta})")
                break
        return best


if __name__ == "__main__":
    # Leaf nodes of the game tree
    values = [3, 5, 6, 9, 1, 2, 0, 4]  # Example leaf values

    # Depth of the game tree
    max_depth = int(math.log2(len(values)))

    alpha = -sys.maxsize  # Initialize alpha as -∞
    beta = sys.maxsize    # Initialize beta as +∞

    # Start Alpha-Beta Pruning
    print("Starting Alpha-Beta Pruning...\n")
    optimal_value = alpha_beta_pruning(0, 0, True, values, alpha, beta, max_depth)
    print("\nThe optimal value for the root MAX node is:", optimal_value)
