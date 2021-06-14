# https://leetcode.com/problems/binary-number-with-alternating-bits/


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if n == 0:
            return True
        bin_repr = bin(n)[2:]
        for i in range(1, len(bin_repr)):
            if bin_repr[i] == bin_repr[i - 1]:
                return False
        return True
