#!/usr/bin/python3
"""
Prime Game
"""

def isWinner(x, nums):
    """
    Determines the winner between Maria and Ben based on a game
    played with the given parameters.

    Args:
        x (int): An integer representing a condition.
        nums (list): A list of integers representing the game rounds.

    Returns:
        str or None: The winner of the game, either 'Maria' or
        'Ben', or None if it's a tie.

    Algorithm:
        1. Generates a list of prime numbers up to the maximum number in `nums`.
        2. Plays the game for each round by calling the `game` function with
        the current number and the list of prime numbers.
        3. Determines the winner of each round based on the current number
        and the list of prime numbers.
        4. Compares the number of wins for Maria and Ben.
        5. Returns the winner, either 'Maria' or 'Ben', or
        None if they have the same number of wins.
    """
    if x <= 0 or not nums:
        return None

    marias_wins, bens_wins = 0, 0

    # Generate primes with a limit of the maximum number in nums
    max_n = max(nums)
    is_prime = [True] * (max_n + 1)
    is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime numbers

    for i in range(2, int(max_n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, max_n + 1, i):
                is_prime[j] = False

    # Play the game for each round
    for n in nums:
        winner = game(n, is_prime)
        if winner == "Maria":
            marias_wins += 1
        else:
            bens_wins += 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'


def game(n, is_prime):
    """
    Determines the winner of a game played with the given parameters.

    Args:
        n (int): An integer representing the maximum number in the game.
        is_prime (list): A list of booleans representing whether each number
            from 2 to n is prime or not.

    Returns:
        str: The winner of the game, either 'Maria' or 'Ben'.

    Algorithm:
        1. Initialize a list of available numbers from 1 to n.
        2. Iterate through numbers from 2 to n.
        3. If a number is prime and available, mark all its multiples as
           unavailable.
        4. Switch the turn to the other player.
        5. Return 'Maria' if it is her turn, otherwise return 'Ben'.
    """
    available = [True] * (n + 1)
    available[0] = available[1] = False
    turn = 0

    for i in range(2, n + 1):
        if is_prime[i] and available[i]:
            for multiple in range(i, n + 1, i):
                available[multiple] = False
            turn = 1 - turn

    return "Maria" if turn == 1 else "Ben"
