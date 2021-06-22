# https://leetcode.com/problems/combination-sum-ii/
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self.find_candidates(candidates, 0, target, [], result)
        return result

    def find_candidates(self, candidates: List[int], index: int, target: int, curr_list: List[int],
                        result: List[List[int]]):
        if target == 0:
            result.append(curr_list)
            return
        if target < 0:
            return
        for i in range(index, len(candidates)):
            if index == i or candidates[i - 1] != candidates[i]:
                curr_list.append(candidates[i])
                self.find_candidates(candidates, i + 1, target - candidates[i], curr_list.copy(), result)
                curr_list.pop()
