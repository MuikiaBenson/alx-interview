#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines the fewest number of coins needed to meet a given
    total amount given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    # Initialize dp array where dp[i] represents the minimum coins
    # to make total i
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make total 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If dp[total] is still infinity, it means the total can't be made
    return dp[total] if dp[total] != float('inf') else -1
