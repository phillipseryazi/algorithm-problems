nums = [7, 1, 3, 2, 4, 5, 6]
nums2 = [4, 3, 1, 2]


def minimumSwaps(arr):
    swaps = 0

    for i in range(len(arr)):
        while arr[i] != i + 1:
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]
            swaps += 1
            print(i)

    return swaps


if __name__ == "__main__":
    print(minimumSwaps(nums))
    # print(minimumSwaps(nums2))
