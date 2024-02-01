#!/usr/bin/python3
''' Main module '''


def makeChange(coins, total):
    if total < 0:
        return -1

    # Initialize an array to store the minimum number of coins needed for each amount
    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # You need 0 coins to make change for 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
