# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import Counter


def frequency_sort(s: str) -> str:
    return_s = ""
    most_common_ordered = Counter(s).most_common()
    for char, num in most_common_ordered:
        return_s += char * num
    return return_s
