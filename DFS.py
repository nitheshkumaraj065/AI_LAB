tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(node, visited, tree):
    if node not in visited:
        visited.append(node)
        # Recursively visit each neighbor
        for neighbor in tree[node]:
            dfs(neighbor, visited, tree)

    return visited

# Run DFS starting from root 'A'
visited_order = dfs('A', [], tree)
print("Order of nodes visited:", visited_order)