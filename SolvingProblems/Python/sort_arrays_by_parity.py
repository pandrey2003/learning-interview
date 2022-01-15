# https://leetcode.com/problems/sort-array-by-parity/
def sort_array_by_parity(nums: list[int]) -> list[int]:
    return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 != 0]
