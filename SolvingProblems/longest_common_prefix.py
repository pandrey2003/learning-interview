# https://leetcode.com/problems/longest-common-prefix/


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ''

    shortest_string = min(strs, key=len)

    for i, character in enumerate(shortest_string):
        for string in strs:
            if character != string[i]:
                return shortest_string[:i]

    return shortest_string
