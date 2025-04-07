"""
https://leetcode.com/problems/symmetric-tree/description/
"""


# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):

        if not root:
            return True

        def helper(node1, node2):
            if not node1 and not node2:
                return True

            if not node1 or not node2 or node1.val != node2.val:
                return False

            left = helper(node1.left, node2.right)
            right = helper(node1.right, node2.left)

            return left and right

        return helper(root.left, root.right)
