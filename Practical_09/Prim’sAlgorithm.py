import heapq


def prims_mst(num_vertices: int, adj: dict[int, list[tuple[int, int]]], start: int = 0) -> tuple[int, list[tuple[int, int, int]]]:
    """
    Compute a Minimum Spanning Tree using Prim's algorithm with a binary min-heap.
    `adj[u]` contains tuples of `(neighbor_v, weight)`.
    Returns `(total_mst_weight, mst_edges)` where each edge is `(u, v, weight)`.
    """
    if num_vertices <= 0 or start not in adj:
        return 0, []

    in_mst: set[int] = set()
    min_heap: list[tuple[int, int, int]] = [(0, -1, start)]  # (weight, parent_u, current_v)
    mst_edges: list[tuple[int, int, int]] = []
    total_weight = 0

    while min_heap and len(in_mst) < num_vertices:
        weight, u, v = heapq.heappop(min_heap)

        if v in in_mst:
            continue

        in_mst.add(v)
        total_weight += weight

        if u != -1:
            mst_edges.append((u, v, weight))

        for neighbor, edge_weight in adj.get(v, []):
            if neighbor not in in_mst:
                heapq.heappush(min_heap, (edge_weight, v, neighbor))

    return total_weight, mst_edges


# Test driver
# Vertices: 0, 1, 2, 3, 4
graph_adj: dict[int, list[tuple[int, int]]] = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8), (4, 9)],
    4: [(1, 5), (2, 7), (3, 9)],
}

mst_cost, selected_edges = prims_mst(num_vertices=5, adj=graph_adj, start=0)
print("Total MST weight:", mst_cost)
print("Edges in MST (u, v, weight):", selected_edges)
