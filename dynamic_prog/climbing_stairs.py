def climbStairs(n: int) -> int:
    if n == 1:
        return 1

    arr = [0] * (n + 1)
    arr[0] = 1
    arr[1] = 1

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


if __name__ == "__main__":
    print(climbStairs(5))
