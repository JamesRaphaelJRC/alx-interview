#!/usr/bin/python3
""" Prime Game Algorithm Python """


def is_prime(n):
    """ Checks if a number given n is a prime number """
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))


def calculate_primes(n, primes):
    """ Calculate all primes """
    for i in range(primes[-1] + 1, n + 1):
        if is_prime(i):
            primes.append(i)


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

    for round_num in range(x):
        calculate_primes(nums[round_num], primes)
        sum_options = sum(1 for i in primes[:nums[round_num] + 1] if i != 0)

        if sum_options % 2:
            winner = "Maria"
        else:
            winner = "Ben"

        if winner:
            players_wins[winner] += 1

    if players_wins["Maria"] > players_wins["Ben"]:
        return "Maria"
    elif players_wins["Ben"] > players_wins["Maria"]:
        return "Ben"

    return None
