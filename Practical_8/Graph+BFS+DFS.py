from collections import deque


class Graph:
    """Undirected or directed graph implemented with an adjacency list."""

    def __init__(self, directed: bool = False) -> None:
        self.directed = directed
        self.adj: dict[int, list[int]] = {}

    def add_vertex(self, v: int) -> None:
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u: int, v: int) -> None:
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        if not self.directed:
            self.adj[v].append(u)

    def bfs(self, start: int) -> list[int]:
        """Breadth-First Search traversal starting from `start`."""
        if start not in self.adj:
            return []

        visited: set[int] = {start}
        queue: deque[int] = deque([start])
        order: list[int] = []

        while queue:
            curr = queue.popleft()
            order.append(curr)

            for neighbor in self.adj[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs_recursive(self, start: int) -> list[int]:
        """Depth-First Search traversal using recursion."""
        if start not in self.adj:
            return []

        visited: set[int] = set()
        order: list[int] = []

        def _dfs(node: int) -> None:
            visited.add(node)
            order.append(node)
            for neighbor in self.adj[node]:
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return order

    def dfs_iterative(self, start: int) -> list[int]:
        """Depth-First Search traversal using an explicit stack."""
        if start not in self.adj:
            return []

        visited: set[int] = set()
        stack: list[int] = [start]
        order: list[int] = []

        while stack:
            curr = stack.pop()
            if curr not in visited:
                visited.add(curr)
                order.append(curr)
                # Push neighbors in reverse so standard order is visited first
                for neighbor in reversed(self.adj[curr]):
                    if neighbor not in visited:
                        stack.append(neighbor)

        return order


# Test driver
g = Graph(directed=False)
edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (4, 5)]
for u, v in edges:
    g.add_edge(u, v)

print("Adjacency List:", g.adj)
print("BFS from 0:          ", g.bfs(0))
print("DFS (Recursive) 0:   ", g.dfs_recursive(0))
print("DFS (Iterative) 0:   ", g.dfs_iterative(0))
