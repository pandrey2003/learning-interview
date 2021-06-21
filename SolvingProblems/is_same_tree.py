# https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        return self.isSameTreeRecursive(p, q)

    def isSameTreeRecursive(self, f_tree_node: TreeNode, s_tree_node: TreeNode):
        if f_tree_node is None and s_tree_node is None:
            return True
        if f_tree_node and not s_tree_node or s_tree_node and not f_tree_node:
            return False
        if f_tree_node.val != s_tree_node.val:
            return False
        return self.isSameTreeRecursive(f_tree_node.left, s_tree_node.left) and self.isSameTreeRecursive(
            f_tree_node.right, s_tree_node.right)
