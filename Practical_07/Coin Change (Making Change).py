def min_coins_change(coins: list[int], amount: int) -> tuple[int, list[int]]:
    """
    Find the minimum number of coins needed to form `amount` using unbounded coins.
    Returns (min_coins, chosen_coins). Returns (-1, []) if `amount` cannot be formed.
    """
    if amount < 0:
        raise ValueError("Target amount cannot be negative.")
    if amount == 0:
        return 0, []

    inf = amount + 1
    dp = [inf] * (amount + 1)
    parent = [-1] * (amount + 1)  # Stores the coin denomination that gave the optimal step
    dp[0] = 0

    for current_amt in range(1, amount + 1):
        for coin in coins:
            if coin <= current_amt and dp[current_amt - coin] + 1 < dp[current_amt]:
                dp[current_amt] = dp[current_amt - coin] + 1
                parent[current_amt] = coin

    if dp[amount] == inf:
        return -1, []

    # Reconstruct the coins used
    chosen_coins: list[int] = []
    rem = amount
    while rem > 0 and parent[rem] != -1:
        chosen_coins.append(parent[rem])
        rem -= parent[rem]

    chosen_coins.reverse()
    return dp[amount], chosen_coins


# Test driver
denominations = [1, 2, 5, 10]
target_amount = 18

count, used_coins = min_coins_change(denominations, target_amount)
print("Denominations:", denominations)
print("Target amount:", target_amount)
print("Minimum coins required:", count)
print("Coins used:", used_coins)
