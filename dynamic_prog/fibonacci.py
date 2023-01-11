def fib(n, memo: dict):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


if __name__ == '__main__':
    print(fib(3, {}))
    print(fib(7, {}))
    print(fib(8, {}))
    print(fib(50, {}))
    print(fib(500, {}))
