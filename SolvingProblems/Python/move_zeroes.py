def move_zeroes(nums):
    # Space O(N) which is dissatisfactory for LeetCode
    zeroes = nums.count(0)
    new_lst = [num for num in nums if num != 0]
    return new_lst + [0] * zeroes


def move_zeroes_o_1_space(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1
    for i in range(index, len(nums)):
        nums[i] = 0
    return nums


if __name__ == "__main__":
    print(move_zeroes([0, 1, 0, 3, 12]))
    print(move_zeroes_o_1_space([0, 1, 0, 3, 12]))
