# https://leetcode.com/problems/find-peak-element/


def find_peak_element(nums: list[int]) -> int:
    # Time complexity: O(n)
    # Space complexity: O(1)
    lst_len = len(nums)
    if lst_len == 1:
        return 0
    if lst_len >= 2 and nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return lst_len - 1
    for i in range(1, lst_len - 1):
        if nums[i - 1] < nums[i] > nums[i + 1]:
            return i


def find_peak_element_logarithmic(nums: list[int]) -> int:
    # Using Binary Search
    # Time complexity: O(log_2(n))
    # Space complexity: O(1)
    left = 0
    right = len(nums)-1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < nums[mid+1]:
            left = mid + 1
        else:
            right = mid
    return left
