from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        print("BFS:", end=" ")
        while queue:
            node = queue.popleft()
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
        print()

    def dfs_util(self, node, visited):
        visited.add(node)
        print(node, end=" ")
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

    def dfs(self, start):
        visited = set()
        print("DFS:", end=" ")
        self.dfs_util(start, visited)
        print()


# Sample Workouts
graph = Graph()
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (3, 6)]
for u, v in edges:
    graph.add_edge(u, v)

print("Graph Traversals:")
graph.bfs(0)  # BFS: 0 1 2 3 4 5 6
graph.dfs(0)  # DFS: 0 1 3 6 4 2 5