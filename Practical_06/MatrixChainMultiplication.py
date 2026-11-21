def matrix_chain_order(dims: list[int]) -> tuple[int, list[list[int]], list[list[int]]]:
    """
    Solve Matrix Chain Multiplication using bottom-up dynamic programming.
    Given dims of length n + 1, matrix i (0-indexed: 0..n-1) has dimensions dims[i] x dims[i+1].
    Returns (min_scalar_multiplications, dp_table, split_table).
    """
    n = len(dims) - 1
    if n <= 1:
        return 0, [[0] * max(n, 1) for _ in range(max(n, 1))], [[0] * max(n, 1) for _ in range(max(n, 1))]

    inf = float("inf")
    dp = [[0] * n for _ in range(n)]      # dp[i][j] = min scalar multiplications for A_i..A_j
    split = [[0] * n for _ in range(n)]   # split[i][j] = index k where optimal split occurs

    # length = number of matrices in the chain (2 up to n)
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = inf

            for k in range(i, j):
                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + dims[i] * dims[k + 1] * dims[j + 1]
                )
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    return int(dp[0][n - 1]), dp, split


def build_parenthesization(split: list[list[int]], i: int, j: int) -> str:
    """Reconstruct the optimal parenthesized expression for matrices A_i through A_j."""
    if i == j:
        return f"A{i + 1}"
    k = split[i][j]
    left = build_parenthesization(split, i, k)
    right = build_parenthesization(split, k + 1, j)
    return f"({left} x {right})"


# Test driver
# 4 matrices: A1(10x30), A2(30x5), A3(5x60), A4(60x3) -> dims = [10, 30, 5, 60, 3]
dims = [10, 30, 5, 60, 3]
min_ops, dp_table, split_table = matrix_chain_order(dims)
expression = build_parenthesization(split_table, 0, len(dims) - 2)

print("Dimensions array:", dims)
print("Minimum scalar multiplications:", min_ops)
print("Optimal parenthesization:", expression)
