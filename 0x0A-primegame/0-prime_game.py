#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of a game based on the given number and
    a list of numbers.

    Parameters:
        x (int): The number to be compared against the list of numbers.
        nums (List[int]): A list of numbers.

    Returns:
        str or None: The winner of the game, either "Maria" or "Ben",
        or None if the input is invalid.

    Algorithm:
        1. Check if the input number is less than or equal to 0 or
        if the list of numbers is empty.
        If so, return None.
        2. Find the maximum number in the list.
        3. Generate a list of primes up to the maximum number using
        the Sieve of Eratosthenes.
        4. Initialize a list of available numbers from 0 to the
        maximum number. Mark 0 and 1 as
        not available.
        5. Iterate through the primes and check if they are available.
        If so, mark them and
        their multiples as not available.
        6. Switch turns between Maria and Ben.
        7. Count the number of wins for Maria and Ben based on the
        outcome of the game for each number in the list.
        8. Return "Maria" if Maria wins more games, "Ben" if Ben
        wins more games, or None if there is a tie.
    """
    if x <= 0 or not nums:
        return None

    max_n = max(nums)

    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False

    p = 2
    while (p * p <= max_n):
        if is_prime[p]:
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1

    primes = [p for p in range(max_n + 1) if is_prime[p]]

    def game(n):
        """
        Play a game where two players, Maria and Ben, take turns
        picking numbers from 0 to n. The first player to pick a
        prime number wins the game.

        Parameters:
            n (int): The maximum number that can be picked.

        Returns:
            str: The winner of the game, either "Maria" or "Ben".

        Algorithm:
            1. Initialize a list of available numbers from 0 to n.
            Mark 0 and 1 as not available.
            2. Iterate through the list of primes up to n.
            3. If a prime number is available, mark it and its
            multiples as not available.
            4. Switch turns between Maria and Ben.
            5. Return "Maria" if Maria wins the game, "Ben" otherwise.
        """

        available = [True] * (n + 1)
        available[0] = available[1] = False
        turn = 0

        for prime in primes:
            if prime > n:
                break
            if available[prime]:
                for multiple in range(prime, n + 1, prime):
                    available[multiple] = False
                turn = 1 - turn

        return "Maria" if turn == 1 else "Ben"

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = game(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
