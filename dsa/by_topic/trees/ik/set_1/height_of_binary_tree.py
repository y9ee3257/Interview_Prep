"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def height_of_binary_tree(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """
    if not root:
        return 0

    return max(height_of_binary_tree(root.left), height_of_binary_tree(root.right)) + 1
