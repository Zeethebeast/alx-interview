#!/usr/bin/python3
"""Given a pile of coins of different values,
determine the fewest number of coins needed to
meet a given amount total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if coin > total:
            continue
        while total >= coin:
            total -= coin
            count += 1

    return count if total == 0 else -1
