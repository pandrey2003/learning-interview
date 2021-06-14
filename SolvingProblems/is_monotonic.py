# https://leetcode.com/problems/monotonic-array/


class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        arr_length = len(nums)
        if arr_length == 1:
            return True
        i = 1
        character = None
        while i < arr_length:
            if character is None:
                if nums[i] > nums[i-1]:
                    character = 1
                elif nums[i] < nums[i-1]:
                    character = -1
            elif (nums[i] - nums[i-1]) * character < 0:
                return False
            i += 1
        return True


class SolutionShorter:
    def isMonotonicShorter(self, nums: list[int]) -> bool:
        return all(nums[i] <= nums[i+1] for i in range(len(nums) - 1)) or all(nums[i] >= nums[i+1] for i in range(len(nums) - 1))
