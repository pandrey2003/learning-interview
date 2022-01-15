# https://leetcode.com/problems/path-sum-ii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        paths, currentPath = [], []
        self.find_path(root, targetSum, currentPath, paths)
        return paths

    def find_path(self, root: TreeNode, targetSum: int, currentPath: list, paths: list):
        if root is None:
            return
        currentPath.append(root.val)
        if root.val == targetSum and root.left is None and root.right is None:
            paths.append(currentPath)
            return
        self.find_path(root.left, targetSum - root.val, currentPath.copy(), paths)
        self.find_path(root.right, targetSum - root.val, currentPath.copy(), paths)
