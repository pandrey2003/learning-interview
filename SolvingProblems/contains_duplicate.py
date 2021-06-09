# https://leetcode.com/problems/contains-duplicate/


def contains_duplicate(nums: list[int]) -> bool:
    return True if len(set(nums)) < len(nums) else False
