arr1 = [1, 4, 7, 2]
arr2 = [10, 100, 300, 200, 1000, 20, 30]


def maxMin(k, arr):
    arr.sort()
    j = k - 1
    diff = float('inf')

    for i in range(len(arr) - j):
        newDiff = arr[j] - arr[i]
        if newDiff < diff:
            diff = newDiff
        j += 1

    return diff


if __name__ == "__main__":
    print(maxMin(2, arr1))
    print(maxMin(3, arr2))
