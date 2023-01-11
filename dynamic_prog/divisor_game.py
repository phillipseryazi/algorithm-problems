"""
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.

Input: n = 2
Output: true
Explanation: Alice chooses 1, and Bob has no more moves.

Input: n = 3
Output: false
Explanation: Alice chooses 1, Bob chooses 1, and Alice has no more moves.
"""


def divisorGame(n: int) -> bool:
    return calc(n, {})


def calc(n: int, cache: dict) -> bool:
    if n <= 1:
        return False

    if n in cache:
        return cache[n]

    for num in range(1, n):
        if n % num == 0:
            if not calc(n - 1, cache):
                cache[n] = True
                return True

    cache[n] = False
    return False


if __name__ == "__main__":
    print(divisorGame(1))
    print(divisorGame(2))
    print(divisorGame(3))
    print(divisorGame(4))
    print(divisorGame(5))
