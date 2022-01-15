from collections import defaultdict


def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    char_s = defaultdict(int)
    char_t = defaultdict(int)
    for char in s:
        char_s[char] += 1
    for char in t:
        char_t[char] += 1
    return char_s == char_t
