"""
Find the height of a given binary tree.
Notes
The height of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

Constraints:

0 <= number of nodes <= 2 * 104
-103 <= value of a binary tree node <= 103

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




