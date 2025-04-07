"""
https://leetcode.com/problems/diameter-of-binary-tree/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def binary_tree_diameter(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    max_diameter = 0

    def helper(node):
        nonlocal max_diameter
        if not node:
            return 0

        left_height = helper(node.left)
        right_height = helper(node.right)
        max_diameter = max(max_diameter, left_height + right_height)
        return max(left_height, right_height) + 1

    helper(root)
    return max_diameter
