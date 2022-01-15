# https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dp = {}
        for cur_index, num in enumerate(nums):
            if dp.get(num) is None:
                dp[num] = cur_index
                continue
            prev_index = dp[num]
            if cur_index - prev_index <= k:
                return True
            dp[num] = cur_index
        return False
