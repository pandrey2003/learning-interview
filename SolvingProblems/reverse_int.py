# https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        char_x = [char for char in str(x)]
        if char_x[0] == "-":
            reversed_int = -1 * int("".join(char_x[1:][::-1]))
        else:
            reversed_int = int("".join(char_x[::-1]))
        if abs(reversed_int) >= 2**31 or reversed_int == 2**31 - 1:
            return 0
        return reversed_int
