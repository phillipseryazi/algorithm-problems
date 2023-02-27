def fib(n, memo: dict):
    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)

    return memo[n]


def fib2(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    arr = [0] * (n + 1)

    arr[0] = 0
    arr[1] = 1

    for i in range(2, n + 1):
        arr[i] = arr[i - 2] + arr[i - 1]

    return arr[n]


if __name__ == '__main__':
    print(fib(3, {}))
    print(fib(7, {}))
    print(fib(8, {}))
    print(fib(50, {}))
    print(fib(500, {}))
    print("-----------")
    print(fib2(2))
    print(fib2(3))
    print(fib2(7))
    print(fib2(8))
    print(fib2(50))
    print(fib2(500))
