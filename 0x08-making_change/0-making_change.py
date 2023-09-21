#!/usr/bin/python3
"""
Given a pile of coins of different values 
determine the fewest coins
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins
    """
    if total <= 0:
        return 0
    
    # Create a list to store the minimum number of coins for each amount from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    # Iterate through each coin and update the dp array
    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If dp[total] is still infinity, it means the total cannot be met by the given coins
    if dp[total] == float('inf'):
        return -1
    
    return dp[total]
