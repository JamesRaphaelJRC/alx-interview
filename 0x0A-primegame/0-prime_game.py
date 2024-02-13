#!/usr/bin/python3
''' Prime Game module '''


def sieve_of_eratosthenes(n):
    ''' Uses sieve of Eratosthenes to calculate prime numbers '''
    primes = [True] * (n + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n + 1, i):
                primes[j] = False
    return [num for num, is_prime in enumerate(primes) if is_prime]


def isWinner(x, nums):
    ''' Calculates and determines the winner of the game '''
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)
    dp = [0] * (max_n + 1)

    for n in range(2, max_n + 1):
        dp[n] = not all(dp[n - p] for p in primes if p <= n)

    maria_wins = sum(dp[num] for num in nums)

    if maria_wins > x - maria_wins:
        return "Maria"
    elif maria_wins < x - maria_wins:
        return "Ben"
    else:
        return None
