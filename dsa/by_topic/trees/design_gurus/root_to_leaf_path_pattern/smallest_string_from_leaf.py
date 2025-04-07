"""
https://leetcode.com/problems/smallest-string-starting-from-leaf/description/
"""


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def smallestFromLeaf(self, root: TreeNode) -> str:

        def compare(a, b):
            if not a or not b:
                return a if a else b

            return a if a < b else b

        def helper(node):
            if not node:
                return ""

            left = helper(node.left)
            right = helper(node.right)

            return compare(left, right) + chr(ord("a") + node.val)

        return helper(root)


