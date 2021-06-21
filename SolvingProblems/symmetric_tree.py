# https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.isSymmetricRecursive(root.left, root.right)

    def isSymmetricRecursive(self, left_node, right_node):
        if left_node is None and right_node is None:
            return True
        if not (left_node and right_node):
            return False
        if left_node.val != right_node.val:
            return False
        return self.isSymmetricRecursive(right_node.left, left_node.right) \
            and self.isSymmetricRecursive(left_node.left, right_node.right)
