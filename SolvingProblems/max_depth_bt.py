# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.maxDepthRecursive(root, 0)

    def maxDepthRecursive(self, node: TreeNode, counter: int) -> int:
        if node is None:
            return counter
        return max(self.maxDepthRecursive(node.left, counter + 1), self.maxDepthRecursive(node.right, counter + 1))
