"""
https://leetcode.com/problems/insufficient-nodes-in-root-to-leaf-paths/description/
"""


# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def sufficientSubset(self, root, limit):

        def helper(node, total_sum):
            if not node:
                return False

            if not node.left and not node.right:
                total_sum += node.val
                return total_sum >= limit

            left = helper(node.left, total_sum + node.val)
            right = helper(node.right, total_sum + node.val)

            if not left:
                node.left = None
            if not right:
                node.right = None

            return left or right

        helper(root, 0)
        return root