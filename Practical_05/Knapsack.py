def knapsack_01(weights: list[int], values: list[int], capacity: int) -> tuple[int, list[int]]:
    """
    Solve the 0/1 Knapsack problem using bottom-up dynamic programming.
    Returns (max_value, selected_item_indices).
    """
    n = len(weights)
    # dp[i][w] = max value using first i items (1..i) with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        wt = weights[i - 1]
        val = values[i - 1]
        for w in range(capacity + 1):
            if wt <= w:
                dp[i][w] = max(dp[i - 1][w], val + dp[i - 1][w - wt])
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find which 0-based items were chosen
    selected_indices: list[int] = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            idx = i - 1
            selected_indices.append(idx)
            w -= weights[idx]

    selected_indices.reverse()
    return dp[n][capacity], selected_indices


# Test driver
weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

max_val, chosen = knapsack_01(weights, values, capacity)
print("Maximum value:", max_val)
print("Selected item indices:", chosen)
print("Chosen weights/values:", [(weights[i], values[i]) for i in chosen])
