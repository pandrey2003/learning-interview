# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/


class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        length = len(nums)
        set_missing = set(range(1, length + 1)) - set(nums)
        return list(set_missing)
