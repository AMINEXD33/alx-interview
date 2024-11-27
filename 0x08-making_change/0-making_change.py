#!/usr/bin/python3
"""Module that has a function that solves the coin change problem"""
import math


def makeChange(coins, total) -> int:
    """a function to calculate the minimum amount of coins
        to get a total value
    """
    dp: list = [math.inf] * (total + 1)
    dp[0] = 0

    for n in range(1, total + 1):
        for coin in range(len(coins)):
            if n - coins[coin] >= 0:
                dp[n] = min(dp[n], 1 + dp[n - coins[coin]])

    if dp[total] == math.inf:
        return -1
    return dp[total]
