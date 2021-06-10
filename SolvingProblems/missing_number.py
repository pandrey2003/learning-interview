# https://leetcode.com/problems/missing-number/


def missing_number(nums: list[int]) -> int:
    n = len(nums)
    set_missing_elem = set(range(n + 1)) - set(nums)
    return next(iter(set_missing_elem))
