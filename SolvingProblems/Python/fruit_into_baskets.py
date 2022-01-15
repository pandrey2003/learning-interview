# https://leetcode.com/problems/fruit-into-baskets/


def totalFruit(tree: list[int]) -> int:
    if tree is None or len(tree) == 0:
        return 0
    maximum = 1
    hash_map = {}
    i, j = 0, 0
    while j < len(tree):
        if len(hash_map) <= 2:
            hash_map[tree[j]] = j
            j += 1
        if len(hash_map) > 2:
            minimum = len(tree) - 1
            for value in hash_map.values():
                minimum = min(minimum, value)
            i = minimum + 1
            del hash_map[tree[minimum]]
        maximum = max(maximum, j - i)
    return maximum


if __name__ == "__main__":
    print(totalFruit([1, 2, 3, 2, 2]))
