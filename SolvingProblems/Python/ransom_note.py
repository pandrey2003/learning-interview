# https://leetcode.com/problems/ransom-note/
from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_counter = Counter(ransomNote)
        magazine_counter = Counter(magazine)
        for key in note_counter.keys():
            if magazine_counter[key] < note_counter[key]:
                return False
        return True
