"""
https://www.geeksforgeeks.org/tree-isomorphism-problem/
"""
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def isIsomorphic(self, root1, root2):

        if not root1 and not root2:
            return True

        if not root1 or not root2 or root1.val != root2.val:
            return False

        # check with out swapping
        left = self.isIsomorphic(root1.left, root2.left)
        right = self.isIsomorphic(root1.right, root2.right)

        # check after swapping
        if not (left and right):
            left = self.isIsomorphic(root1.left, root2.right)
            right = self.isIsomorphic(root1.right, root2.left)

        return left and right









