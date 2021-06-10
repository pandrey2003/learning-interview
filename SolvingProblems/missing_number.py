# https://leetcode.com/problems/missing-number/


def missing_number(nums: list[int]) -> int:
    n = len(nums)
    set_missing_elem = set(range(n + 1)) - set(nums)
    return next(iter(set_missing_elem))


def missing_number_alternative(nums: list[int]) -> int:
    received_sum = sum(nums)
    needed_sum = len(nums) * (len(nums) + 1) // 2
    return needed_sum - received_sum
