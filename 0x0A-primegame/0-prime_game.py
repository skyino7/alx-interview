#!/usr/bin/python3
"""
Prime Game
"""

def isWinner(x, nums):
    """
    Determines the winner of a prime game session with x rounds.

    Parameters:
        x (int): The number of rounds.
        nums (List[int]): A list of numbers, each representing the range for a round.

    Returns:
        str or None: The winner of the most rounds, either "Maria" or "Ben",
        or None if the input is invalid or there's a tie.
    """
    if x <= 0 or not nums:
        return None

    marias_wins, bens_wins = 0, 0


    n = max(nums)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    for _, n in zip(range(x), nums):
        primes_count = sum(is_prime[0:n+1])
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
