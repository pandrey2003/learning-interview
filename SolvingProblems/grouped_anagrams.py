# https://leetcode.com/problems/group-anagrams/
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    hash_map = {}
    for string in strs:
        str_sorted = str(sorted(list(string)))
        if str_sorted not in hash_map:
            hash_map[str_sorted] = []
        hash_map[str_sorted].append(string)
    return list(hash_map.values())
