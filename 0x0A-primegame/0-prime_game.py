#!/usr/bin/python3
""" Prime Game Algorithm Python """


def is_prime(n):
    """ Checks if a number given n is a prime number """
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def calculate_primes(n, primes):
    """ Calculate all primes """
    top_prime = primes[-1]
    primes.extend(i for i in range(top_prime + 1, n + 1) if is_prime(i))


def isWinner(x, nums):
    """
    Arguments:
    x - number of rounds.
    nums - an array of n

    Return:
        - name of the player that won the most rounds
        - If winner cannot be determined, return None

    Assumption:
        n and x will not be larger than 10000
    """

    players_wins = {"Maria": 0, "Ben": 0}

    primes = [0, 0, 2]

    calculate_primes(max(nums), primes)

    for n in nums:
        sum_options = sum(i != 0 and i <= n for i in primes[:n + 1])

        winner = "Maria" if sum_options % 2 else "Ben"

        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
