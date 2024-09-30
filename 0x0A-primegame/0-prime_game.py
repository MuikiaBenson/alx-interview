#!/usr/bin/python3
''' Prime game module '''

def rwh_primes(n):
    '''
    Generate a list of primes up to n using an efficient sieve algorithm.
    '''
    sieve = [True] * n
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i]:
            sieve[i * i::2 * i] = [False] * int((n - i * i - 1) / (2 * i) + 1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def playMatch(n):
    ''' Plays a single round, returns 0 if Maria wins, 1 if Ben wins. '''
    primes = rwh_primes(n + 1)
    return 1 - (len(primes) % 2) if n > 1 else 1


def isWinner(x, nums):
    ''' Plays x rounds of the game and returns the overall winner. '''
    if not nums or x < 1:
        return None

    players = {0: 'Maria', 1: 'Ben'}
    wins = {0: 0, 1: 0}

    for num in nums:
        wins[playMatch(num)] += 1

    # Determine the overall winner
    if wins[0] == wins[1]:
        return None
    return players[0] if wins[0] > wins[1] else players[1]
