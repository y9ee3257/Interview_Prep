"""
https://www.geeksforgeeks.org/convert-a-binary-tree-to-a-circular-doubly-link-list/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

"""


def binary_tree_to_cdll(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     BinaryTreeNode_int32
    """

    def helper(node, direction):

        if not node:
            return

        left = helper(node.left, "left")
        right = helper(node.right, "right")

        node.right = right
        node.left = left

        if right:
            right.left = node

        if left:
            left.right = node

        if direction == "left" and right:
            return right
        elif direction == "right" and left:
            return left
        else:
            return node

    helper(root, "")

    left, right = root, root

    while left.left:
        left = left.left
    while right.right:
        right = right.right

    left.left = right
    right.right = left

    return left
