import math


def floyd_warshall(adj_matrix: list[list[float]]) -> tuple[list[list[float]], list[list[int | None]], bool]:
    """
    Compute all-pairs shortest paths using the Floyd-Warshall algorithm.
    `adj_matrix[i][j]` is edge weight from i to j, `0` if i == j, or `math.inf` if no direct edge.
    Returns `(dist_matrix, next_node_matrix, has_negative_cycle)`.
    """
    n = len(adj_matrix)
    dist = [row[:] for row in adj_matrix]
    next_node: list[list[int | None]] = [[None] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i != j and not math.isinf(dist[i][j]):
                next_node[i][j] = j

    # k must be the outermost loop: allow vertices 0..k as intermediates
    for k in range(n):
        for i in range(n):
            if math.isinf(dist[i][k]):
                continue
            for j in range(n):
                if math.isinf(dist[k][j]):
                    continue
                via_k = dist[i][k] + dist[k][j]
                if via_k < dist[i][j]:
                    dist[i][j] = via_k
                    next_node[i][j] = next_node[i][k]

    has_negative_cycle = any(dist[i][i] < 0 for i in range(n))
    return dist, next_node, has_negative_cycle


def reconstruct_path(next_node: list[list[int | None]], start: int, end: int) -> list[int]:
    """Reconstruct shortest path from `start` to `end`, or return [] if unreachable."""
    if next_node[start][end] is None:
        return []
    path = [start]
    curr = start
    while curr != end:
        nxt = next_node[curr][end]
        if nxt is None:
            return []
        curr = nxt
        path.append(curr)
    return path


# Test driver (4 vertices: 0, 1, 2, 3)
INF = math.inf
graph = [
    [0,   3,   INF, 7],
    [8,   0,   2,   INF],
    [5,   INF, 0,   1],
    [2,   INF, INF, 0],
]

shortest_dist, next_hop, neg_cycle = floyd_warshall(graph)

print("Has negative cycle:", neg_cycle)
print("\nShortest Distance Matrix:")
for row in shortest_dist:
    print(["INF" if math.isinf(x) else int(x) for x in row])

print("\nSample shortest paths:")
for u, v in [(0, 2), (3, 1), (1, 3)]:
    p = reconstruct_path(next_hop, u, v)
    cost = "INF" if math.isinf(shortest_dist[u][v]) else int(shortest_dist[u][v])
    print(f"  {u} -> {v}: path={p}, cost={cost}")
