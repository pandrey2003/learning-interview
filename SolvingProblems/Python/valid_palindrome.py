# https://leetcode.com/problems/valid-palindrome/


import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ", "")
        if len(s) <= 1:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
