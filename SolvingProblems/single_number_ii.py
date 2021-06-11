# https://leetcode.com/problems/single-number-ii/


def single_number_ii(nums: list[int]) -> int:
    hash_map = {}
    for num in nums:
        if num not in hash_map:
            hash_map[num] = 1
        else:
            hash_map[num] += 1
    filtered_key = filter(lambda key: (hash_map[key] == 1), hash_map)
    return next(filtered_key)
