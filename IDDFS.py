def dls(node, goal, depth, visited_order, tree):
    """
    Depth-Limited Search (DLS)
    node: current node
    goal: target node
    depth: current depth limit
    visited_order: list to track visited nodes
    tree: adjacency list representation of the tree
    """
    if depth == 0:
        visited_order.append(node)
        return node == goal
    
    visited_order.append(node)
    if node == goal:
        return True
    
    if node not in tree:  # leaf node
        return False
    
    for child in tree[node]:
        if dls(child, goal, depth - 1, visited_order, tree):
            return True
    return False


def iddfs(root, goal, tree, max_depth=10):
    """
    Iterative Deepening DFS (IDDFS)
    root: starting node
    goal: target node
    tree: adjacency list representation of the tree
    max_depth: maximum depth to search
    """
    for depth in range(max_depth + 1):
        visited_order = []
        print(f"\nDepth Limit = {depth}")
        found = dls(root, goal, depth, visited_order, tree)
        print("Visited Order:", visited_order)
        
        if found:
            print(f"Goal '{goal}' found at depth {depth}")
            return True
    print(f"Goal '{goal}' not found within depth {max_depth}")
    return False


# Example usage:
if __name__ == "__main__":
    # Tree represented as adjacency list
    tree = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F', 'G'],
        'E': ['H']
    }
    
    root = 'A'
    goal = 'H'
    
    iddfs(root, goal, tree, max_depth=5)