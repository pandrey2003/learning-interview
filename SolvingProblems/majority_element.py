# https://leetcode.com/problems/majority-element


def majority_element(nums: list[int]) -> int:
    # Good O(N) for time, but can improve from O(n) space
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 1
        else:
            counts[num] += 1
    threshold = len(nums) // 2
    for num, count in counts.items():
        if count > threshold:
            return num


def majority_element_better_space(nums: list[int]) -> int:
    # O(N) space, but technically better
    if len(nums) == 1:
        return nums[0]
    counts = {}
    threshold = len(nums) // 2
    for num in nums:
        if num not in counts:
            counts[num] = 1
        elif counts[num] == threshold:
            return num
        else:
            counts[num] += 1
