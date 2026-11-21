class DisjointSet:
    """Disjoint Set Union (Union-Find) with path compression and union by size."""

    def __init__(self, n: int) -> None:
        self.parent: list[int] = list(range(n))
        self.size: list[int] = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a == root_b:
            return False  # Already connected; adding edge (a, b) would create a cycle

        # Attach smaller component under larger component
        if self.size[root_a] < self.size[root_b]:
            root_a, root_b = root_b, root_a

        self.parent[root_b] = root_a
        self.size[root_a] += self.size[root_b]
        return True


def kruskals_mst(num_vertices: int, edges: list[tuple[int, int, int]]) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Compute a Minimum Spanning Tree using Kruskal's algorithm.
    Each tuple in `edges` is `(u, v, weight)` with vertices in `0 .. num_vertices - 1`.
    Returns `(total_mst_weight, mst_edges)`.
    """
    if num_vertices <= 1:
        return 0, []

    # Sort edges by weight ascending
    sorted_edges = sorted(edges, key=lambda edge: edge[2])
    dsu = DisjointSet(num_vertices)

    mst_edges: list[tuple[int, int, int]] = []
    total_weight = 0

    for u, v, weight in sorted_edges:
        if dsu.union(u, v):
            mst_edges.append((u, v, weight))
            total_weight += weight
            if len(mst_edges) == num_vertices - 1:
                break

    return total_weight, mst_edges


# Test driver
# Vertices: 0, 1, 2, 3, 4 | Edges: (u, v, weight)
graph_edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9),
]

mst_cost, selected_edges = kruskals_mst(num_vertices=5, edges=graph_edges)
print("Total MST weight:", mst_cost)
print("Edges in MST (u, v, weight):", selected_edges)
