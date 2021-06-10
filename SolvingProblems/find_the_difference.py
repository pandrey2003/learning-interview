# https://leetcode.com/problems/find-the-difference/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_as_dict = {}
        for char in s:
            if char not in s_as_dict:
                s_as_dict[char] = 1
            else:
                s_as_dict[char] += 1
        for char in t:
            if s_as_dict.get(char) == 0 or s_as_dict.get(char) is None:
                return char
            else:
                s_as_dict[char] -= 1
        return "!"
