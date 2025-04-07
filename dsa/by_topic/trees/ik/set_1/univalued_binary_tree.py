"""
https://leetcode.com/problems/univalued-binary-tree/description/
"""

"""
For your reference:
class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
"""


def find_single_value_trees(root):
    """
    Args:
     root(BinaryTreeNode_int32)
    Returns:
     int32
    """

    count = [0]

    def helper(node):
        if not node:
            return True

        is_left = helper(node.left)
        is_right = helper(node.right)

        if is_left and is_right and (not node.left or node.left.value == node.value) and (
                not node.right or node.right.value == node.value):
            count[0] += 1
            return True
        else:
            return False

    helper(root)
    return count[0]
