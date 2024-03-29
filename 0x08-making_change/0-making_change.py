#!/usr/bin/python3
''' Main module '''


def makeChange(coins, total):
    ''' Returns the fewest number of coins needed to meet 'total'
    '''
    if total <= 0:
        return 0

    rem = total
    coins_count = 0
    coin_idx = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while rem > 0:
        if coin_idx >= num_coins:
            return -1
        if rem - sorted_coins[coin_idx] >= 0:
            rem -= sorted_coins[coin_idx]
            coins_count += 1
        else:
            coin_idx += 1

    return coins_count
