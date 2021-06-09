from collections import defaultdict


def first_unique_char_andrew(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    hash_map = defaultdict(list)
    for i, char in enumerate(s):
        hash_map[char].append(i)
    for index_lst in hash_map.values():
        if len(index_lst) == 1:
            return index_lst[0]
    return -1


def first_unique_element_new(s: str) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    # This solution is better: no dependencies
    hash_map = {}
    for i, char in enumerate(s):
        if char not in hash_map:
            hash_map[char] = i
        else:
            hash_map[char] = -1
    for index in hash_map.values():
        if index != -1:
            return index
    return -1
