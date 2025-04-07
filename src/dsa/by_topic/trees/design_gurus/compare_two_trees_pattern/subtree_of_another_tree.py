"""
https://leetcode.com/problems/subtree-of-another-tree/description/
"""

# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
from collections import deque
class Solution:


    # Function to check if subRoot is a subtree of root
    def isSubtree(self, root, subRoot):

        if (not root and not subRoot) or (not subRoot):
            return True

        if not root:
            return False

        if self.tree_compare(root ,subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        return left or right



    def tree_compare(self, node1, node2):
        if not node1 and not node2:
            return True

        if not node1 or not node2 or node1.val != node2.val:
            return False

        left = self.tree_compare(node1.left, node2.left)
        right = self.tree_compare(node1.right, node2.right)

        return left and right


