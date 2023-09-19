#!/usr/bin/python3


def makeChange(coins, total):
    coins.sort()
    neededCoins = 0
    while total > 0:
        if coins:
            coin = coins.pop()
        else:
            return -1
        neededCoins += (total // coin)
        total %= coin
    return neededCoins


print(makeChange([1, 2, 25], -1))

print(makeChange([1256, 54, 48, 16, 102], 1453))
