tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dls(node, tree, limit, depth=0, visited=None):
    if visited is None:
        visited = []

    # Visit the current node
    visited.append(node)

    # Stop if depth limit is reached
    if depth == limit:
        return visited

    # Explore neighbors if within depth limit
    for neighbor in tree[node]:
        dls(neighbor, tree, limit, depth + 1, visited)

    return visited

# Example usage
depth_limit = 2
visited_order = dls('A', tree, depth_limit)
print(f"Order of nodes visited up to depth {depth_limit}:", visited_order)