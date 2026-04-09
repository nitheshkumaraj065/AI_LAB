from collections import deque

# Define a simple tree using adjacency list representation
tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def bfs(start_node, tree):
    visited = []          # List to keep track of visited nodes
    queue = deque([start_node])  # Queue for BFS

    while queue:
        node = queue.popleft()   # Dequeue the front element
        if node not in visited:
            visited.append(node)
            # Enqueue all unvisited neighbors
            for neighbor in tree[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return visited

# Run BFS starting from root 'A'
order = bfs('A', tree)
print("Order of nodes visited:", order)