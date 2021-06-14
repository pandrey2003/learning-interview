# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        if root is None:
            return []
        return self.postorderRecursive(root, [])

    def postorderRecursive(self, node, node_list):
        if node.left:
            self.postorderRecursive(node.left, node_list)
        if node.right:
            self.postorderRecursive(node.right, node_list)
        node_list.append(node.val)
        return node_list
