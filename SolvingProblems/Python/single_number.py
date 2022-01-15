# https://leetcode.com/problems/single-number/


def single_number(nums: list[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(n)
    hash_set = set()
    for number in nums:
        if number not in hash_set:
            hash_set.add(number)
        else:
            hash_set.remove(number)
    (number, ) = hash_set
    return number
