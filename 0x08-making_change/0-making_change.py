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
    
    coins.sort(reverse=True)

    i, j_coins = (0, 0)
    dp_total = total
    len_coins = len(coins)

    while(i < len_coins and dp_total > 0):
        if (dp_total - coins[i]) >= 0:
            dp_total -= coins[i]
            j_coins += 1
        else:
            i += 1

    check = dp_total > 0 and j_coins > 0
    return -1 if check or j_coins == 0 else j_coins
