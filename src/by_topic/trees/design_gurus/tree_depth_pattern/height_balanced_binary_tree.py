"""
https://www.geeksforgeeks.org/how-to-determine-if-a-binary-tree-is-balanced/

Determine if a binary tree is height-balanced.

A binary tree is considered height-balanced if, for each node, the difference in height between its left and right subtrees is no more than one.
"""



# class TreeNode:
#    def __init__(self, val=0, left=None, right=None):
#        self.val = val
#        self.left = left
#        self.right = right

class Solution:
    def isBalanced(self, root):
        return self.helper(root)[0]



    def helper(self, root):

        if not root:
            return (True, 0)

        (left_balanced, left_height) = self.helper(root.left)
        (right_balanced, right_height) = self.helper(root.right)

        is_balanced = left_balanced and right_balanced and abs(left_height-right_height) <= 1
        return (is_balanced, max(left_height,right_height)+1)
