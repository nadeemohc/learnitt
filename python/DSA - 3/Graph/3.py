def is_connected(graph):
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(next(iter(graph)))  # Start from any node
    return len(visited) == len(graph)


# Sample Workouts
graph = {0: [1, 2], 1: [0, 3], 2: [0], 3: [1]}
print("Is Graph Connected?", is_connected(graph))  # True