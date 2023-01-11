from typing import List


def can_sum(target_sum, nums: List[int], memo: dict) -> bool:
    if target_sum in memo:
        return memo[target_sum]

    if target_sum == 0:
        return True

    if target_sum < 0:
        return False

    for num in nums:
        remainder = target_sum - num
        if can_sum(remainder, nums, memo) is True:
            memo[target_sum] = True
            return True

    memo[target_sum] = False
    return False


def can_sum(target_sum, nums: List[int]) -> bool:
    pass


if __name__ == "__main__":
    print(can_sum(7, [2, 3], {}))
    print(can_sum(7, [5, 3, 4, 7], {}))
    print(can_sum(7, [2, 4], {}))
    print(can_sum(8, [2, 3, 5], {}))
    print(can_sum(300, [7, 14], {}))
