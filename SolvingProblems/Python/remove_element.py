# https://leetcode.com/problems/remove-element/


def remove_element(nums: list[int], val: int) -> int:
    index = 0
    for num in nums:
        if val != num:
            nums[index] = num
            index += 1
    return index
