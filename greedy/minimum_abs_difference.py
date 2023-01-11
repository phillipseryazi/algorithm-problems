a = [-2, 2, 4]


def minimumAbsoluteDifference(arr):
    minDiff = float("inf")
    sortedArr = sorted(arr)

    for i in range(len(sortedArr) - 1):
        diff = abs(sortedArr[i] - sortedArr[i + 1])
        if diff < minDiff:
            minDiff = diff

    return minDiff


if __name__ == "__main__":
    print(minimumAbsoluteDifference(a))
