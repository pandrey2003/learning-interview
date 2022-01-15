# https://leetcode.com/problems/backspace-string-compare/


class Solution:
    def backspace_compare(self, s: str, t: str) -> bool:
        # Time complexity: O(n)
        # Space complexity: O(1)
        new_s = self.strip_str(s)
        new_t = self.strip_str(t)
        return new_s == new_t

    @staticmethod
    def strip_str(string: str):
        index = 1
        while index < len(string):
            if string[index] == "#":
                string = string[:index - 1] + string[index + 1:]
                index -= 1 if index > 1 else 0
                continue
            index += 1
        return string.strip("#")
