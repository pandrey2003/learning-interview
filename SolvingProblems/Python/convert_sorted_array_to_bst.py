# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums is None or len(nums) == 0:
            return None
        return self.construct_bst(nums, 0, len(nums) - 1)

    def construct_bst(self, nums: List[int], left: int, right: int):
        if left > right:
            return None
        mid = (left + right) // 2
        current_node = TreeNode(val=nums[mid])
        current_node.left = self.construct_bst(nums, left, mid - 1)
        current_node.right = self.construct_bst(nums, mid + 1, right)
        return current_node
