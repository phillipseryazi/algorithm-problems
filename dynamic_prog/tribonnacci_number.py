"""
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.

Ex 1
Input: n = 4
Output: 4
Explanation:
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

Ex 2
Input: n = 25
Output: 1389537
"""


def tribonacci(n: int) -> int:
    return calc(n, {})


def calc(n: int, cache: dict) -> int:
    if n <= 0:
        return 0

    if n == 1 or n == 2:
        return 1

    if n in cache:
        return cache[n]

    cache[n] = calc(n - 1, cache) + calc(n - 2, cache) + calc(n - 3, cache)

    return cache[n]


if __name__ == "__main__":
    print(tribonacci(4))
    print(tribonacci(25))
