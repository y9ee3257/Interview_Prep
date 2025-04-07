"""
https://leetcode.com/problems/validate-binary-search-tree/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def is_bst(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     bool
    """

    def helper(node, upper_limit, lower_limit):
        if not node:
            return True

        if not (lower_limit <= node.value <= upper_limit):
            return False

        return helper(node.left, node.value, lower_limit) and helper(node.right, upper_limit, node.value)

    return helper(root, float("inf"), float("-inf"))
