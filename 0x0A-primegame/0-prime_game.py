#!/usr/bin/python3
''' Prime Game module '''


def is_prime(num):
    ''' Checks if a number is a prime number'''
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_up_to_n(n):
    ''' gets a list of prime numbers from 0 to n '''
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    ''' Gets the winner of the game '''
    def can_win(n):
        primes = get_primes_up_to_n(n)
        total_primes = len(primes)

        # Check if the total number of primes is even or odd
        if total_primes % 2 == 0:
            # If even, Ben wins
            return "Ben"
        else:
            # If odd, Maria wins
            return "Maria"

    winners = [can_win(num) for num in nums]

    # Count the occurrences of each winner
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
