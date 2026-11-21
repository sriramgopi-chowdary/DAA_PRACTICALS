import math


def tsp_held_karp(dist: list[list[float]], start: int = 0) -> tuple[float, list[int]]:
    """
    Solve the metric/general TSP for `n` cities using Held-Karp bitmask DP.
    `dist[i][j]` is travel cost from city `i` to city `j`.
    Returns `(min_tour_cost, tour_path)` starting and ending at `start`.
    """
    n = len(dist)
    if n == 0:
        return 0.0, []
    if n == 1:
        return 0.0, [start, start]

    full_mask = (1 << n) - 1
    inf = math.inf

    # dp[mask][u] = min cost to start at `start`, visit all cities in `mask`, and end at `u`
    dp = [[inf] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    start_mask = 1 << start
    dp[start_mask][start] = 0.0

    for mask in range(1 << n):
        if not (mask & start_mask):
            continue
        for u in range(n):
            if not (mask & (1 << u)) or math.isinf(dp[mask][u]):
                continue
            for v in range(n):
                if mask & (1 << v) or math.isinf(dist[u][v]):
                    continue
                next_mask = mask | (1 << v)
                new_cost = dp[mask][u] + dist[u][v]
                if new_cost < dp[next_mask][v]:
                    dp[next_mask][v] = new_cost
                    parent[next_mask][v] = u

    # Close the tour by returning to `start`
    best_cost = inf
    last_city = -1
    for u in range(n):
        if u == start or math.isinf(dp[full_mask][u]) or math.isinf(dist[u][start]):
            continue
        total = dp[full_mask][u] + dist[u][start]
        if total < best_cost:
            best_cost = total
            last_city = u

    if last_city == -1 or math.isinf(best_cost):
        return inf, []

    # Reconstruct path backwards from `last_city`
    rev_path: list[int] = []
    curr_mask = full_mask
    curr_city = last_city
    while curr_city != -1:
        rev_path.append(curr_city)
        prev_city = parent[curr_mask][curr_city]
        curr_mask ^= 1 << curr_city
        curr_city = prev_city

    path = list(reversed(rev_path)) + [start]
    return best_cost, path


# Test driver (4 cities: 0, 1, 2, 3)
cost_matrix = [
    [0,  10, 15, 20],
    [10, 0,  35, 25],
    [15, 35, 0,  30],
    [20, 25, 30, 0],
]

min_tour_cost, route = tsp_held_karp(cost_matrix, start=0)
print("Minimum tour cost:", min_tour_cost)
print("Optimal route:    ", " -> ".join(map(str, route)))
